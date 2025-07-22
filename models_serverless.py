import os
import sys
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, Date
from datetime import datetime

# Import db from the api directory if in serverless, otherwise from main
try:
    from api.main import db
except ImportError:
    from main import db

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