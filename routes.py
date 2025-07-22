import logging
import json
from flask import Blueprint, render_template, request, jsonify, flash
from sqlalchemy import text
from app import db
from models import ProductEligibility, AdSalesMetrics, TotalSalesMetrics
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
        'product_eligibility': {
            'description': 'Product eligibility for advertising with reasons',
            'columns': {
                'eligibility_datetime_utc': 'Date and time when eligibility was checked',
                'item_id': 'Product item identifier',
                'eligibility': 'Boolean indicating if product is eligible for ads (TRUE/FALSE)',
                'message': 'Message explaining why product is not eligible (if applicable)'
            }
        },
        'ad_sales_metrics': {
            'description': 'Daily advertising performance metrics by product',
            'columns': {
                'date': 'Date of the metrics',
                'item_id': 'Product item identifier',
                'ad_sales': 'Revenue generated from advertising',
                'impressions': 'Number of ad impressions shown',
                'ad_spend': 'Amount spent on advertising',
                'clicks': 'Number of clicks on ads',
                'units_sold': 'Number of units sold through ads'
            }
        },
        'total_sales_metrics': {
            'description': 'Daily total sales performance by product',
            'columns': {
                'date': 'Date of the metrics',
                'item_id': 'Product item identifier',
                'total_sales': 'Total sales revenue for the product',
                'total_units_ordered': 'Total number of units ordered'
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
            'total_eligibility_records': ProductEligibility.query.count(),
            'total_ad_records': AdSalesMetrics.query.count(),
            'total_sales_records': TotalSalesMetrics.query.count(),
            'total_revenue': db.session.query(db.func.sum(TotalSalesMetrics.total_sales)).scalar() or 0,
            'total_ad_spend': db.session.query(db.func.sum(AdSalesMetrics.ad_spend)).scalar() or 0,
        }
        return jsonify(stats)
    except Exception as e:
        logging.error(f"Stats error: {str(e)}")
        return jsonify({'error': 'Could not retrieve stats'}), 500
