import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Configure logging for serverless
logging.basicConfig(level=logging.INFO)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def create_app():
    """Application factory for serverless deployment"""
    app = Flask(__name__)
    app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

    # Configure the database
    database_url = os.environ.get("DATABASE_URL", "sqlite:///ecommerce_ai.db")
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
    }
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the database
    db.init_app(app)

    with app.app_context():
        # Import models
        from models import ProductEligibility, AdSalesMetrics, TotalSalesMetrics
        from routes import main_bp
        
        # Create tables
        db.create_all()
        
        # Register blueprints
        app.register_blueprint(main_bp)
    
    return app

# Create app instance for both local and serverless
app = create_app()

# For local development
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
