import logging
import json
from flask import Blueprint, render_template, request, jsonify, flash
from sqlalchemy import text
from app import db
from models import Product, AdSales, TotalSales
from gemini_service import GeminiService

main_bp = Blueprint('main', __name__)
gemini_service = GeminiService()

@main_bp.route('/')
def index():
    """Home page with basic information about the AI agent."""
    return render_template('index.html')

@main_bp.route('/query', methods=['GET', 'POST'])
def query_page():
    """Query interface for asking questions about the data."""
    if request.method == 'POST':
        return handle_query()
    return render_template('query.html')

@main_bp.route('/api/ask', methods=['POST'])
def api_ask():
    """API endpoint for asking questions about the data."""
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({'error': 'Question is required'}), 400
        
        question = data['question'].strip()
        if not question:
            return jsonify({'error': 'Question cannot be empty'}), 400
        
        result = process_question(question)
        return jsonify(result)
    
    except Exception as e:
        logging.error(f"API error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

def handle_query():
    """Handle form-based query submission."""
    question = request.form.get('question', '').strip()
    
    if not question:
        flash('Please enter a question.', 'error')
        return render_template('query.html')
    
    try:
        result = process_question(question)
        if 'error' in result:
            flash(result['error'], 'error')
            return render_template('query.html')
        else:
            return render_template('query.html', result=result)
    except Exception as e:
        logging.error(f"Query error: {str(e)}")
        flash('An error occurred while processing your question.', 'error')
        return render_template('query.html')

def process_question(question):
    """Process a natural language question and return the answer."""
    try:
        logging.info(f"Processing question: {question}")
        
        # Get database schema information
        schema_info = get_schema_info()
        
        # Generate SQL query using Gemini
        sql_query = gemini_service.generate_sql_query(question, schema_info)
        
        if not sql_query:
            return {'error': 'Could not generate SQL query from your question. Please try rephrasing.'}
        
        logging.info(f"Generated SQL: {sql_query}")
        
        # Execute the query
        query_result = execute_query(sql_query)
        
        if query_result is None:
            return {'error': 'Query execution failed. Please check your question.'}
        
        # Generate human-readable response
        response = gemini_service.format_response(question, sql_query, query_result)
        
        return {
            'question': question,
            'sql_query': sql_query,
            'raw_result': query_result,
            'formatted_response': response,
            'success': True
        }
        
    except Exception as e:
        logging.error(f"Error processing question: {str(e)}")
        return {'error': f'Error processing question: {str(e)}'}

def get_schema_info():
    """Get database schema information for the LLM."""
    schema_info = {
        'products': {
            'description': 'Product information and eligibility',
            'columns': {
                'product_id': 'Unique product identifier',
                'product_name': 'Name of the product',
                'category': 'Product category',
                'brand': 'Product brand',
                'price': 'Product price',
                'is_eligible_for_ads': 'Whether product is eligible for advertising'
            }
        },
        'ad_sales': {
            'description': 'Advertising sales and metrics data',
            'columns': {
                'product_id': 'Product identifier (foreign key)',
                'campaign_name': 'Advertising campaign name',
                'ad_spend': 'Amount spent on advertising',
                'ad_revenue': 'Revenue generated from ads',
                'impressions': 'Number of ad impressions',
                'clicks': 'Number of ad clicks',
                'cpc': 'Cost Per Click',
                'ctr': 'Click Through Rate',
                'conversion_rate': 'Ad conversion rate'
            }
        },
        'total_sales': {
            'description': 'Total sales and metrics data',
            'columns': {
                'product_id': 'Product identifier (foreign key)',
                'total_revenue': 'Total revenue for the product',
                'units_sold': 'Number of units sold',
                'organic_revenue': 'Revenue not from advertising',
                'total_orders': 'Total number of orders',
                'average_order_value': 'Average order value',
                'return_rate': 'Product return rate'
            }
        }
    }
    return schema_info

def execute_query(sql_query):
    """Execute SQL query and return results."""
    try:
        # Clean up the SQL query
        sql_query = sql_query.strip()
        if sql_query.endswith(';'):
            sql_query = sql_query[:-1]
        
        result = db.session.execute(text(sql_query))
        
        # Convert result to list of dictionaries
        rows = []
        if hasattr(result, 'returns_rows') and result.returns_rows:
            columns = result.keys()
            for row in result:
                row_dict = dict(zip(columns, row))
                rows.append(row_dict)
        else:
            # For non-SELECT queries or when returns_rows is not available
            try:
                columns = result.keys()
                for row in result:
                    row_dict = dict(zip(columns, row))
                    rows.append(row_dict)
            except:
                rows = [{'message': 'Query executed successfully'}]
        
        return rows
        
    except Exception as e:
        logging.error(f"Query execution error: {str(e)}")
        return None

@main_bp.route('/api/stats')
def api_stats():
    """Get basic statistics about the data."""
    try:
        stats = {
            'total_products': Product.query.count(),
            'total_ad_campaigns': AdSales.query.count(),
            'total_sales_records': TotalSales.query.count(),
            'total_revenue': db.session.query(db.func.sum(TotalSales.total_revenue)).scalar() or 0,
            'total_ad_spend': db.session.query(db.func.sum(AdSales.ad_spend)).scalar() or 0,
        }
        return jsonify(stats)
    except Exception as e:
        logging.error(f"Stats error: {str(e)}")
        return jsonify({'error': 'Could not retrieve stats'}), 500
