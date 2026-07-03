# Installation & Setup Guide

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python**: Version 3.8 or higher
- **pip**: Python package installer
- **Git**: Version control system
- **Virtual Environment**: venv or conda
- **Docker** (Optional): For containerized deployment

### Verify Installation

```bash
python --version  # Should show Python 3.8+
pip --version     # Should show pip version
git --version     # Should show git version
```

---

## 🚀 Quick Start (5 Minutes)

### Option 1: Using Virtual Environment (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Train the model
python main.py

# 6. Launch dashboard
streamlit run app.py
```

### Option 2: Using Conda

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction

# 2. Create conda environment
conda create -n churn-pred python=3.9
conda activate churn-pred

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train the model
python main.py

# 5. Launch dashboard
streamlit run app.py
```

---

## 🔧 Detailed Installation Steps

### Step 1: System Setup

#### Windows

```bash
# Install Python from python.org
# Install Git from git-scm.com

# Verify installations
python --version
pip --version
git --version
```

#### Linux (Ubuntu/Debian)

```bash
# Update system
sudo apt update
sudo apt upgrade

# Install Python and pip
sudo apt install python3.9 python3-pip python3-venv

# Install Git
sudo apt install git

# Verify installations
python3 --version
pip3 --version
git --version
```

#### macOS

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.9

# Install Git
brew install git

# Verify installations
python3 --version
pip3 --version
git --version
```

### Step 2: Project Setup

```bash
# Clone repository
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction

# Check project structure
ls -la  # Linux/Mac
dir     # Windows
```

### Step 3: Virtual Environment Setup

#### Option A: venv (Standard)

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Verify activation (should show (venv) in prompt)
which python  # Linux/Mac
where python  # Windows
```

#### Option B: Conda

```bash
# Create environment
conda create -n churn-pred python=3.9 -y

# Activate
conda activate churn-pred

# Verify
conda info --envs
```

### Step 4: Install Dependencies

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt

# Verify installation
pip list
```

### Step 5: Verify Installation

```bash
# Test imports
python -c "import pandas; import sklearn; import xgboost; import streamlit; print('All imports successful!')"
```

---

## 📦 Package Installation Details

### Core ML Packages

```bash
# Data manipulation
pip install pandas==2.0.3
pip install numpy==1.24.3

# Machine Learning
pip install scikit-learn==1.3.0
pip install xgboost==1.7.6
pip install imbalanced-learn==0.11.0

# Visualization
pip install matplotlib==3.7.2
pip install seaborn==0.12.2
pip install plotly==5.15.0

# Web Application
pip install streamlit==1.25.0

# Utilities
pip install pyyaml==6.0.1
pip install joblib==1.3.1
```

---

## 🎯 Post-Installation Setup

### 1. Verify Dataset

```bash
# Check if dataset.csv exists
ls dataset.csv  # Linux/Mac
dir dataset.csv  # Windows

# If missing, download from source or use sample data
```

### 2. Create Required Directories

```bash
# These are created automatically, but you can create manually
mkdir -p artifacts logs notebooks
# Windows: md artifacts logs notebooks
```

### 3. Configuration Check

```bash
# Verify config file exists
cat config/config.yaml  # Linux/Mac
type config\config.yaml  # Windows
```

### 4. Test Run

```bash
# Quick test of the pipeline (without full training)
python -c "from src.logger import logging; logging.info('Setup successful!')"
```

---

## 🐳 Docker Setup

### Install Docker

#### Windows
Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop)

#### Linux
```bash
# Ubuntu
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker

# Verify
docker --version
```

#### macOS
Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop)

### Build and Run

```bash
# Build image
docker build -t churn-prediction .

# Run container
docker run -p 8501:8501 churn-prediction

# Access at http://localhost:8501
```

### Docker Compose (Advanced)

```bash
# Create docker-compose.yml first
docker-compose up -d

# Stop
docker-compose down
```

---

## 🔍 Troubleshooting

### Issue 1: Python Version Mismatch

**Error**: `Python 3.6 is not supported`

**Solution**:
```bash
# Install Python 3.8+
# Update virtual environment
python3.9 -m venv venv
```

### Issue 2: pip Install Fails

**Error**: `Could not find a version that satisfies the requirement`

**Solution**:
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Clear cache
pip cache purge

# Retry installation
pip install -r requirements.txt
```

### Issue 3: ModuleNotFoundError

