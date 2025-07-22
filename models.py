from app import db
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(50), unique=True, nullable=False)
    product_name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_eligible_for_ads = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Product {self.product_name}>'

class AdSales(db.Model):
    __tablename__ = 'ad_sales'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(50), db.ForeignKey('products.product_id'), nullable=False)
    campaign_name = db.Column(db.String(200), nullable=False)
    ad_spend = db.Column(db.Float, nullable=False)
    ad_revenue = db.Column(db.Float, nullable=False)
    impressions = db.Column(db.Integer, nullable=False)
    clicks = db.Column(db.Integer, nullable=False)
    cpc = db.Column(db.Float, nullable=False)  # Cost Per Click
    ctr = db.Column(db.Float, nullable=False)  # Click Through Rate
    conversion_rate = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship to Product
    product = db.relationship('Product', backref=db.backref('ad_sales', lazy=True))
    
    def __repr__(self):
        return f'<AdSales {self.product_id} - {self.campaign_name}>'

class TotalSales(db.Model):
    __tablename__ = 'total_sales'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(50), db.ForeignKey('products.product_id'), nullable=False)
    total_revenue = db.Column(db.Float, nullable=False)
    units_sold = db.Column(db.Integer, nullable=False)
    organic_revenue = db.Column(db.Float, nullable=False)  # Revenue not from ads
    total_orders = db.Column(db.Integer, nullable=False)
    average_order_value = db.Column(db.Float, nullable=False)
    return_rate = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship to Product
    product = db.relationship('Product', backref=db.backref('total_sales', lazy=True))
    
    def __repr__(self):
        return f'<TotalSales {self.product_id}>'
