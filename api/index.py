import os
import json
import logging
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, Date, text
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "vercel-secret-key")

# Database configuration
database_url = os.environ.get("DATABASE_URL", "sqlite:///memory:")
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
db.init_app(app)

# Define models inline for serverless
class ProductEligibility(db.Model):
    __tablename__ = 'product_eligibility'
    id = Column(Integer, primary_key=True)
    item_id = Column(String(50), nullable=False)
    eligibility_status = Column(String(20), nullable=False)
    eligibility_datetime_utc = Column(DateTime, nullable=False)
    reason = Column(Text)

class AdSalesMetrics(db.Model):
    __tablename__ = 'ad_sales_metrics'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    item_id = Column(String(50), nullable=False)
    ad_sales = Column(Float, default=0.0)
    impressions = Column(Integer, default=0)
    ad_spend = Column(Float, default=0.0)
    clicks = Column(Integer, default=0)
    units_sold_ad = Column(Integer, default=0)

class TotalSalesMetrics(db.Model):
    __tablename__ = 'total_sales_metrics'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    item_id = Column(String(50), nullable=False)
    total_sales = Column(Float, default=0.0)
    total_units_ordered = Column(Integer, default=0)

# Gemini service
class GeminiService:
    def __init__(self):
        try:
            from google import genai
            self.client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
            self.model = "gemini-2.5-flash"
            self.available = True
        except Exception as e:
            logging.error(f"Gemini service initialization failed: {e}")
            self.available = False
    
    def generate_sql_query(self, question, schema_info):
        if not self.available:
            raise Exception("Gemini service not available")
            
        system_prompt = f"""Generate a SQL query for: {question}
        
Database Schema:
- product_eligibility: item_id, eligibility_status, eligibility_datetime_utc, reason
- ad_sales_metrics: date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold_ad
- total_sales_metrics: date, item_id, total_sales, total_units_ordered

Return only the SQL query, no explanation."""

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=system_prompt
            )
            return response.text.strip()
        except Exception as e:
            raise Exception(f"Failed to generate SQL: {e}")

# Routes
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>E-commerce AI Agent</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            .container { background: #f5f5f5; padding: 20px; border-radius: 10px; }
            input[type="text"] { width: 100%; padding: 10px; margin: 10px 0; }
            button { background: #007cba; color: white; padding: 10px 20px; border: none; border-radius: 5px; }
            .result { background: white; padding: 15px; margin: 10px 0; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>E-commerce AI Agent</h1>
            <p>Ask questions about your e-commerce data in natural language:</p>
            
            <input type="text" id="question" placeholder="What is my total sales?" />
            <button onclick="askQuestion()">Ask</button>
            
            <div id="result"></div>
        </div>
        
        <script>
        async function askQuestion() {
            const question = document.getElementById('question').value;
            const resultDiv = document.getElementById('result');
            
            if (!question.trim()) {
                resultDiv.innerHTML = '<div class="result">Please enter a question</div>';
                return;
            }
            
            resultDiv.innerHTML = '<div class="result">Processing...</div>';
            
            try {
                const response = await fetch('/api/query', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ question })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    resultDiv.innerHTML = `
                        <div class="result">
                            <h3>Answer:</h3>
                            <p>${data.response || 'Query executed successfully'}</p>
                            <h4>SQL Query:</h4>
                            <code>${data.sql_query}</code>
                            <h4>Data:</h4>
                            <pre>${JSON.stringify(data.data, null, 2)}</pre>
                        </div>
                    `;
                } else {
                    resultDiv.innerHTML = `<div class="result">Error: ${data.error}</div>`;
                }
            } catch (error) {
                resultDiv.innerHTML = `<div class="result">Network error: ${error.message}</div>`;
            }
        }
        </script>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    status = {
        'status': 'healthy',
        'database': 'not configured',
        'gemini': 'not configured'
    }
    
    # Check database
    try:
        with app.app_context():
            db.session.execute(text('SELECT 1'))
        status['database'] = 'connected'
    except:
        status['database'] = 'disconnected'
    
    # Check Gemini
    if os.environ.get('GEMINI_API_KEY'):
        status['gemini'] = 'configured'
    
    return jsonify(status)

@app.route('/api/query', methods=['POST'])
def api_query():
    try:
        # Check environment variables
        if not os.environ.get('GEMINI_API_KEY'):
            return jsonify({
                'error': 'GEMINI_API_KEY not configured. Please set it in Vercel environment variables.',
                'success': False
            }), 500
        
        if not os.environ.get('DATABASE_URL'):
            return jsonify({
                'error': 'DATABASE_URL not configured. Please set it in Vercel environment variables.',
                'success': False
            }), 500
        
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({'error': 'No question provided', 'success': False}), 400
        
        question = data['question'].strip()
        if not question:
            return jsonify({'error': 'Empty question', 'success': False}), 400
        
        # Initialize Gemini service
        gemini_service = GeminiService()
        
        # Generate SQL query
        sql_query = gemini_service.generate_sql_query(question, {})
        
        # Execute SQL query
        with app.app_context():
            result = db.session.execute(text(sql_query))
            rows = result.fetchall()
            columns = result.keys()
            data_result = [dict(zip(columns, row)) for row in rows]
        
        return jsonify({
            'question': question,
            'sql_query': sql_query,
            'data': data_result,
            'response': f"Found {len(data_result)} results for your query.",
            'success': True
        })
        
    except Exception as e:
        logging.error(f"Error processing query: {str(e)}")
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

# Create tables
with app.app_context():
    db.create_all()

# Export app for Vercel
if __name__ == "__main__":
    app.run(debug=True)