# E-commerce AI Agent

An intelligent AI-powered query interface for e-commerce data analysis that converts natural language questions into SQL queries and provides human-readable insights.

## Features

- **Natural Language Processing**: Ask questions in plain English about your e-commerce data
- **Real-time SQL Generation**: Uses Google's Gemini AI to convert questions to accurate SQL queries
- **Multi-table Analysis**: Analyzes product eligibility, advertising metrics, and sales performance
- **Web Interface**: User-friendly web application with Bootstrap styling
- **REST API**: Programmatic access for integration with other systems

## Tech Stack

- **Backend**: Flask with SQLAlchemy ORM
- **Database**: PostgreSQL (production) / SQLite (development)
- **AI Service**: Google Gemini 2.5 Flash
- **Frontend**: Bootstrap 5 with Replit dark theme
- **Deployment**: Gunicorn WSGI server

## Data Sources

The application works with three main datasets:

1. **Product Eligibility**: Advertising eligibility status with detailed reasons
2. **Ad Sales Metrics**: Daily advertising performance (spend, sales, impressions, clicks)
3. **Total Sales Metrics**: Daily sales performance (revenue, units ordered)

## Quick Start

1. **Clone and Setup**:
   ```bash
   git clone <repository-url>
   cd ecommerce-ai-agent
   pip install flask flask-sqlalchemy google-genai gunicorn psycopg2-binary email-validator
   ```

2. **Configure Environment**:
   ```bash
   export GEMINI_API_KEY="your-google-gemini-api-key"
   export DATABASE_URL="postgresql://user:pass@host:port/db"  # Optional
   ```

3. **Run the Application**:
   ```bash
   gunicorn --bind 0.0.0.0:5000 --reload main:app
   ```

4. **Access the AI Agent**:
   - Web Interface: `http://localhost:5000`
   - API: `POST http://localhost:5000/api/query`

## Data Integration

This project includes real e-commerce datasets:
- **4,382 product eligibility records** with advertising approval status
- **3,696 daily ad performance metrics** (spend, sales, impressions, clicks)
- **702 daily sales records** with revenue and unit data
- **Total Revenue**: Over $1M in authentic business data

## Usage

### Web Interface

Visit `http://localhost:5000` to access the web interface where you can:
- Ask natural language questions about your data
- View generated SQL queries
- See formatted results and insights

### API Endpoints

- `POST /api/query` - Submit a natural language question
- `GET /api/stats` - Get basic database statistics

### Example Questions

- "What is my total sales?"
- "Which products are not eligible for ads and why?"
- "Calculate my RoAS by product"
- "Show me the best performing items by ad spend"
- "What's the average click-through rate?"

## Architecture

- **Flask Application** (`app.py`, `main.py`): Core web application setup
- **Database Models** (`models.py`): SQLAlchemy models for data structure
- **Route Handlers** (`routes.py`): Web endpoints and API logic
- **AI Service** (`gemini_service.py`): Google Gemini AI integration
- **Data Loader** (`data_loader.py`): CSV data import utilities

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.