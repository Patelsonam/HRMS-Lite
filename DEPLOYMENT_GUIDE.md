# HRMS Lite - Complete Deployment Guide

This guide will walk you through deploying your HRMS Lite application to production.

## 📋 Prerequisites

Before starting, ensure you have:
- Git installed
- GitHub account
- Railway account (for backend)
- Vercel account (for frontend)

## 🗂️ Step 1: Prepare Your Code

### 1.1 Create GitHub Repository

```bash
# Navigate to your project
cd hrms-lite

# Initialize git
git init

# Create .gitignore files (already included)
# Add all files
git add .

# Commit
git commit -m "Initial commit - HRMS Lite"

# Create repository on GitHub (via web interface)
# Then connect local repo to GitHub
git remote add origin https://github.com/yourusername/hrms-lite.git
git branch -M main
git push -u origin main
```

## 🚂 Step 2: Deploy Backend to Railway

### 2.1 Create Railway Account
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Authorize Railway to access your repositories

### 2.2 Deploy Backend

1. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `hrms-lite` repository
   - Railway will detect it's a Python project

2. **Configure Build Settings**
   - Railway should auto-detect Python
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

3. **Add PostgreSQL Database**
   - In your project dashboard, click "New"
   - Select "Database"
   - Choose "PostgreSQL"
   - Railway automatically creates the database and sets `DATABASE_URL`

4. **Get Your Backend URL**
   - Go to your backend service settings
   - Click "Settings" → "Networking"
   - Click "Generate Domain"
   - Copy the URL (e.g., `https://your-app.railway.app`)

### 2.3 Verify Backend Deployment

Open your backend URL in browser:
```
https://your-app.railway.app
```

You should see:
```json
{
  "message": "Welcome to HRMS Lite API",
  "version": "1.0.0",
  "status": "active"
}
```

Check API docs:
```
https://your-app.railway.app/docs
```

## ▲ Step 3: Deploy Frontend to Vercel

### 3.1 Create Vercel Account
1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub
3. Authorize Vercel

### 3.2 Deploy Frontend

**Option A: Via Vercel Dashboard (Recommended)**

1. Click "Add New Project"
2. Import your GitHub repository
3. Configure project:
   - Framework Preset: Vite
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`
   - Install Command: `npm install`

4. **Add Environment Variables**
   - Click "Environment Variables"
   - Add variable:
     - Name: `VITE_API_URL`
     - Value: `https://your-app.railway.app/api` (your Railway backend URL)

5. Click "Deploy"

**Option B: Via Vercel CLI**

```bash
# Install Vercel CLI
npm install -g vercel

# Navigate to frontend
cd frontend

# Login to Vercel
vercel login

# Deploy
vercel

# Follow prompts:
# - Link to existing project? No
# - What's your project name? hrms-lite-frontend
# - In which directory is your code? ./
# - Want to override settings? Yes
#   - Build Command: npm run build
#   - Output Directory: dist
#   - Development Command: npm run dev

# Set environment variable
vercel env add VITE_API_URL

# Paste your Railway backend URL + /api
# Example: https://your-app.railway.app/api

# Deploy to production
vercel --prod
```

### 3.3 Verify Frontend Deployment

Your frontend will be available at:
```
https://your-app.vercel.app
```

## ✅ Step 4: Verify Complete Deployment

### 4.1 Test Employee Management
1. Go to your Vercel URL
2. Click "Add Employee"
3. Fill in details:
   - Employee ID: EMP001
   - Name: John Doe
   - Email: john@example.com
   - Department: IT
4. Click "Add Employee"
5. Employee should appear in table

### 4.2 Test Attendance Management
1. Click "Attendance" in navigation
2. Click "Mark Attendance"
3. Select employee
4. Choose date and status
5. Click "Mark Attendance"
6. Record should appear in table

### 4.3 Test Error Handling
1. Try adding duplicate Employee ID
2. Should show error message
3. Try adding invalid email
4. Should show validation error

