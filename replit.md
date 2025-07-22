# E-commerce AI Agent

## Overview

This is a Flask-based web application that serves as an AI-powered query interface for e-commerce data analysis. The application allows users to ask natural language questions about their e-commerce data, which are then converted to SQL queries using Google's Gemini AI service and executed against a SQLAlchemy database.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Framework**: Flask with SQLAlchemy ORM
- **Database**: SQLite (default) with support for PostgreSQL via environment configuration
- **AI Service**: Google Gemini 2.5 Flash model for natural language to SQL conversion
- **Session Management**: Flask sessions with configurable secret key
- **Proxy Support**: ProxyFix middleware for deployment behind reverse proxies

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Bootstrap 5
- **Styling**: Bootstrap with Replit dark theme and custom CSS
- **JavaScript**: Vanilla JavaScript for form interactions and UI enhancements
- **Icons**: Bootstrap Icons for consistent iconography

### Database Schema
The application uses three main entities:
- **Products**: Core product information (ID, name, category, brand, price, ad eligibility)
- **AdSales**: Advertising campaign performance data (spend, revenue, impressions, clicks, conversion rates)
- **TotalSales**: Overall sales metrics (revenue, units sold, orders, return rates)

## Key Components

### Data Models (`models.py`)
- **Product Model**: Stores product catalog information with foreign key relationships
- **AdSales Model**: Tracks advertising campaign performance metrics including RoAS calculations
- **TotalSales Model**: Aggregates overall sales performance data

### AI Service (`gemini_service.py`)
- **GeminiService Class**: Handles communication with Google's Gemini AI
- **SQL Generation**: Converts natural language questions to SQL queries
- **Schema Context**: Provides database schema information to the AI for accurate query generation

### Route Handlers (`routes.py`)
- **Query Interface**: Web form and API endpoints for question submission
- **Data Processing**: Handles question parsing, SQL execution, and result formatting
- **Error Handling**: Comprehensive error management with user-friendly feedback

### Data Initialization (`data_loader.py`)
- **Sample Data**: Pre-loads the database with realistic e-commerce sample data
- **Product Catalog**: 8 sample products across different categories (Electronics, Clothing, Sports, Kitchen)
- **Campaign Data**: Sample advertising campaigns with performance metrics
- **Sales Data**: Historical sales data for analysis

## Data Flow

1. **User Input**: User submits natural language question via web form or API
2. **AI Processing**: Question is sent to Gemini AI service with database schema context
3. **SQL Generation**: AI generates appropriate SQL query based on the question
4. **Query Execution**: Generated SQL is executed against the database
5. **Result Processing**: Query results are formatted and presented to the user
6. **Error Handling**: Any errors in the pipeline are caught and user-friendly messages are displayed

## External Dependencies

### Required Services
- **Google Gemini AI**: Requires `GEMINI_API_KEY` environment variable
- **Database**: Configurable via `DATABASE_URL` environment variable (defaults to SQLite)

### Python Packages
- **Flask**: Web framework and session management
- **SQLAlchemy**: Database ORM and query building
- **google-genai**: Google Gemini AI client library
- **Werkzeug**: WSGI utilities and proxy support

### Frontend Dependencies
- **Bootstrap 5**: UI framework with Replit dark theme
- **Bootstrap Icons**: Icon library for consistent UI elements

## Deployment Strategy

### Environment Configuration
- **Development**: Uses SQLite database and debug mode enabled
- **Production**: Supports PostgreSQL via `DATABASE_URL` environment variable
- **Security**: Session secret configurable via `SESSION_SECRET` environment variable

### Database Management
- **Auto-initialization**: Creates tables and sample data on first run
- **Connection Pooling**: Configured with connection recycling and health checks
- **Migration Support**: Uses SQLAlchemy's declarative base for schema management

### Hosting Considerations
- **Proxy Support**: Includes ProxyFix middleware for deployment behind load balancers
- **Port Configuration**: Listens on all interfaces (0.0.0.0) on port 5000
- **Logging**: Comprehensive logging for debugging and monitoring

### Scalability Features
- **Database Flexibility**: Easy switching between SQLite (development) and PostgreSQL (production)
- **API Architecture**: RESTful API endpoints support frontend/backend separation
- **Session Management**: Stateless design with session-based user interactions