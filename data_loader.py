import logging
import csv
import os
from datetime import datetime, date
from app import db
from models import ProductEligibility, AdSalesMetrics, TotalSalesMetrics

def initialize_sample_data():
    """Initialize the database with real CSV data if it's empty."""
    try:
        # Check if data already exists
        if ProductEligibility.query.count() > 0:
            logging.info("Database already has data, skipping initialization.")
            return
        
        logging.info("Loading real CSV data into database...")
        
        # Load Product Eligibility data
        load_product_eligibility()
        
        # Load Ad Sales Metrics data
        load_ad_sales_metrics()
        
        # Load Total Sales Metrics data
        load_total_sales_metrics()
        
        # Commit all changes
        db.session.commit()
        logging.info("Real CSV data loaded successfully!")
        
    except Exception as e:
        logging.error(f"Error loading CSV data: {str(e)}")
        db.session.rollback()
        raise

def load_product_eligibility():
    """Load product eligibility data from CSV."""
    csv_path = 'attached_assets/Product-Level Eligibility Table (mapped) - Product-Level Eligibility Table (mapped)_1753179705317.csv'
    
    if not os.path.exists(csv_path):
        logging.warning(f"CSV file not found: {csv_path}")
        return
    
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        batch_size = 1000
        records = []
        
        for row in reader:
            try:
                # Parse datetime
                dt_str = row['eligibility_datetime_utc']
                dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
                
                eligibility = ProductEligibility(
                    eligibility_datetime_utc=dt,
                    item_id=int(row['item_id']),
                    eligibility=row['eligibility'].upper() == 'TRUE',
                    message=row['message'] if row['message'] else None
                )
                records.append(eligibility)
                
                if len(records) >= batch_size:
                    db.session.bulk_save_objects(records)
                    db.session.commit()
                    records = []
                    logging.info(f"Loaded {batch_size} eligibility records...")
                    
            except Exception as e:
                logging.error(f"Error processing eligibility row: {row}, error: {str(e)}")
                continue
        
        # Save remaining records
        if records:
            db.session.bulk_save_objects(records)
            db.session.commit()
            logging.info(f"Loaded final {len(records)} eligibility records")

def load_ad_sales_metrics():
    """Load ad sales metrics data from CSV."""
    csv_path = 'attached_assets/Product-Level Ad Sales and Metrics (mapped) - Product-Level Ad Sales and Metrics (mapped)_1753179705318.csv'
    
    if not os.path.exists(csv_path):
        logging.warning(f"CSV file not found: {csv_path}")
        return
    
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        batch_size = 1000
        records = []
        
        for row in reader:
            try:
                # Parse date
                date_str = row['date']
                parsed_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                
                ad_metrics = AdSalesMetrics(
                    date=parsed_date,
                    item_id=int(row['item_id']),
                    ad_sales=float(row['ad_sales']) if row['ad_sales'] else 0.0,
                    impressions=int(row['impressions']) if row['impressions'] else 0,
                    ad_spend=float(row['ad_spend']) if row['ad_spend'] else 0.0,
                    clicks=int(row['clicks']) if row['clicks'] else 0,
                    units_sold=int(row['units_sold']) if row['units_sold'] else 0
                )
                records.append(ad_metrics)
                
                if len(records) >= batch_size:
                    db.session.bulk_save_objects(records)
                    db.session.commit()
                    records = []
                    logging.info(f"Loaded {batch_size} ad sales records...")
                    
            except Exception as e:
                logging.error(f"Error processing ad sales row: {row}, error: {str(e)}")
                continue
        
        # Save remaining records
        if records:
            db.session.bulk_save_objects(records)
            db.session.commit()
            logging.info(f"Loaded final {len(records)} ad sales records")

def load_total_sales_metrics():
    """Load total sales metrics data from CSV."""
    csv_path = 'attached_assets/Product-Level Total Sales and Metrics (mapped) - Product-Level Total Sales and Metrics (mapped)_1753179705319.csv'
    
    if not os.path.exists(csv_path):
        logging.warning(f"CSV file not found: {csv_path}")
        return
    
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        batch_size = 1000
        records = []
        
        for row in reader:
            try:
                # Parse date
                date_str = row['date']
                parsed_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                
                sales_metrics = TotalSalesMetrics(
                    date=parsed_date,
                    item_id=int(row['item_id']),
                    total_sales=float(row['total_sales']) if row['total_sales'] else 0.0,
                    total_units_ordered=int(row['total_units_ordered']) if row['total_units_ordered'] else 0
                )
                records.append(sales_metrics)
                
                if len(records) >= batch_size:
                    db.session.bulk_save_objects(records)
                    db.session.commit()
                    records = []
                    logging.info(f"Loaded {batch_size} total sales records...")
                    
            except Exception as e:
                logging.error(f"Error processing total sales row: {row}, error: {str(e)}")
                continue
        
        # Save remaining records
        if records:
            db.session.bulk_save_objects(records)
            db.session.commit()
            logging.info(f"Loaded final {len(records)} total sales records")