## 🔧 Step 5: Configure Production Settings

### 5.1 Update CORS in Backend

Edit `backend/app/main.py`:

```python
# Replace
allow_origins=["*"],

# With your actual frontend URL
allow_origins=[
    "https://your-app.vercel.app",
    "http://localhost:3000"  # Keep for local development
],
```

Commit and push:
```bash
git add .
git commit -m "Update CORS for production"
git push
```

Railway will automatically redeploy.

### 5.2 Enable Custom Domain (Optional)

**For Vercel:**
1. Go to Project Settings → Domains
2. Add your custom domain
3. Follow DNS configuration instructions

**For Railway:**
1. Go to Service Settings → Networking
2. Add custom domain
3. Configure DNS records

## 📊 Step 6: Monitor Your Application

### Railway Monitoring
- View logs: Project → Service → Logs
- Check metrics: CPU, Memory, Network usage
- Set up alerts for errors

### Vercel Monitoring
- Analytics: Project → Analytics
- Deployment logs: Deployments → View logs
- Performance insights available

## 🔒 Step 7: Security Checklist

- [ ] CORS configured with specific origins
- [ ] Environment variables set correctly
- [ ] No sensitive data in repository
- [ ] HTTPS enabled (automatic on Railway/Vercel)
- [ ] Database credentials secured
- [ ] API rate limiting configured (optional)

## 🐛 Troubleshooting Deployment

### Backend Issues

**Problem: Database connection failed**
```
Solution:
1. Check Railway logs
2. Verify DATABASE_URL is set
3. Ensure PostgreSQL service is running
```

**Problem: Import errors**
```
Solution:
1. Verify requirements.txt is complete
2. Check Python version compatibility
3. Rebuild deployment
```

### Frontend Issues

**Problem: API calls failing**
```
Solution:
1. Check VITE_API_URL environment variable
2. Verify backend is running
3. Check browser console for CORS errors
4. Ensure backend URL includes /api
```

**Problem: Environment variable not working**
```
Solution:
1. Redeploy after adding environment variables
2. Ensure variable name starts with VITE_
3. Check Vercel deployment logs
```

### Common Issues

**Problem: 500 errors on API calls**
```
Check Railway logs:
railway logs

Look for Python errors
```

**Problem: Blank page on frontend**
```
Check Vercel deployment logs
Verify build completed successfully
Check browser console for errors
```

## 🔄 Making Updates

### Update Backend
```bash
# Make changes to backend code
git add backend/
git commit -m "Update backend"
git push

# Railway auto-deploys on push to main
```

### Update Frontend
```bash
# Make changes to frontend code
git add frontend/
git commit -m "Update frontend"
git push

# Vercel auto-deploys on push to main
```

### Manual Redeploy

**Railway:**
- Go to deployment
- Click "Redeploy"

**Vercel:**
- Go to deployments
- Click "Redeploy"

## 📝 Post-Deployment Checklist

- [ ] Backend accessible at Railway URL
- [ ] Frontend accessible at Vercel URL
- [ ] API documentation available at /docs
- [ ] Can create employees
- [ ] Can delete employees
- [ ] Can mark attendance
- [ ] Can view attendance
- [ ] Error messages display correctly
- [ ] Responsive design works on mobile
- [ ] No console errors in browser

## 🎉 Success!

Your HRMS Lite application is now live!

**Share your URLs:**
- Frontend: `https://your-app.vercel.app`
- Backend API: `https://your-app.railway.app`
- API Docs: `https://your-app.railway.app/docs`

## 📞 Support

If you encounter issues:

1. Check deployment logs
2. Verify environment variables
3. Test locally first
4. Check Railway/Vercel status pages
5. Review error messages carefully

## 🔗 Useful Links

- [Railway Documentation](https://docs.railway.app)
- [Vercel Documentation](https://vercel.com/docs)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [Vite Deployment](https://vitejs.dev/guide/static-deploy.html)

---

Good luck with your deployment! 🚀
