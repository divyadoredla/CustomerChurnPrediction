# 🎯 Customer Churn Prediction & Business Intelligence Dashboard

A production-ready end-to-end machine learning project that predicts customer churn using advanced ML algorithms and provides actionable business intelligence insights through interactive dashboards.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.0-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Architecture](#project-architecture)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [ML Pipeline](#ml-pipeline)
- [Model Performance](#model-performance)
- [Streamlit Dashboard](#streamlit-dashboard)
- [Tableau Dashboard](#tableau-dashboard)
- [Docker Deployment](#docker-deployment)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

Customer churn is a critical business metric that directly impacts revenue and growth. This project leverages machine learning to:

- **Predict** which customers are likely to churn
- **Identify** key factors influencing churn
- **Provide** actionable insights for retention strategies
- **Deliver** real-time predictions through a web interface

### Business Value

- 🎯 **Proactive Retention**: Identify at-risk customers before they leave
- 💰 **Revenue Protection**: Reduce customer acquisition costs
- 📊 **Data-Driven Decisions**: Make informed business strategies
- 🚀 **Scalable Solution**: Production-ready architecture

---

## ✨ Features

### Machine Learning Pipeline
- ✅ Automated data ingestion and preprocessing
- ✅ Comprehensive data validation
- ✅ Advanced feature engineering
- ✅ Multiple ML model training and comparison
- ✅ Hyperparameter tuning with GridSearchCV
- ✅ Automated best model selection
- ✅ Detailed model evaluation and metrics

### Web Application
- ✅ Interactive Streamlit dashboard
- ✅ Real-time churn predictions
- ✅ Customer risk level assessment
- ✅ Probability visualization with gauges
- ✅ Prediction history tracking
- ✅ Business recommendations
- ✅ Model performance metrics
- ✅ Export capabilities

### Code Quality
- ✅ Modular and reusable components
- ✅ Comprehensive logging
- ✅ Custom exception handling
- ✅ Configuration-driven architecture
- ✅ PEP8 compliant code
- ✅ Production-ready structure

---

## 🏗️ Project Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     RAW DATA (CSV)                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│               DATA INGESTION                                 │
│  • Load dataset                                              │
│  • Train-test split (stratified)                             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│               DATA VALIDATION                                │
│  • Schema validation                                         │
│  • Missing value check                                       │
│  • Duplicate detection                                       │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│               DATA TRANSFORMATION                            │
│  • Feature engineering                                       │
│  • Label encoding                                            │
│  • Feature scaling                                           │
│  • Save preprocessor                                         │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│               MODEL TRAINING                                 │
│  • Logistic Regression                                       │
│  • Decision Tree                                             │
│  • Random Forest                                             │
│  • Gradient Boosting                                         │
│  • XGBoost                                                   │
│  • GridSearchCV tuning                                       │
│  • Best model selection                                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│               MODEL EVALUATION                               │
│  • Metrics calculation                                       │
│  • Confusion matrix                                          │
│  • ROC curve                                                 │
│  • Feature importance                                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│               PREDICTION PIPELINE                            │
│  • Load model & preprocessor                                 │
│  • Transform new data                                        │
│  • Generate predictions                                      │
│  • Calculate confidence                                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│          STREAMLIT WEB APPLICATION                           │
│  • Interactive UI                                            │
│  • Real-time predictions                                     │
│  • Visualizations                                            │
│  • Recommendations                                           │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.8+**: Primary programming language
- **Pandas & NumPy**: Data manipulation and numerical computing
- **Scikit-learn**: Machine learning algorithms and preprocessing
- **XGBoost**: Gradient boosting framework

### Visualization
- **Matplotlib & Seaborn**: Statistical visualizations
- **Plotly**: Interactive charts and graphs
- **Streamlit**: Web application framework

### DevOps & Tools
- **Docker**: Containerization
- **Git**: Version control
- **YAML**: Configuration management
- **Joblib**: Model serialization

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction
```

2. **Create virtual environment**
```bash
python -m venv venv
```

3. **Activate virtual environment**

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Train the Model

Run the complete training pipeline:

```bash
python main.py
```

This will:
- Ingest and split the data
- Validate data quality
- Transform and engineer features
- Train multiple ML models
- Select the best model
- Generate evaluation metrics

Output artifacts will be saved in `artifacts/` directory.

### 2. Launch Streamlit Dashboard

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### 3. Make Predictions

Navigate through the dashboard:
- **Home**: Overview and statistics
- **Customer Prediction**: Enter customer data for real-time predictions
- **Model Performance**: View detailed metrics and visualizations
- **Prediction History**: Track all predictions
- **About Project**: Project documentation

---

## 📁 Project Structure

```
Customer-Churn-Prediction/
│
├── artifacts/                      # Generated artifacts
│   ├── models/                    # Saved models
│   ├── plots/                     # Visualization plots
│   ├── train.csv                  # Training data
│   ├── test.csv                   # Test data
│   ├── preprocessor.pkl           # Fitted preprocessor
│   ├── model_comparison.json      # Model comparison results
│   └── evaluation_metrics.json    # Evaluation metrics
│
├── config/
│   └── config.yaml               # Configuration parameters
│
├── logs/                         # Application logs
│   └── *.log
│
├── notebooks/                    # Jupyter notebooks (optional)
│   └── EDA.ipynb
│
├── src/
│   ├── __init__.py
│   ├── exception.py             # Custom exception handling
│   ├── logger.py                # Logging configuration
│   ├── utils.py                 # Utility functions
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py         # Data loading and splitting
│   │   ├── data_validation.py        # Data quality checks
│   │   ├── data_transformation.py    # Feature engineering
│   │   ├── model_trainer.py          # Model training
│   │   └── model_evaluation.py       # Model evaluation
│   │
│   └── pipeline/
│       ├── __init__.py
│       ├── training_pipeline.py      # Complete training workflow
│       └── prediction_pipeline.py    # Prediction workflow
│
├── dataset.csv                  # Raw dataset
├── main.py                      # Training execution script
├── app.py                       # Streamlit application
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker configuration
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

---

## 🔬 ML Pipeline

### 1. Data Ingestion
- Reads raw customer data from CSV
- Performs stratified split (80% train, 20% test)
- Preserves class distribution

### 2. Data Validation
- **Schema Validation**: Verifies expected columns
- **Missing Values**: Identifies null values
- **Duplicates**: Detects duplicate records
- **Data Types**: Validates column types

### 3. Data Transformation
- **Feature Engineering**:
  - Tenure groups (0-1 year, 1-2 years, etc.)
  - Monthly charges categories
  - Total services count
- **Encoding**: Label encoding for categorical features
- **Scaling**: StandardScaler for numerical features
- **Imputation**: Median strategy for missing values

### 4. Model Training
Trains and compares 5 different models:

| Model | Description | Hyperparameters |
|-------|-------------|-----------------|
| Logistic Regression | Linear model for binary classification | C, max_iter |
| Decision Tree | Tree-based model | max_depth, min_samples_split |
| Random Forest | Ensemble of decision trees | n_estimators, max_depth |
| Gradient Boosting | Boosting ensemble | n_estimators, learning_rate |
| XGBoost | Optimized gradient boosting | n_estimators, learning_rate, max_depth |

**Hyperparameter Tuning**: GridSearchCV with 5-fold cross-validation

### 5. Model Evaluation

**Metrics**:
- Accuracy
- Precision
- Recall
- F1-Score
- ROC AUC Score

**Visualizations**:
- Confusion Matrix
- ROC Curve
- Feature Importance

---

## 📊 Model Performance

*Example Results (will vary based on training)*

| Model | Accuracy | Precision | Recall | F1-Score | ROC AUC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 0.8045 | 0.6742 | 0.5421 | 0.6012 | 0.8456 |
| Decision Tree | 0.7856 | 0.6234 | 0.5987 | 0.6108 | 0.8123 |
| Random Forest | 0.8234 | 0.7123 | 0.6345 | 0.6712 | 0.8789 |
| Gradient Boosting | 0.8345 | 0.7234 | 0.6456 | 0.6823 | 0.8856 |
| **XGBoost** | **0.8456** | **0.7456** | **0.6678** | **0.7045** | **0.8934** |

**Best Model**: XGBoost with ROC AUC of 0.8934

---

## 🎨 Streamlit Dashboard

### Features

#### 1. Home Page
- Project overview
- Quick statistics
- Model information

#### 2. Customer Prediction
- Interactive input forms
- Real-time predictions
- Probability gauges
- Risk level assessment
- Business recommendations

#### 3. Model Performance
- Model comparison table
- Detailed metrics
- Confusion matrix
- ROC curve
- Feature importance chart

#### 4. Prediction History
- All predictions log
- Summary statistics
- Distribution charts
- CSV export functionality

#### 5. About Project
- Complete documentation
- Architecture details
- Tech stack information

### Screenshots

*[Add screenshots here after running the application]*

---

## 📈 Tableau Dashboard

### Preparing Data for Tableau

Run the Tableau preparation script:

```bash
python src/utils/prepare_tableau_data.py
```

This generates processed CSV files in `artifacts/tableau_data/`:
- `customer_data_with_predictions.csv`
- `churn_summary.csv`
- `risk_segments.csv`

### Dashboard Components

#### 1. Executive Dashboard
**KPIs**:
- Total Customers
- Total Churn Count
- Retention Rate
- Monthly Revenue
- Revenue at Risk

#### 2. Customer Dashboard
- Churn by Gender
- Churn by Age Group
- Churn by Senior Citizen
- Churn by Partner Status
- Churn by Dependents

#### 3. Service Dashboard
- Churn by Contract Type
- Churn by Internet Service
- Churn by Payment Method
- Churn by Tenure
- Monthly Charges Distribution

#### 4. Prediction Dashboard
- High Risk Customers List
- Probability Distribution
- Risk Segments
- Retention Opportunities

### Tableau Connection

1. Open Tableau Desktop
2. Connect to Data → Text File
3. Select the generated CSV files
4. Create relationships between tables
5. Start building visualizations

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t customer-churn-prediction .
```

### Run Container

```bash
docker run -p 8501:8501 customer-churn-prediction
```

Access the application at `http://localhost:8501`

### Docker Compose (Optional)

```bash
docker-compose up
```

---

## 🔮 Future Enhancements

### Short-term
- [ ] REST API development with FastAPI
- [ ] Integration tests
- [ ] CI/CD pipeline
- [ ] Model versioning with MLflow

### Medium-term
- [ ] Real-time data pipeline
- [ ] A/B testing framework
- [ ] Automated model retraining
- [ ] Email/SMS alert system

### Long-term
- [ ] Cloud deployment (AWS/Azure/GCP)
- [ ] Kubernetes orchestration
- [ ] Multi-model ensemble
- [ ] Deep learning models
- [ ] CRM system integration

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Divya Sri Doredla**
- Portfolio: [Your Portfolio](https://yourportfolio.com)
- GitHub: [@divyasridoredla](https://github.com/divyasridoredla)
- LinkedIn: [Divya Sri Doredla](https://linkedin.com/in/divyasridoredla)

---

## 🙏 Acknowledgments

- Dataset: Telco Customer Churn Dataset
- Inspiration: Real-world business problem
- Community: Open source ML community

---

## 📞 Contact & Support

For questions, suggestions, or issues:
- Open an issue on GitHub
- Connect on LinkedIn
- Email: divyasri@example.com

---

**Built with ❤️ by Divya Sri Doredla**

---

## 🙏 Acknowledgments

- Dataset: Telco Customer Churn Dataset
- Inspiration: Real-world business problem
- Community: Open source ML community

---

## 📞 Contact & Support

For questions, suggestions, or issues:
- Open an issue on GitHub
- Email: your.email@example.com
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

**Built with ❤️ using Python and Machine Learning**
#   C u s t o m e r C h u r n P r e d i c t i o n  
 