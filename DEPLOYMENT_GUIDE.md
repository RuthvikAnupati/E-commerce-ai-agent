# E-commerce AI Agent - Deployment Guide

Your project is now on GitHub at: https://github.com/RuthvikAnupati/E-commerce-ai-agent

## Production Deployment Options

### Option 1: Deploy on Replit (Easiest)

1. **From your current Replit:**
   - Click "Deploy" button in the top toolbar
   - Choose "Replit Deployments"
   - Your app will be live at `yourapp.replit.app`
   - Automatic HTTPS and scaling included

2. **Environment Setup:**
   - Add your `GEMINI_API_KEY` in Secrets tab
   - Database will use PostgreSQL automatically

### Option 2: Deploy on Railway (Popular)

1. **In your current Replit project:**
   - Click the **"Version Control"** tab in the left sidebar (looks like a branch icon)
   - Or go to the **Shell** tab at the bottom

2. **In the Shell, run these commands:**
   ```bash
   git add .
   git commit -m "Initial commit: E-commerce AI Agent with real data"
   ```

3. **Create a new GitHub repository:**
   - Go to [github.com](https://github.com) → Click "+" → "New repository"
   - Name it: `ecommerce-ai-agent`
   - Don't initialize with README
   - Copy the repository URL

4. **Push to GitHub:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/ecommerce-ai-agent.git
   git branch -M main
   git push -u origin main
   ```

## Option 2: Using Replit's GitHub Integration

1. **Connect to GitHub:**
   - In Replit, click your profile → "Account"
   - Go to "Connected services" → Connect GitHub

2. **Create from Replit:**
   - In your current project, click the "Version Control" tab
   - Click "Create a Git repository"
   - Choose "Push to GitHub"
   - Follow the prompts to create the repository

## Authentication
If prompted for credentials:
- Username: Your GitHub username
- Password: Use a Personal Access Token (not your password)
  - Go to GitHub → Settings → Developer settings → Personal access tokens
  - Generate new token with "repo" permissions

## What Gets Uploaded
Your repository will include:
- ✅ Complete AI agent source code
- ✅ Real e-commerce datasets (4,382+ records)
- ✅ Professional README with setup instructions
- ✅ Proper .gitignore and LICENSE files
- ✅ Over $1M in authentic revenue data

1. **Connect GitHub:**
   - Go to [railway.app](https://railway.app)
   - Sign in with GitHub
   - Click "Deploy from GitHub repo"
   - Select `RuthvikAnupati/E-commerce-ai-agent`

2. **Add Environment Variables:**
   - `GEMINI_API_KEY` = Your Google Gemini API key
   - Railway will provide PostgreSQL automatically

3. **Deploy:**
   - Railway detects Python and deploys automatically
   - Live at your custom Railway domain

### Option 3: Deploy on Heroku

1. **Create Heroku App:**
   ```bash
   heroku create your-ecommerce-ai
   heroku addons:create heroku-postgresql:mini
   ```

2. **Set Environment Variables:**
   ```bash
   heroku config:set GEMINI_API_KEY=your-key
   heroku config:set SESSION_SECRET=random-secret-string
   ```

3. **Deploy:**
   ```bash
   git push heroku main
   ```

### Option 4: Deploy on Vercel

1. **Connect Repository:**
   - Go to [vercel.com](https://vercel.com)
   - Import from GitHub: `RuthvikAnupati/E-commerce-ai-agent`

2. **Configuration:**
   - Framework: Other
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn main:app`

3. **Environment Variables:**
   - Add `GEMINI_API_KEY`
   - Add external PostgreSQL database URL

## Required Environment Variables

For all deployment platforms, you need:
- `GEMINI_API_KEY` - Your Google Gemini API key
- `DATABASE_URL` - PostgreSQL connection (usually auto-provided)
- `SESSION_SECRET` - Random string for session security

## What Gets Deployed

Your live application includes:
- ✅ AI-powered query interface
- ✅ Real CSV datasets (4,382+ records)
- ✅ Over $1M in revenue data
- ✅ Natural language to SQL conversion
- ✅ Professional web interface
- ✅ REST API endpoints

## Post-Deployment

Once deployed, users can:
- Ask questions like "What's my total sales?"
- Query advertising metrics and ROI
- Analyze product performance
- Access via web interface or API

Your E-commerce AI Agent will be production-ready with real business data!