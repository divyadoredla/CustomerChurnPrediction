# ⚡ Quick Fix Guide - Deployment Error

## Problem
```
❗️ installer returned a non-zero exit code
❗️ Error during processing dependencies!
```

## Quick Solution (30 seconds)

### Step 1: Verify Files
Check that these files exist:
- ✅ `requirements.txt` (simplified, no versions)
- ✅ `.streamlit/config.toml`
- ✅ `artifacts/` folder with models

### Step 2: Push to GitHub
```bash
git add .
git commit -m "Fix: Simplified requirements for deployment"
git push origin main
```

### Step 3: Redeploy
**On Streamlit Cloud:**
1. Go to your app
2. Click ⋮ (three dots)
3. Click "Reboot app"

**Done!** ✅

---

## If That Doesn't Work

### Try Option A: Use Locked Versions
```bash
# Windows
del requirements.txt
ren requirements_locked.txt requirements.txt

# Linux/Mac
rm requirements.txt
mv requirements_locked.txt requirements.txt

# Then push
git add requirements.txt
git commit -m "Use locked dependency versions"
git push origin main
```

### Try Option B: Local Test First
```bash
# Windows
install_dependencies.bat
streamlit run app.py

# Linux/Mac
pip install -r requirements.txt
streamlit run app.py
```

---

## Need More Help?

📚 **Full Documentation:**
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Detailed solutions
- [DEPLOYMENT.md](DEPLOYMENT.md) - Platform-specific guides
- [DEPLOYMENT_FIX.md](DEPLOYMENT_FIX.md) - Technical details

🔍 **Check Logs:**
- Streamlit Cloud: Settings → Logs
- Local: Terminal output

💬 **Get Support:**
- GitHub Issues: [Open an issue](https://github.com/divyadoredla/CustomerChurnPrediction/issues)
- Check existing solutions in docs

---

## What We Fixed

✅ Simplified `requirements.txt` (removed version constraints)
✅ Added `.streamlit/config.toml` for proper configuration
✅ Created backup `requirements_locked.txt`
✅ Added comprehensive troubleshooting guides
✅ Verified all imports work locally

**Your app should now deploy successfully!** 🎉
