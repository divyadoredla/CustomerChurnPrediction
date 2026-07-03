# 🚀 Deployment Guide

## Streamlit Cloud Deployment (Recommended)

### Prerequisites
- GitHub account
- Streamlit Cloud account (free at [share.streamlit.io](https://share.streamlit.io))
- Repository pushed to GitHub

### Step-by-Step Instructions

#### 1. Prepare Your Repository

Ensure these files are in your GitHub repository:
```
✅ requirements.txt (simplified, no version numbers)
✅ app.py
✅ artifacts/ (with trained models)
✅ src/ (all Python modules)
✅ config/config.yaml
✅ .streamlit/config.toml
```

#### 2. Push to GitHub

```bash
git add .
git commit -m "Prepare for Streamlit Cloud deployment"
git push origin main
```

#### 3. Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Select your repository: `divyadoredla/CustomerChurnPrediction`
4. Set main file path: `app.py`
5. Click "Deploy"

#### 4. Configuration

In Streamlit Cloud settings:
- **Python version:** 3.10 (recommended)
- **Main file:** `app.py`
- **Branch:** `main`

#### 5. Wait for Deployment

The app will:
1. Clone your repository
2. Install dependencies from `requirements.txt`
3. Start the Streamlit server
4. Provide a public URL

### Troubleshooting Streamlit Cloud

If deployment fails:

1. **Check Logs:** Click "Manage app" → "Logs"
2. **Reboot App:** Click three dots → "Reboot app"
3. **Clear Cache:** Delete and redeploy
4. **Verify Files:** Ensure all artifacts are committed

---

## Local Deployment

### Windows

```bash
# Clone repository
git clone https://github.com/divyadoredla/CustomerChurnPrediction.git
cd CustomerChurnPrediction

# Install dependencies
install_dependencies.bat

# Run app
streamlit run app.py
```

### Linux/Mac

```bash
# Clone repository
git clone https://github.com/divyadoredla/CustomerChurnPrediction.git
cd CustomerChurnPrediction

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

---

## Docker Deployment

### Build Image

```bash
docker build -t customer-churn-prediction .
```

### Run Container

```bash
# Basic run
docker run -p 8501:8501 customer-churn-prediction

# Run with name
docker run -d --name churn-app -p 8501:8501 customer-churn-prediction

# Run with volume mount (for persistence)
docker run -d \
  -p 8501:8501 \
  -v $(pwd)/artifacts:/app/artifacts \
  customer-churn-prediction
```

### Access Application

Open browser: http://localhost:8501

---

## Heroku Deployment

### 1. Create Required Files

**runtime.txt**
```
python-3.10.12
```

**Procfile**
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

**setup.sh**
```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

### 2. Deploy

```bash
# Login to Heroku
heroku login

# Create app
heroku create your-churn-app

# Deploy
git push heroku main

# Open app
heroku open
```

---

## AWS EC2 Deployment

### 1. Launch EC2 Instance

- **AMI:** Ubuntu 22.04 LTS
- **Instance Type:** t2.medium (minimum)
- **Security Group:** Allow port 8501

### 2. Connect and Setup

```bash
# SSH into instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python
sudo apt install python3-pip python3-venv -y

# Clone repository
git clone https://github.com/divyadoredla/CustomerChurnPrediction.git
cd CustomerChurnPrediction

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run with nohup (background)
nohup streamlit run app.py --server.port=8501 --server.address=0.0.0.0 &
```

### 3. Access

Open browser: http://your-ec2-ip:8501

---

## Azure Web App Deployment

### 1. Create Web App

```bash
# Login
az login

# Create resource group
az group create --name churn-rg --location eastus

# Create app service plan
az appservice plan create --name churn-plan --resource-group churn-rg --sku B1 --is-linux

# Create web app
az webapp create --name your-churn-app --resource-group churn-rg --plan churn-plan --runtime "PYTHON:3.10"
```

### 2. Deploy

```bash
# Deploy from GitHub
az webapp deployment source config --name your-churn-app --resource-group churn-rg \
  --repo-url https://github.com/divyadoredla/CustomerChurnPrediction \
  --branch main --manual-integration
```

---

## Google Cloud Run Deployment

### 1. Build and Push Image

```bash
# Set project
gcloud config set project your-project-id

# Build image
gcloud builds submit --tag gcr.io/your-project-id/churn-prediction

# Deploy
gcloud run deploy churn-prediction \
  --image gcr.io/your-project-id/churn-prediction \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

---

## Environment Variables (Optional)

If you need to set environment variables:

### Streamlit Cloud
Add in app settings under "Advanced settings" → "Secrets"

### Docker
```bash
docker run -e VAR_NAME=value -p 8501:8501 customer-churn-prediction
```

### Heroku
```bash
heroku config:set VAR_NAME=value
```

---

## Performance Optimization

### For Production Deployments

1. **Enable Caching:** Already implemented in code
2. **Use CDN:** For static assets
3. **Load Balancing:** For high traffic
4. **Database:** Store predictions in database instead of JSON

### Recommended Resources

| Platform | vCPU | RAM | Storage |
|----------|------|-----|---------|
| Streamlit Cloud | Free tier | Free tier | Free tier |
| Heroku | 1 dyno | 512 MB | Free |
| AWS EC2 | 2 vCPU | 4 GB | 20 GB |
| Azure | B1 | 1.75 GB | 10 GB |
| GCP Cloud Run | 1 vCPU | 512 MB | Auto |

---

## Monitoring

### Application Health

```bash
# Check if app is running
curl http://your-app-url/_stcore/health

# Monitor logs
streamlit logs  # Streamlit Cloud
heroku logs --tail  # Heroku
docker logs churn-app  # Docker
```

---

## Backup and Recovery

### Backup Artifacts

```bash
# Backup trained models
tar -czf artifacts-backup.tar.gz artifacts/

# Upload to cloud storage
# AWS S3
aws s3 cp artifacts-backup.tar.gz s3://your-bucket/

# Google Cloud Storage
gsutil cp artifacts-backup.tar.gz gs://your-bucket/
```

---

## SSL/HTTPS

- **Streamlit Cloud:** Automatically provided
- **Heroku:** Automatically provided
- **AWS/Azure/GCP:** Configure load balancer with SSL certificate

---

## Custom Domain

### Streamlit Cloud
Not supported on free tier

### Heroku
```bash
heroku domains:add www.yourapp.com
```

Then update DNS:
```
CNAME www.yourapp.com -> your-app.herokuapp.com
```

---

## Support

For deployment issues:
- Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- Review platform-specific logs
- Open GitHub issue with error details

---

## Quick Deployment Checklist

- [ ] Repository on GitHub
- [ ] `requirements.txt` present
- [ ] Trained models in `artifacts/`
- [ ] All source files pushed
- [ ] Python 3.8-3.11
- [ ] Platform account created
- [ ] Configuration files present
- [ ] Security groups configured (if cloud)
- [ ] Health check passing

---

**Recommended:** Start with Streamlit Cloud for easiest deployment!
