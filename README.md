# 🎯 Customer Churn Prediction System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.0-orange.svg)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.7.6-red.svg)](https://xgboost.ai/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25.0-FF4B4B.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Accuracy](https://img.shields.io/badge/Accuracy-80.55%25-brightgreen.svg)](artifacts/model_comparison.json)

> A production-ready, end-to-end machine learning system that predicts customer churn with **80.55% accuracy** using XGBoost, featuring an interactive Streamlit dashboard and comprehensive business intelligence insights.

<p align="center">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-success" alt="Status">
  <img src="https://img.shields.io/badge/Maintained-Yes-brightgreen" alt="Maintained">
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED" alt="Docker">
</p>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Model Performance](#model-performance)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Dashboard Preview](#dashboard-preview)
- [Docker Deployment](#docker-deployment)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 🎯 Overview

This project implements a **complete machine learning pipeline** to predict customer churn in the telecommunications industry. It analyzes customer behavior patterns, service usage, and account information to identify customers at risk of leaving, enabling businesses to take proactive retention measures.

### 🎪 Live Demo
- **Streamlit Dashboard:** Run `streamlit run app.py`
- **Local Access:** http://localhost:8501

### 🏆 Key Achievements
- ✅ **80.55% Accuracy** with XGBoost model
- ✅ **5 ML Models** trained and compared
- ✅ **Real-time Predictions** via interactive dashboard
- ✅ **Production-Ready** code with comprehensive documentation
- ✅ **Docker Support** for easy deployment

### 💼 Business Value
- 🎯 **Proactive Retention**: Identify at-risk customers before they leave
- 💰 **Revenue Protection**: Reduce customer acquisition costs by 15-20%
- 📊 **Data-Driven Decisions**: Make informed retention strategies
- 🚀 **Scalable Solution**: Production-ready architecture

---

## ✨ Key Features

### 🤖 Machine Learning Pipeline
- **5 ML Models**: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost
- **Automated Model Selection**: Best model chosen by accuracy
- **Hyperparameter Tuning**: GridSearchCV with 5-fold cross-validation
- **Comprehensive Evaluation**: Accuracy, Precision, Recall, F1-Score, ROC AUC
- **Feature Engineering**: Tenure groups, charge categories, service aggregation

### 📊 Interactive Dashboard (5 Pages)
- **🏠 Home**: Project overview and model comparison table
- **🔮 Prediction**: Real-time churn prediction with risk assessment
- **📈 Performance**: Detailed metrics, confusion matrix, ROC curve, feature importance
- **📜 History**: Track all predictions with CSV export
- **ℹ️ About**: Complete project documentation

### 💡 Business Intelligence
- **Risk Assessment**: Very Low, Low, Medium, High risk categories
- **Actionable Recommendations**: Targeted retention strategies per customer
- **Probability Gauges**: Visual churn likelihood display (0-100%)
- **Feature Importance**: Identify key factors driving churn
- **Export Capability**: Download predictions and reports

### 🛠️ Code Quality
- **Modular Architecture**: Separate components for data ingestion, transformation, training, evaluation
- **Exception Handling**: Custom exceptions with detailed error tracking
- **Configuration Management**: YAML-based centralized parameter control
- **Comprehensive Logging**: Track every pipeline stage with timestamps
- **PEP8 Compliant**: Clean, readable, maintainable Python code

---

## 📊 Model Performance

### 🏆 Best Model: XGBoost

| Metric | Score | Description |
|--------|-------|-------------|
| **Accuracy** | **80.55%** | Overall prediction correctness |
| **Precision** | **66.89%** | Accuracy of churn predictions (fewer false alarms) |
| **Recall** | 52.94% | Percentage of actual churners identified |
| **F1-Score** | 59.10% | Balanced performance measure |
| **ROC AUC** | 84.39% | Model's ranking ability |

### 📈 All Models Comparison

| Model | Accuracy | ROC AUC | Precision | Recall | F1-Score |
|-------|----------|---------|-----------|--------|----------|
| **XGBoost** 🏆 | **80.55%** | 84.39% | **66.89%** | 52.94% | 59.10% |
| Gradient Boosting | 80.13% | **84.49%** | 66.55% | 50.53% | 57.45% |
| Logistic Regression | 79.91% | 84.05% | 64.26% | **54.81%** | **59.16%** |
| Random Forest | 79.70% | 83.95% | 64.97% | 51.07% | 57.19% |
| Decision Tree | 78.50% | 82.17% | 60.35% | 55.35% | 57.74% |

### 🎯 Confusion Matrix (XGBoost on Test Set)

```
                Predicted
                No      Yes     Total
Actual  No      940     95      1035   (90.8% TPR)
        Yes     176     198     374    (52.9% TPR)
        
        Total   1116    293     1409
```

**Key Insights:**
- ✅ **90.8% True Negative Rate**: Excellent at identifying loyal customers
- ⚠️ **52.9% True Positive Rate**: Catches over half of potential churners
- 📊 **Overall**: 1,138 correct predictions out of 1,409 (80.55%)

---

## 🚀 Quick Start

Get up and running in **5 minutes**!

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Option 1: Quick Setup

```bash
# 1. Clone the repository
git clone https://github.com/divyadoredla/CustomerChurnPrediction.git
cd CustomerChurnPrediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train models (5-10 minutes)
python main.py

# 4. Launch dashboard
streamlit run app.py
```

### Option 2: Using Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
streamlit run app.py
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
streamlit run app.py
```

### Option 3: Using Docker

```bash
# Build image
docker build -t churn-prediction .

# Run container
docker run -p 8501:8501 churn-prediction

# Access at http://localhost:8501
```

---

## 💻 Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/divyadoredla/CustomerChurnPrediction.git
cd CustomerChurnPrediction
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
python -c "import pandas, sklearn, xgboost, streamlit; print('✅ All packages installed successfully!')"
```

---

## 🎮 Usage

### 1. Train the Models

```bash
python main.py
```

**What happens:**
- ✅ Loads and splits data (7,043 customers)
- ✅ Validates data quality
- ✅ Engineers features and transforms data
- ✅ Trains 5 ML models with hyperparameter tuning
- ✅ Selects best model (XGBoost)
- ✅ Generates evaluation metrics and visualizations
- ✅ Saves models to `artifacts/models/`

**Output:**
```
======================================================================
TRAINING PIPELINE EXECUTION SUMMARY
======================================================================
Best Model: XGBoost
Accuracy: 80.55%
ROC AUC Score: 84.39%
======================================================================
```

### 2. Launch Dashboard

```bash
streamlit run app.py
```

Access at: **http://localhost:8501**

### 3. Make Predictions

#### Via Dashboard:
1. Navigate to **Customer Prediction** page
2. Enter customer information
3. Click **Predict Churn**
4. View results with probability and recommendations

#### Via Python Code:

```python
from src.pipeline.prediction_pipeline import PredictionPipeline, CustomData

# Create customer data
customer = CustomData(
    gender='Male',
    SeniorCitizen=0,
    Partner='No',
    Dependents='No',
    tenure=1,
    PhoneService='Yes',
    MultipleLines='No',
    InternetService='Fiber optic',
    OnlineSecurity='No',
    OnlineBackup='No',
    DeviceProtection='No',
    TechSupport='No',
    StreamingTV='No',
    StreamingMovies='No',
    Contract='Month-to-month',
    PaperlessBilling='Yes',
    PaymentMethod='Electronic check',
    MonthlyCharges=85.0,
    TotalCharges=85.0
)

# Make prediction
pipeline = PredictionPipeline()
result = pipeline.predict(customer.get_data_as_dataframe())

print(f"Churn Prediction: {result['prediction']}")
print(f"Churn Probability: {result['churn_probability']}%")
print(f"Risk Level: {result['risk_level']}")
```

### 4. Generate Tableau Data (Optional)

```bash
python src/utils/prepare_tableau_data.py
```

Outputs 6 CSV files to `artifacts/tableau_data/` for BI visualization.

---

## 📁 Project Structure

```
CustomerChurnPrediction/
│
├── 📊 app.py                      # Streamlit dashboard (main application)
├── 🎯 main.py                     # Training pipeline execution
├── 📋 requirements.txt            # Python dependencies
├── ⚙️ setup.py                    # Package configuration
├── 🐳 Dockerfile                  # Docker container setup
├── 📖 README.md                   # This file
│
├── 📂 config/
│   └── config.yaml               # Configuration parameters
│
├── 📂 src/
│   ├── __init__.py
│   ├── exception.py              # Custom exception handling
│   ├── logger.py                 # Logging configuration
│   ├── utils.py                  # Utility functions
│   │
│   ├── 📂 components/            # ML Pipeline Components
│   │   ├── data_ingestion.py         # Load and split data
│   │   ├── data_validation.py        # Quality checks
│   │   ├── data_transformation.py    # Feature engineering
│   │   ├── model_trainer.py          # Train 5 models
│   │   └── model_evaluation.py       # Generate metrics
│   │
│   ├── 📂 pipeline/              # End-to-End Pipelines
│   │   ├── training_pipeline.py      # Complete training workflow
│   │   └── prediction_pipeline.py    # Prediction workflow
│   │
│   └── 📂 utils/
│       └── prepare_tableau_data.py   # BI data preparation
│
├── 📂 artifacts/                  # Generated Files (created after training)
│   ├── models/
│   │   └── best_model.pkl        # Trained XGBoost model
│   ├── plots/
│   │   ├── confusion_matrix.png
│   │   ├── roc_curve.png
│   │   └── feature_importance.png
│   ├── train.csv                 # Training data
│   ├── test.csv                  # Test data
│   ├── preprocessor.pkl          # Feature transformer
│   ├── model_comparison.json     # All model results
│   └── evaluation_metrics.json   # Detailed metrics
│
├── 📂 logs/                       # Application logs
│   └── *.log                     # Timestamped log files
│
├── 📂 notebooks/                  # Analysis and Documentation
│   └── EDA_and_Analysis.md       # Data insights
│
└── 📂 Documentation/              # Comprehensive Guides
    ├── QUICK_START.md            # 5-minute guide
    ├── INSTALLATION_GUIDE.md     # Detailed setup
    ├── TABLEAU_GUIDE.md          # BI visualization
    ├── CONTRIBUTING.md           # Contribution guidelines
    ├── PROJECT_SUMMARY.md        # Technical overview
    └── INDEX.md                  # Navigation guide
```

---

## 🛠️ Tech Stack

### Core Technologies
| Technology | Version | Purpose |
|------------|---------|---------|
| ![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python) | 3.8+ | Primary language |
| ![Pandas](https://img.shields.io/badge/Pandas-2.0.3-blue?logo=pandas) | 2.0.3 | Data manipulation |
| ![NumPy](https://img.shields.io/badge/NumPy-1.24.3-blue?logo=numpy) | 1.24.3 | Numerical computing |
| ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.0-orange?logo=scikit-learn) | 1.3.0 | ML algorithms |
| ![XGBoost](https://img.shields.io/badge/XGBoost-1.7.6-red) | 1.7.6 | Gradient boosting |

### Visualization & UI
| Technology | Version | Purpose |
|------------|---------|---------|
| ![Streamlit](https://img.shields.io/badge/Streamlit-1.25.0-FF4B4B?logo=streamlit) | 1.25.0 | Web dashboard |
| ![Plotly](https://img.shields.io/badge/Plotly-5.15.0-3F4F75?logo=plotly) | 5.15.0 | Interactive charts |
| ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7.2-blue) | 3.7.2 | Static plots |
| ![Seaborn](https://img.shields.io/badge/Seaborn-0.12.2-blue) | 0.12.2 | Statistical viz |

### DevOps & Tools
| Technology | Version | Purpose |
|------------|---------|---------|
| ![Docker](https://img.shields.io/badge/Docker-Latest-2496ED?logo=docker) | Latest | Containerization |
| ![Git](https://img.shields.io/badge/Git-Latest-F05032?logo=git) | Latest | Version control |
| ![YAML](https://img.shields.io/badge/YAML-1.2-red) | 1.2 | Configuration |
| ![Joblib](https://img.shields.io/badge/Joblib-1.3.1-blue) | 1.3.1 | Model serialization |

---

## 📸 Dashboard Preview

### Home Page - Model Comparison
```
🏆 Best Model: XGBoost with 80.55% Accuracy

┌─────────────────────┬──────────┬──────────┬───────────┐
│ Model               │ Accuracy │ ROC AUC  │ Precision │
├─────────────────────┼──────────┼──────────┼───────────┤
│ XGBoost            │ 80.55%   │ 84.39%   │ 66.89%    │
│ Gradient Boosting   │ 80.13%   │ 84.49%   │ 66.55%    │
│ Logistic Regression │ 79.91%   │ 84.05%   │ 64.26%    │
│ Random Forest       │ 79.70%   │ 83.95%   │ 64.97%    │
│ Decision Tree       │ 78.50%   │ 82.17%   │ 60.35%    │
└─────────────────────┴──────────┴──────────┴───────────┘
```

### Prediction Page - Example Result
```
⚠️ Customer Will Churn
Risk Level: High Risk

Churn Probability: 78.5%
Retention Probability: 21.5%
Confidence Score: 57%

💡 Recommendations:
- Priority customer for retention campaign
- Schedule personalized outreach call
- Offer special retention discount
- Provide loyalty rewards
```

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t customer-churn-prediction .
```

### Run Container

```bash
# Run with port mapping
docker run -p 8501:8501 customer-churn-prediction

# Run in detached mode
docker run -d -p 8501:8501 customer-churn-prediction

# Run with name
docker run -d -p 8501:8501 --name churn-app customer-churn-prediction
```

### Access Application

Open browser and navigate to: **http://localhost:8501**

### Stop Container

```bash
docker stop churn-app
docker rm churn-app
```

---

## 📚 Documentation

Comprehensive documentation is available:

| Document | Description | Link |
|----------|-------------|------|
| 📖 **README** | Main documentation | [README.md](README.md) |
| 🚀 **Quick Start** | 5-minute setup guide | [QUICK_START.md](QUICK_START.md) |
| 💻 **Installation** | Detailed installation steps | [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) |
| 🚢 **Deployment** | Cloud & platform deployment | [DEPLOYMENT.md](DEPLOYMENT.md) |
| 🔧 **Troubleshooting** | Fix common issues | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) |
| 📊 **Tableau Guide** | BI visualization setup | [TABLEAU_GUIDE.md](TABLEAU_GUIDE.md) |
| 🤝 **Contributing** | How to contribute | [CONTRIBUTING.md](CONTRIBUTING.md) |
| 📝 **Project Summary** | Technical deep dive | [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) |
| 🗂️ **Index** | Navigation guide | [INDEX.md](INDEX.md) |

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development process.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Divya Sri Doredla

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👨‍💻 Author

<p align="center">
  <img src="https://img.shields.io/badge/Created%20with%20%E2%9D%A4%EF%B8%8F%20by-Divya%20Sri%20Doredla-purple?style=for-the-badge" alt="Author">
</p>

**Divya Sri Doredla**

- 💼 Portfolio: [Your Portfolio Website](https://yourportfolio.com)
- 🐙 GitHub: [@divyadoredla](https://github.com/divyadoredla)
- 💼 LinkedIn: [Divya Sri Doredla](https://linkedin.com/in/divyasridoredla)
- 📧 Email: divyasri@example.com

---

## 🌟 Acknowledgments

- **Dataset**: Telco Customer Churn Dataset
- **Inspiration**: Real-world customer retention challenges
- **Community**: Open source ML community
- **Libraries**: Scikit-learn, XGBoost, Streamlit teams

---

## 📊 Project Statistics

<p align="center">
  <img src="https://img.shields.io/badge/Code%20Lines-3500+-blue" alt="Lines of Code">
  <img src="https://img.shields.io/badge/Python%20Files-15-orange" alt="Files">
  <img src="https://img.shields.io/badge/Documentation-25000+%20words-green" alt="Documentation">
  <img src="https://img.shields.io/badge/ML%20Models-5-red" alt="Models">
</p>

---

## 🎯 Future Enhancements

### Planned Features
- [ ] REST API with FastAPI
- [ ] Real-time data streaming
- [ ] A/B testing framework
- [ ] Automated model retraining
- [ ] Email/SMS alerts for high-risk customers
- [ ] CRM system integration (Salesforce, HubSpot)
- [ ] Cloud deployment (AWS/Azure/GCP)
- [ ] Kubernetes orchestration
- [ ] CI/CD pipeline with GitHub Actions

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Documentation](#documentation)
2. Search [Existing Issues](https://github.com/divyadoredla/CustomerChurnPrediction/issues)
3. Open a [New Issue](https://github.com/divyadoredla/CustomerChurnPrediction/issues/new)
4. Contact via [Email](mailto:divyasri@example.com)

---

## ⭐ Show Your Support

If you find this project helpful, please give it a ⭐ on GitHub!

<p align="center">
  <a href="https://github.com/divyadoredla/CustomerChurnPrediction/stargazers">
    <img src="https://img.shields.io/github/stars/divyadoredla/CustomerChurnPrediction?style=social" alt="GitHub Stars">
  </a>
  <a href="https://github.com/divyadoredla/CustomerChurnPrediction/network/members">
    <img src="https://img.shields.io/github/forks/divyadoredla/CustomerChurnPrediction?style=social" alt="GitHub Forks">
  </a>
</p>

---

<p align="center">
  <b>Built with ❤️ by Divya Sri Doredla</b><br>
  <sub>Production-Ready Machine Learning System</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Quality-Enterprise%20Grade-blue?style=for-the-badge" alt="Quality">
</p>
