import os
import json
import logging
from google import genai
from google.genai import types

class GeminiService:
    def __init__(self):
        self.client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
        self.model = "gemini-2.5-flash"
    
    def generate_sql_query(self, question, schema_info):
        """Convert natural language question to SQL query."""
        try:
            # Create schema description for the prompt
            schema_description = self._format_schema_for_prompt(schema_info)
            
            system_prompt = f"""
You are an expert SQL query generator for an e-commerce database. Given a natural language question, generate a precise SQL query.

Database Schema:
{schema_description}

Important Guidelines:
1. Only generate SELECT queries for data retrieval
2. Use proper JOIN statements when querying multiple tables using item_id as the join key
3. Use aggregate functions (SUM, AVG, COUNT, MAX, MIN) appropriately
4. For RoAS (Return on Ad Spend) calculation: SUM(ad_sales) / SUM(ad_spend)
5. For CPC (Cost Per Click) calculation: ad_spend / clicks (when clicks > 0)
6. Always use proper WHERE clauses when filtering is needed
7. Return only the SQL query without any explanation or formatting
8. Do not include semicolons at the end
9. Use proper column aliases for calculated fields
10. Use item_id to identify products across tables

Example queries for reference:
- Total sales: SELECT SUM(total_sales) as total_sales FROM total_sales_metrics
- RoAS calculation: SELECT (SUM(ad_sales) / SUM(ad_spend)) as roas FROM ad_sales_metrics WHERE ad_spend > 0
- Highest CPC: SELECT item_id, MAX(ad_spend / NULLIF(clicks, 0)) as highest_cpc FROM ad_sales_metrics WHERE clicks > 0 GROUP BY item_id ORDER BY highest_cpc DESC LIMIT 1
- Products with most ad spend: SELECT item_id, SUM(ad_spend) as total_spend FROM ad_sales_metrics GROUP BY item_id ORDER BY total_spend DESC LIMIT 10
"""

            user_prompt = f"Convert this question to SQL: {question}"
            
            response = self.client.models.generate_content(
                model=self.model,
                contents=[
                    types.Content(role="user", parts=[types.Part(text=user_prompt)])
                ],
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    temperature=0.1,
                    max_output_tokens=500
                )
            )
            
            if response.text:
                sql_query = response.text.strip()
                # Remove code block formatting if present
                if sql_query.startswith('```sql'):
                    sql_query = sql_query[6:]
                if sql_query.startswith('```'):
                    sql_query = sql_query[3:]
                if sql_query.endswith('```'):
                    sql_query = sql_query[:-3]
                
                return sql_query.strip()
            
            return None
            
        except Exception as e:
            logging.error(f"Error generating SQL query: {str(e)}")
            return None
    
    def format_response(self, question, sql_query, query_result):
        """Format query results into human-readable response."""
        try:
            system_prompt = """
You are an expert data analyst. Given a question, SQL query, and query results, provide a clear, human-readable answer.

Guidelines:
1. Provide a direct answer to the question
2. Include relevant numbers and calculations
3. Format currency values appropriately 
4. Explain any calculations performed
5. Keep the response concise but informative
6. If the result contains multiple rows, summarize appropriately
"""

            user_prompt = f"""
Question: {question}
SQL Query: {sql_query}
Query Results: {json.dumps(query_result, default=str)}

Please provide a human-readable answer to the question based on the query results.
"""

            response = self.client.models.generate_content(
                model=self.model,
                contents=[
                    types.Content(role="user", parts=[types.Part(text=user_prompt)])
                ],
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    temperature=0.3,
                    max_output_tokens=300
                )
            )
            
            return response.text if response.text else "Unable to format response."
            
        except Exception as e:
            logging.error(f"Error formatting response: {str(e)}")
            return f"Query executed successfully. Raw result: {query_result}"
    
    def _format_schema_for_prompt(self, schema_info):
        """Format schema information for the LLM prompt."""
        schema_text = ""
        for table_name, table_info in schema_info.items():
            schema_text += f"\nTable: {table_name}\n"
            schema_text += f"Description: {table_info['description']}\n"
            schema_text += "Columns:\n"
            for col_name, col_desc in table_info['columns'].items():
                schema_text += f"  - {col_name}: {col_desc}\n"
        
        return schema_text
