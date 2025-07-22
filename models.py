from main import db
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, Date
from datetime import datetime

class ProductEligibility(db.Model):
    __tablename__ = 'product_eligibility'
    
    id = db.Column(db.Integer, primary_key=True)
    eligibility_datetime_utc = db.Column(db.DateTime, nullable=False)
    item_id = db.Column(db.Integer, nullable=False)
    eligibility = db.Column(db.Boolean, nullable=False)
    message = db.Column(db.Text)
    
    def __repr__(self):
        return f'<ProductEligibility {self.item_id} - {self.eligibility}>'

class AdSalesMetrics(db.Model):
    __tablename__ = 'ad_sales_metrics'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    item_id = db.Column(db.Integer, nullable=False)
    ad_sales = db.Column(db.Float, nullable=False)
    impressions = db.Column(db.Integer, nullable=False)
    ad_spend = db.Column(db.Float, nullable=False)
    clicks = db.Column(db.Integer, nullable=False)
    units_sold = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<AdSalesMetrics {self.item_id} - {self.date}>'

class TotalSalesMetrics(db.Model):
    __tablename__ = 'total_sales_metrics'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    item_id = db.Column(db.Integer, nullable=False)
    total_sales = db.Column(db.Float, nullable=False)
    total_units_ordered = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<TotalSalesMetrics {self.item_id} - {self.date}>'