**Error**: `ModuleNotFoundError: No module named 'src'`

**Solution**:
```bash
# Install package in editable mode
pip install -e .

# Or add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:${PWD}"  # Linux/Mac
set PYTHONPATH=%PYTHONPATH%;%CD%          # Windows
```

### Issue 4: Permission Denied

**Error**: `PermissionError: [Errno 13] Permission denied`

**Solution**:
```bash
# Linux/Mac
chmod +x main.py
# Or run with sudo if needed

# Windows: Run terminal as Administrator
```

### Issue 5: Port Already in Use

**Error**: `streamlit error: Port 8501 is already in use`

**Solution**:
```bash
# Use different port
streamlit run app.py --server.port 8502

# Or kill process using port 8501
# Linux/Mac
lsof -ti:8501 | xargs kill -9

# Windows
netstat -ano | findstr :8501
taskkill /PID <PID> /F
```

### Issue 6: Dataset Not Found

**Error**: `FileNotFoundError: [Errno 2] No such file or directory: 'dataset.csv'`

**Solution**:
```bash
# Ensure dataset.csv is in root directory
ls dataset.csv

# If missing, download or copy dataset
cp /path/to/your/dataset.csv .
```

### Issue 7: Memory Error During Training

**Error**: `MemoryError`

**Solution**:
```python
# Reduce GridSearchCV parameters in config.yaml
# Use fewer folds (cv=3 instead of cv=5)
# Reduce parameter grid size
```

---

## 🧪 Verification Tests

### Test 1: Import Check

```python
python -c "
from src.logger import logging
from src.exception import CustomException
from src.utils import load_config
print('✓ All core modules working')
"
```

### Test 2: Data Ingestion

```python
python -c "
from src.components.data_ingestion import DataIngestion
di = DataIngestion()
print('✓ Data Ingestion module ready')
"
```

### Test 3: Configuration

```python
python -c "
from src.utils import load_config
config = load_config()
print('✓ Configuration loaded successfully')
print(f'Models to train: {list(config['model_training']['models'].keys())}')
"
```

---

## 📊 Performance Optimization

### For Faster Training

1. **Reduce Grid Search Space**
   - Edit `config/config.yaml`
   - Reduce parameter options

2. **Use Fewer Folds**
   - Change `cv=5` to `cv=3` in config

3. **Limit Models**
   - Comment out models in `model_trainer.py`

### For Lower Memory Usage

1. **Use Smaller Dataset**
   - Sample the data before training

2. **Reduce Batch Size**
   - Process data in chunks

---

## 🔄 Update & Maintenance

### Update Dependencies

```bash
# Update all packages
pip install --upgrade -r requirements.txt

# Update specific package
pip install --upgrade pandas

# Check outdated packages
pip list --outdated
```

### Pull Latest Changes

```bash
# Fetch updates
git pull origin main

# Reinstall if requirements changed
pip install -r requirements.txt
```

---

## 📱 IDE Setup

### VS Code

1. Install Python extension
2. Select interpreter: `Ctrl+Shift+P` → "Python: Select Interpreter"
3. Choose your virtual environment
4. Install recommended extensions:
   - Python
   - Pylance
   - Jupyter
   - GitLens

### PyCharm

1. Open project
2. File → Settings → Project → Python Interpreter
3. Add interpreter → Existing environment
4. Select venv/bin/python

### Jupyter

```bash
# Install Jupyter
pip install jupyter

# Launch
jupyter notebook

# Access at http://localhost:8888
```

---

## 🎓 Next Steps

After successful installation:

1. ✅ **Read README.md**: Understand project structure
2. ✅ **Run main.py**: Train the model
3. ✅ **Launch app.py**: Explore dashboard
4. ✅ **Check TABLEAU_GUIDE.md**: Setup visualizations
5. ✅ **Review notebooks/**: Understand EDA

---

## 💬 Support

If you encounter issues:

1. Check [Issues](https://github.com/yourusername/customer-churn-prediction/issues)
2. Create new issue with:
   - Error message
   - Python version
   - OS details
   - Steps to reproduce

---

## 📚 Additional Resources

- [Python Documentation](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Docker Documentation](https://docs.docker.com/)

---

**Installation Guide Version**: 1.0  
**Last Updated**: 2024  
**Tested On**: Windows 10/11, Ubuntu 20.04+, macOS 11+

Happy Coding! 🚀
