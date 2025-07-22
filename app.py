import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///ecommerce_ai.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database
db.init_app(app)

with app.app_context():
    # Import models to ensure tables are created
    from models import ProductEligibility, AdSalesMetrics, TotalSalesMetrics
    from routes import main_bp
    from data_loader import initialize_sample_data
    
    # Create all tables
    db.create_all()
    
    # Initialize with sample data if tables are empty
    initialize_sample_data()
    
    # Register blueprints
    app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
