# Complete Vercel Deployment Guide for E-commerce AI Agent

Your GitHub Repository: **https://github.com/RuthvikAnupati/E-commerce-ai-agent**

## Prerequisites Checklist ✅

- [x] GitHub repository with all code
- [x] Google Gemini API key
- [x] Vercel configuration files (vercel.json, runtime.txt, requirements.txt)
- [x] Real e-commerce data (4,382+ records, $1M+ revenue)

---

## Step 1: Set Up External Database (5 minutes)

### Option A: Neon Database (Recommended - Free)

1. **Go to [neon.tech](https://neon.tech)**
2. **Sign up** with GitHub or email
3. **Create New Project:**
   - Project Name: `ecommerce-ai-agent`
   - Region: Select closest to you
   - PostgreSQL Version: Keep default
4. **Copy Connection String:**
   - Go to Dashboard → Connection Details
   - Copy the connection string (starts with `postgresql://`)
   - Example: `postgresql://user:password@ep-cool-math-123456.us-east-2.aws.neon.tech/neondb`

### Option B: Supabase Database (Alternative - Free)

1. **Go to [supabase.com](https://supabase.com)**
2. **Create account** and new project
3. **Project settings → Database → Connection string**
4. **Copy the connection pooling URL**

---

## Step 2: Deploy on Vercel (10 minutes)

### 2.1 Create Vercel Account
1. **Go to [vercel.com](https://vercel.com)**
2. **Sign up with GitHub** (use same account as your repository)
3. **Verify your email** if prompted

### 2.2 Import Your Project
1. **Click "New Project"** on Vercel dashboard
2. **Import Git Repository:**
   - Search for: `E-commerce-ai-agent`
   - Select: `RuthvikAnupati/E-commerce-ai-agent`
   - Click **"Import"**

### 2.3 Configure Build Settings
**Framework Preset:** Other  
**Root Directory:** `./` (keep default)  
**Build Settings:**
- **Build Command:** (leave empty)
- **Output Directory:** (leave empty)  
- **Install Command:** (leave default)
- **Development Command:** (leave default)

*Vercel will automatically detect Python and use requirements.txt*

---

## Step 3: Configure Environment Variables (3 minutes)

In the Vercel deployment configuration, add these **Environment Variables:**

### Required Variables:
1. **GEMINI_API_KEY**
   - Value: Your Google Gemini API key (starts with `AIza...`)
   - Environment: Production, Preview, Development

2. **DATABASE_URL** 
   - Value: Your PostgreSQL connection string from Step 1
   - Environment: Production, Preview, Development

3. **SESSION_SECRET**
   - Value: Any random string (e.g., `my-ecommerce-secret-2025-xyz`)
   - Environment: Production, Preview, Development

### How to Add Variables:
- Either add them during initial deployment
- Or go to Project Settings → Environment Variables after deployment

---

## Step 4: Deploy & Test (5 minutes)

### 4.1 Deploy
1. **Click "Deploy"** - Vercel will:
   - Clone your GitHub repository
   - Install Python dependencies from requirements.txt
   - Build your Flask application
   - Deploy to global edge network

### 4.2 Monitor Build
Watch the build logs. You should see:
```
Building...
Installing Python dependencies
✅ Build completed successfully
```

### 4.3 Access Your App
1. **Your app will be live at:** `your-project-name.vercel.app`
2. **Click the domain** to open your AI agent
3. **First visit triggers data loading** - your 4,382+ records will be imported automatically

---

## Step 5: Test Your AI Agent (2 minutes)

### Test Questions:
Try asking these questions to verify everything works:

1. **"What is my total sales?"**
   - Should return sum of all revenue data

2. **"Which products are not eligible for ads?"**
   - Should show products with advertising restrictions

3. **"What's my return on ad spend (RoAS)?"**
   - Should calculate RoAS from ad sales vs ad spend

4. **"Show me top 5 products by ad sales"**
   - Should return ranked list of best performing products

---

## Step 6: Custom Domain (Optional - 5 minutes)

### If you own a domain:
1. **Vercel Dashboard → Your Project → Settings → Domains**
2. **Add your domain:** `yourbusiness.com`
3. **Configure DNS** as Vercel instructs:
   - Add CNAME record pointing to `cname.vercel-dns.com`
4. **SSL certificate** applied automatically
5. **Your AI agent accessible at your custom domain**

---

## Troubleshooting Common Issues

### Build Fails
**Problem:** "pip: command not found" or dependency errors  
**Solution:** 
- Ensure requirements.txt exists in root directory
- Check environment variables are set
- Verify Python runtime in runtime.txt

### Database Connection Error
**Problem:** "could not connect to server"  
**Solution:**
- Verify DATABASE_URL format
- Check database is running (Neon/Supabase)
- Ensure connection string includes password

### Gemini API Error
**Problem:** "API key invalid"  
**Solution:**
- Verify GEMINI_API_KEY in environment variables
- Check API key hasn't expired
- Ensure key has proper permissions

### Data Not Loading
**Problem:** Empty database on first visit  
**Solution:**
- Visit root URL `/` to trigger data import
- Check logs for CSV file access
- Verify attached_assets folder deployed

---

## Your Deployed Application Features

### What Users Can Do:
- **Ask natural language questions** about your e-commerce data
- **Get AI-powered insights** from real business metrics
- **Access via web browser** from anywhere globally
- **Query $1M+ in revenue data** with simple questions

### Technical Benefits:
- **Global CDN** - Fast loading worldwide
- **Auto-scaling** - Handles traffic spikes
- **SSL certificate** - Secure HTTPS
- **Serverless** - No server management
- **Real-time updates** - Changes deploy instantly

### Business Value:
- **Professional AI agent** showcasing your technical skills
- **Real data analysis** capabilities for e-commerce businesses  
- **Scalable architecture** ready for production use
- **Portfolio piece** demonstrating full-stack AI integration

---

## Final URLs & Access

After successful deployment:

- **Vercel URL:** `your-project-name.vercel.app`
- **GitHub Repo:** `https://github.com/RuthvikAnupati/E-commerce-ai-agent`
- **Custom Domain:** `yourbusiness.com` (if configured)

Your E-commerce AI Agent is now live and accessible worldwide with authentic business data!

## Support Resources

- **Vercel Documentation:** [vercel.com/docs](https://vercel.com/docs)
- **Neon Database Docs:** [neon.tech/docs](https://neon.tech/docs)
- **Gemini AI API:** [ai.google.dev](https://ai.google.dev)

---

**Total deployment time: ~25 minutes**  
**Result: Production-ready AI agent with real $1M+ e-commerce data**