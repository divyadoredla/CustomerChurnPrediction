# 🔧 Troubleshooting Guide

## Dependency Installation Errors

### Error: "installer returned a non-zero exit code"

This error typically occurs when deploying to Streamlit Cloud or other platforms. Here are solutions:

### Solution 1: Use Simple Requirements (Recommended)

The `requirements.txt` file now uses package names without version constraints:
```
pandas
numpy
scikit-learn
xgboost
matplotlib
seaborn
plotly
streamlit
pyyaml
joblib
imbalanced-learn
```

This allows the platform to install the latest compatible versions.

### Solution 2: Use Locked Versions

If Solution 1 fails, rename `requirements_locked.txt` to `requirements.txt`:

**Windows:**
```bash
del requirements.txt
ren requirements_locked.txt requirements.txt
```

**Linux/Mac:**
```bash
rm requirements.txt
mv requirements_locked.txt requirements.txt
```

### Solution 3: Check Python Version

Ensure you're using Python 3.8-3.11. Check with:
```bash
python --version
```

For Streamlit Cloud, create a file named `.streamlit/config.toml` (already created).

### Solution 4: Clear Cache (Streamlit Cloud)

If deploying to Streamlit Cloud:
1. Go to your app dashboard
2. Click the three dots menu
3. Select "Reboot app"
4. Or delete and redeploy the app

### Solution 5: Install Dependencies Locally

**Windows:**
```bash
# Run the automated script
install_dependencies.bat

# Or manually
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Linux/Mac:**
```bash
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
```

## Common Issues

### Issue: "No module named 'sklearn'"

**Solution:**
```bash
pip install scikit-learn
```

### Issue: "XGBoost installation failed"

**Solution:**
```bash
# For Windows
pip install xgboost

# For Mac with Apple Silicon
pip install xgboost --no-binary :all:

# For Linux
pip install xgboost
```

### Issue: "Streamlit won't start"

**Solution:**
```bash
# Kill existing Streamlit processes
taskkill /F /IM streamlit.exe /T  # Windows
pkill -f streamlit                 # Linux/Mac

# Start fresh
streamlit run app.py
```

### Issue: "Module 'numpy' has no attribute 'X'"

This indicates version conflicts.

**Solution:**
```bash
pip uninstall numpy pandas scikit-learn -y
pip install numpy==1.24.3 pandas==2.0.3 scikit-learn==1.3.0
```

## Platform-Specific Instructions

### Streamlit Cloud Deployment

1. Ensure `requirements.txt` is in the root directory
2. Ensure `.streamlit/config.toml` exists (already created)
3. Make sure your GitHub repository is up to date
4. In Streamlit Cloud settings:
   - Main file path: `app.py`
   - Python version: 3.10 (recommended)

### Heroku Deployment

Create `runtime.txt`:
```
python-3.10.12
```

Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT
```

### Docker Deployment

The included `Dockerfile` should work. Build with:
```bash
docker build -t churn-prediction .
docker run -p 8501:8501 churn-prediction
```

## Verification

After installation, verify with:

```bash
python -c "import pandas, numpy, sklearn, xgboost, streamlit; print('✅ Success!')"
```

## Getting Help

If issues persist:

1. Check the [GitHub Issues](https://github.com/divyadoredla/CustomerChurnPrediction/issues)
2. Review Streamlit Cloud logs (Settings → Logs)
3. Ensure all required files are present:
   - `requirements.txt`
   - `app.py`
   - `artifacts/` directory with trained models
   - `src/` directory with all modules

## Quick Fix Checklist

- [ ] Using Python 3.8-3.11
- [ ] `requirements.txt` is in root directory
- [ ] All files pushed to GitHub
- [ ] No syntax errors in Python files
- [ ] Models are trained (`artifacts/models/best_model.pkl` exists)
- [ ] Dependencies listed without conflicts

## Contact

If you still encounter issues, please open an issue on GitHub with:
- Error message (full traceback)
- Python version
- Operating system
- Deployment platform (local, Streamlit Cloud, etc.)

---

**Note:** The simplified `requirements.txt` (without version numbers) should resolve most deployment issues on Streamlit Cloud.
