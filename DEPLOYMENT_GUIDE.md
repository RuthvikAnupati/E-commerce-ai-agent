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

### Option 4: Deploy on Vercel (Detailed Steps)

#### Step 1: Fix Vercel Build Issue
The build failed because of missing requirements.txt. Here's the solution:

**In your Replit Shell, run:**
```bash
# Copy the requirements file
cp requirements-vercel.txt requirements.txt

# Push the fix to GitHub
git add vercel.json runtime.txt requirements.txt requirements-vercel.txt
git commit -m "Fix Vercel deployment - add proper requirements.txt"
git push origin main
```

#### Step 2: Create Vercel Account & Import Project
1. **Go to [vercel.com](https://vercel.com)**
2. **Sign up/Login** with GitHub account
3. **Click "New Project"**
4. **Import from GitHub:** Search for `E-commerce-ai-agent`
5. **Select your repository:** `RuthvikAnupati/E-commerce-ai-agent`
6. **Click "Import"**

#### Step 3: Configure Project Settings
**Framework Preset:** Other  
**Root Directory:** `./` (leave default)  
**Build and Output Settings:**
- Build Command: (leave empty - Vercel will use requirements.txt automatically)
- Output Directory: (leave empty)
- Install Command: (leave default)

#### Step 4: Set Up Database
**Option A: Use Neon (Free PostgreSQL)**
1. Go to [neon.tech](https://neon.tech) → Create account
2. Create new project: "ecommerce-ai-agent"
3. Copy the connection string (looks like: `postgresql://user:pass@host/db`)

**Option B: Use Supabase (Free PostgreSQL)**
1. Go to [supabase.com](https://supabase.com) → Create account
2. New project → Get connection string
3. Enable "Use connection pooling"

#### Step 5: Configure Environment Variables in Vercel
In your Vercel project settings:
1. **Go to Settings → Environment Variables**
2. **Add these variables:**
   - `GEMINI_API_KEY` = Your Google Gemini API key
   - `DATABASE_URL` = Your PostgreSQL connection string
   - `SESSION_SECRET` = Any random string (e.g., `my-secret-key-2025`)

#### Step 6: Deploy & Test
1. **Click "Deploy"** - Vercel will build and deploy automatically
2. **Your app will be live at:** `your-project-name.vercel.app`
3. **Test the deployment:** Visit the URL and try asking a question

#### Step 7: Load Your Data
Since Vercel is serverless, you need to trigger data loading:
1. **Visit your deployed app**
2. **The data loader runs automatically** on first visit
3. **Your 4,382+ records and $1M+ revenue data** will be loaded

#### Step 8: Custom Domain (Optional)
1. **Go to Settings → Domains**
2. **Add your custom domain:** `yourbusiness.com`
3. **Configure DNS** as instructed by Vercel
4. **Get SSL certificate** (automatic)

#### Troubleshooting Common Issues:
- **Build fails:** Check that all environment variables are set
- **Database connection:** Verify DATABASE_URL format
- **Gemini API:** Ensure GEMINI_API_KEY is valid
- **Data loading:** Visit `/` to trigger automatic data import

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