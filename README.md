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

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ecommerce-ai-agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   export GEMINI_API_KEY="your-gemini-api-key"
   export DATABASE_URL="your-database-url"  # Optional, defaults to SQLite
   export SESSION_SECRET="your-session-secret"  # Optional, random if not set
   ```

4. Run the application:
   ```bash
   gunicorn --bind 0.0.0.0:5000 --reload main:app
   ```

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