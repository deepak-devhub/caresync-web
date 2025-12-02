# Vercel Deployment Guide - PostgreSQL Only

## ✅ Configuration Complete

Your Healthify application is now **PostgreSQL-only** and ready for Vercel deployment.

### What Was Changed:
- ✅ Removed all SQLite references
- ✅ Removed all MySQL compatibility code
- ✅ PostgreSQL only configuration in settings.py
- ✅ Deleted db.sqlite3 and db.sqlite3-journal
- ✅ Simplified .env.example for PostgreSQL

---

## 🔧 Pre-Deployment Checklist

- [ ] DATABASE_URL environment variable set in Vercel
- [ ] DEBUG = False in Vercel
- [ ] SECRET_KEY generated and set in Vercel
- [ ] ALLOWED_HOSTS includes yourdomain.vercel.app
- [ ] requirements.txt has psycopg2-binary
- [ ] No .env file committed to git

---

## 📋 Step 1: Get Supabase Connection String

1. Go to https://supabase.com/dashboard
2. Select your project
3. Click **Settings** → **Database**
4. Copy connection string (PostgreSQL tab)

Example format:
```
postgresql://postgres:password@db.xxxxxxxxxxxxx.supabase.co:5432/postgres
```

---

## 🚀 Step 2: Deploy to Vercel

### Option A: GitHub Integration (Recommended)

1. Push to GitHub:
```bash
git add .
git commit -m "PostgreSQL-only configuration for Vercel"
git push origin main
```

2. Go to https://vercel.com/new
3. Select your GitHub repository
4. Click **Deploy**

### Option B: Vercel CLI

```bash
npm install -g vercel
vercel
```

---

## ⚙️ Step 3: Set Environment Variables in Vercel

After deployment starts, go to **Settings** → **Environment Variables**:

| Name | Value |
|------|-------|
| DATABASE_URL | postgresql://postgres:password@db.xxxxxxxxxxxxx.supabase.co:5432/postgres |
| DEBUG | False |
| SECRET_KEY | (generate new: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())") |
| ALLOWED_HOSTS | yourdomain.vercel.app |

---

## 🗄️ Step 4: Run Migrations on Vercel

After deployment completes:

### Using Vercel CLI:
```bash
vercel env pull
python manage.py migrate
python manage.py createsuperuser
```

### Or manually:
1. SSH into Vercel environment
2. Run: `python manage.py migrate`
3. Run: `python manage.py createsuperuser`

---

## ✅ Step 5: Verify Deployment

Test these on your live URL:

1. **Admin Panel**: https://yourdomain.vercel.app/admin/
2. **Login Page**: https://yourdomain.vercel.app/
3. **Database**: Tables should be created
4. **File Uploads**: Should work
5. **Static Files**: CSS/JS should load

---

## 🐛 Troubleshooting

### Error: "could not connect to server"

**Causes:**
- DATABASE_URL not set in Vercel
- Wrong DATABASE_URL format
- Supabase database not running

**Solution:**
1. Verify DATABASE_URL in Vercel settings
2. Check format: `postgresql://user:pass@host:5432/db`
3. Test connection locally first

### Error: "no such table"

**Cause:** Migrations not run on Vercel

**Solution:**
```bash
vercel env pull
python manage.py migrate
```

### Error: "ALLOWED_HOSTS validation"

**Cause:** Your domain not in ALLOWED_HOSTS

**Solution:**
Add to Vercel environment variable:
```
ALLOWED_HOSTS = yourdomain.vercel.app
```

### Error: "SECRET_KEY not set"

**Solution:**
Generate and add to Vercel:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 📊 Current Configuration

### Settings.py Database:
```python
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}
```

### Requirements.txt:
```
Django==3.2.25
psycopg2-binary==2.9.9
dj-database-url==2.1.0
gunicorn==21.2.0
whitenoise==6.6.0
... (other packages)
```

### Environment Variables Needed:
```
DATABASE_URL=postgresql://...
DEBUG=False
SECRET_KEY=...
ALLOWED_HOSTS=...
```

---

## 🔄 Local Testing (Before Deployment)

### 1. Create .env file:
```bash
cp .env.example .env
```

### 2. Edit .env with your Supabase details:
```
DATABASE_URL=postgresql://postgres:yourpassword@db.xxxxx.supabase.co:5432/postgres
DEBUG=True
SECRET_KEY=your-secret-key
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Test migrations:
```bash
python manage.py migrate
```

### 5. Run locally:
```bash
python manage.py runserver
```

### 6. Create superuser:
```bash
python manage.py createsuperuser
```

### 7. Test in browser:
- Admin: http://localhost:8000/admin
- App: http://localhost:8000

---

## 📝 Deployment Checklist

- [ ] requirements.txt updated
- [ ] settings.py PostgreSQL-only
- [ ] .env.example updated
- [ ] LOCAL TESTING PASSED
- [ ] Code pushed to GitHub
- [ ] Vercel project created
- [ ] Environment variables set
- [ ] Build completed successfully
- [ ] Migrations ran on Vercel
- [ ] Admin accessible
- [ ] All features tested
- [ ] No SQLite/MySQL code remains

---

## 🎉 Success!

If you can:
1. Access admin panel
2. Login/logout works
3. See database tables
4. Upload files

**Then your deployment is successful!**

---

## 📞 Support

- Supabase: https://supabase.com/docs
- Vercel: https://vercel.com/docs
- Django: https://docs.djangoproject.com
- PostgreSQL: https://www.postgresql.org/docs/

---

**Status**: ✅ READY FOR VERCEL DEPLOYMENT
**Database**: PostgreSQL Only
**Configuration**: Production Ready
