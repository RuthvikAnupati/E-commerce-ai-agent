import os
import sys
from flask import Flask, render_template, request, jsonify

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import your app
try:
    from main import app
except ImportError:
    # Fallback if main.py not working in serverless
    app = Flask(__name__)
    app.secret_key = os.environ.get("SESSION_SECRET", "fallback-secret")
    
    @app.route('/')
    def home():
        return """
        <html>
        <head><title>E-commerce AI Agent</title></head>
        <body>
            <h1>E-commerce AI Agent</h1>
            <p>Serverless deployment successful! Database connection needed.</p>
            <p>Please configure DATABASE_URL and GEMINI_API_KEY environment variables.</p>
        </body>
        </html>
        """
    
    @app.route('/health')
    def health():
        return {"status": "ok", "message": "Serverless function is running"}

# Handler for Vercel
def handler(request):
    return app(request.environ, request.start_response)

# For direct access
if __name__ == "__main__":
    app.run(debug=True)