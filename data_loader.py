import logging
from datetime import datetime, timedelta
from app import db
from models import Product, AdSales, TotalSales

def initialize_sample_data():
    """Initialize the database with sample e-commerce data if it's empty."""
    try:
        # Check if data already exists
        if Product.query.count() > 0:
            logging.info("Database already has data, skipping initialization.")
            return
        
        logging.info("Initializing database with sample data...")
        
        # Create sample products
        products_data = [
            {'product_id': 'P001', 'product_name': 'Wireless Bluetooth Headphones', 'category': 'Electronics', 'brand': 'TechBrand', 'price': 99.99, 'is_eligible_for_ads': True},
            {'product_id': 'P002', 'product_name': 'Smart Fitness Watch', 'category': 'Electronics', 'brand': 'FitTech', 'price': 199.99, 'is_eligible_for_ads': True},
            {'product_id': 'P003', 'product_name': 'Organic Cotton T-Shirt', 'category': 'Clothing', 'brand': 'EcoWear', 'price': 29.99, 'is_eligible_for_ads': True},
            {'product_id': 'P004', 'product_name': 'Gaming Mechanical Keyboard', 'category': 'Electronics', 'brand': 'GamePro', 'price': 149.99, 'is_eligible_for_ads': True},
            {'product_id': 'P005', 'product_name': 'Yoga Mat Premium', 'category': 'Sports', 'brand': 'FlexFit', 'price': 59.99, 'is_eligible_for_ads': False},
            {'product_id': 'P006', 'product_name': 'Coffee Maker Deluxe', 'category': 'Kitchen', 'brand': 'BrewMaster', 'price': 299.99, 'is_eligible_for_ads': True},
            {'product_id': 'P007', 'product_name': 'Running Shoes Pro', 'category': 'Sports', 'brand': 'SpeedRun', 'price': 129.99, 'is_eligible_for_ads': True},
            {'product_id': 'P008', 'product_name': 'Smartphone Case', 'category': 'Electronics', 'brand': 'ProtectPlus', 'price': 19.99, 'is_eligible_for_ads': True}
        ]
        
        for product_data in products_data:
            product = Product(**product_data)
            db.session.add(product)
        
        # Create sample ad sales data
        ad_sales_data = [
            {'product_id': 'P001', 'campaign_name': 'Holiday Electronics Sale', 'ad_spend': 500.00, 'ad_revenue': 1200.00, 'impressions': 10000, 'clicks': 250, 'cpc': 2.00, 'ctr': 2.5, 'conversion_rate': 8.0},
            {'product_id': 'P002', 'campaign_name': 'Fitness New Year Campaign', 'ad_spend': 800.00, 'ad_revenue': 2000.00, 'impressions': 15000, 'clicks': 400, 'cpc': 2.00, 'ctr': 2.67, 'conversion_rate': 10.0},
            {'product_id': 'P003', 'campaign_name': 'Sustainable Fashion Week', 'ad_spend': 200.00, 'ad_revenue': 360.00, 'impressions': 5000, 'clicks': 100, 'cpc': 2.00, 'ctr': 2.0, 'conversion_rate': 12.0},
            {'product_id': 'P004', 'campaign_name': 'Gaming Gear Promo', 'ad_spend': 600.00, 'ad_revenue': 1350.00, 'impressions': 8000, 'clicks': 150, 'cpc': 4.00, 'ctr': 1.88, 'conversion_rate': 15.0},
            {'product_id': 'P006', 'campaign_name': 'Kitchen Essentials', 'ad_spend': 400.00, 'ad_revenue': 900.00, 'impressions': 6000, 'clicks': 120, 'cpc': 3.33, 'ctr': 2.0, 'conversion_rate': 7.5},
            {'product_id': 'P007', 'campaign_name': 'Running Season Launch', 'ad_spend': 350.00, 'ad_revenue': 780.00, 'impressions': 7000, 'clicks': 140, 'cpc': 2.50, 'ctr': 2.0, 'conversion_rate': 9.0},
            {'product_id': 'P008', 'campaign_name': 'Mobile Accessories Bundle', 'ad_spend': 150.00, 'ad_revenue': 240.00, 'impressions': 3000, 'clicks': 75, 'cpc': 2.00, 'ctr': 2.5, 'conversion_rate': 16.0}
        ]
        
        for ad_data in ad_sales_data:
            ad_sale = AdSales(**ad_data)
            db.session.add(ad_sale)
        
        # Create sample total sales data
        total_sales_data = [
            {'product_id': 'P001', 'total_revenue': 2500.00, 'units_sold': 25, 'organic_revenue': 1300.00, 'total_orders': 22, 'average_order_value': 113.64, 'return_rate': 5.0},
            {'product_id': 'P002', 'total_revenue': 4000.00, 'units_sold': 20, 'organic_revenue': 2000.00, 'total_orders': 18, 'average_order_value': 222.22, 'return_rate': 3.0},
            {'product_id': 'P003', 'total_revenue': 750.00, 'units_sold': 25, 'organic_revenue': 390.00, 'total_orders': 23, 'average_order_value': 32.61, 'return_rate': 8.0},
            {'product_id': 'P004', 'total_revenue': 2250.00, 'units_sold': 15, 'organic_revenue': 900.00, 'total_orders': 13, 'average_order_value': 173.08, 'return_rate': 4.0},
            {'product_id': 'P005', 'total_revenue': 1200.00, 'units_sold': 20, 'organic_revenue': 1200.00, 'total_orders': 18, 'average_order_value': 66.67, 'return_rate': 2.0},
            {'product_id': 'P006', 'total_revenue': 1800.00, 'units_sold': 6, 'organic_revenue': 900.00, 'total_orders': 5, 'average_order_value': 360.00, 'return_rate': 10.0},
            {'product_id': 'P007', 'total_revenue': 1560.00, 'units_sold': 12, 'organic_revenue': 780.00, 'total_orders': 11, 'average_order_value': 141.82, 'return_rate': 6.0},
            {'product_id': 'P008', 'total_revenue': 400.00, 'units_sold': 20, 'organic_revenue': 160.00, 'total_orders': 18, 'average_order_value': 22.22, 'return_rate': 15.0}
        ]
        
        for sales_data in total_sales_data:
            total_sale = TotalSales(**sales_data)
            db.session.add(total_sale)
        
        # Commit all changes
        db.session.commit()
        logging.info("Sample data initialized successfully!")
        
    except Exception as e:
        logging.error(f"Error initializing sample data: {str(e)}")
        db.session.rollback()
        raise
