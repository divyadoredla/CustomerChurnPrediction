# 🚀 Quick Start Guide

Get up and running with Customer Churn Prediction in 5 minutes!

---

## ⚡ Super Fast Setup

### Windows Users

```bash
# 1. Clone and navigate
git clone <repository-url>
cd customer-churn-prediction

# 2. Setup virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train model (takes 5-10 minutes)
run_training.bat

# 5. Launch dashboard
run_app.bat
```

### Linux/Mac Users

```bash
# 1. Clone and navigate
git clone <repository-url>
cd customer-churn-prediction

# 2. Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Make scripts executable
chmod +x run_training.sh run_app.sh

# 5. Train model (takes 5-10 minutes)
./run_training.sh

# 6. Launch dashboard
./run_app.sh
```

### Using Docker

```bash
# Build and run in one command
docker build -t churn-prediction . && docker run -p 8501:8501 churn-prediction

# Access at http://localhost:8501
```

---

## 📋 What You'll See

### During Training

```
======================================================================
CUSTOMER CHURN PREDICTION - TRAINING PIPELINE STARTED
======================================================================

======================================================================
STEP 1: DATA INGESTION
======================================================================
Reading data from dataset.csv
Dataset shape: (7043, 21)
Splitting data into train and test sets...
Train set shape: (5634, 21)
Test set shape: (1409, 21)

======================================================================
STEP 2: DATA VALIDATION
======================================================================
Validating training data...
Validating test data...
Total missing values: 11

======================================================================
STEP 3: DATA TRANSFORMATION
======================================================================
Creating preprocessing pipeline...
Applying feature engineering...
Encoding categorical features...
Train data shape after transformation: (5634, 22)

======================================================================
STEP 4: MODEL TRAINING
======================================================================
Training Logistic Regression...
Best parameters: {'C': 1, 'max_iter': 1000}
Test Accuracy: 0.8045

Training Random Forest...
Best parameters: {'max_depth': 20, 'n_estimators': 200}
Test Accuracy: 0.8234

Training XGBoost...
Best parameters: {'learning_rate': 0.1, 'max_depth': 5, 'n_estimators': 200}
Test Accuracy: 0.8456

======================================================================
MODEL COMPARISON REPORT
======================================================================
Best Model: XGBoost
Best ROC AUC Score: 0.8934

======================================================================
TRAINING PIPELINE COMPLETED SUCCESSFULLY
======================================================================
```

### Dashboard Pages

1. **Home** 🏠
   - Project overview
   - Quick stats
   - Getting started guide

2. **Customer Prediction** 🔮
   - Enter customer details
   - Get instant prediction
   - View probability gauge
   - Receive recommendations

3. **Model Performance** 📈
   - Compare all models
   - View metrics
   - See confusion matrix
   - Check feature importance

4. **Prediction History** 📜
   - View all predictions
   - Download as CSV
   - Analyze trends

5. **About Project** ℹ️
   - Technical details
   - Architecture
   - Documentation

---

## 🎯 Try These Examples

### Example 1: High Risk Customer

```
Gender: Male
Senior Citizen: No
Partner: No
Dependents: No
Tenure: 1 month
Contract: Month-to-month
Internet Service: Fiber optic
Monthly Charges: $85
Payment Method: Electronic check
```

**Expected**: High churn probability (~75%)

### Example 2: Low Risk Customer

```
Gender: Female
Senior Citizen: No
Partner: Yes
Dependents: Yes
Tenure: 48 months
Contract: Two year
Internet Service: DSL
Monthly Charges: $55
Payment Method: Bank transfer (automatic)
```

**Expected**: Low churn probability (~15%)

---

## 📊 Generate Tableau Data

```bash
# After training, generate Tableau datasets
python src/utils/prepare_tableau_data.py

# Files created in artifacts/tableau_data/
# Import these into Tableau Desktop
```

---

## 🐛 Troubleshooting

### Issue: "Module not found"
```bash
# Solution: Install in editable mode
pip install -e .
```

### Issue: "Port already in use"
```bash
# Solution: Use different port
streamlit run app.py --server.port 8502
```

### Issue: "Model not found"
```bash
# Solution: Train model first
python main.py
```

### Issue: "Permission denied" (Linux/Mac)
```bash
# Solution: Make scripts executable
chmod +x run_training.sh run_app.sh
```

---

## 📁 Project Files

### Essential Files

- **main.py**: Run this to train models
- **app.py**: Streamlit dashboard
- **config/config.yaml**: All settings
- **requirements.txt**: Dependencies
- **dataset.csv**: Your data

### Generated Artifacts

After training, check `artifacts/` folder:

```
artifacts/
├── models/
│   └── best_model.pkl          # Trained model
├── plots/
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   └── feature_importance.png
├── train.csv                   # Training data
├── test.csv                    # Test data
├── preprocessor.pkl            # Preprocessing pipeline
├── model_comparison.json       # Model scores
└── evaluation_metrics.json     # Detailed metrics
```

---

## 🎓 Next Steps

1. ✅ **Explore Dashboard**: Try different customer inputs
2. ✅ **Review Model Performance**: Check metrics and charts
3. ✅ **Modify Configuration**: Edit config/config.yaml
4. ✅ **Create Tableau Dashboards**: Follow TABLEAU_GUIDE.md
5. ✅ **Customize Features**: Add your own features
6. ✅ **Deploy**: Use Docker for production

---

## 📚 Documentation

- **README.md**: Complete project documentation
- **INSTALLATION_GUIDE.md**: Detailed setup instructions
- **TABLEAU_GUIDE.md**: Tableau visualization guide
- **CONTRIBUTING.md**: How to contribute
- **PROJECT_SUMMARY.md**: Technical overview

---

## 💡 Tips

### Performance
- Training takes 5-15 minutes depending on your machine
- First prediction might be slow (model loading)
- Use Docker for consistent performance

### Customization
- Edit `config/config.yaml` for model parameters
- Modify `app.py` for dashboard changes
- Update `config.yaml` to add/remove models

### Best Practices
- Train on full dataset for best results
- Retrain monthly with new data
- Monitor prediction accuracy
- Keep logs for debugging

---

## 🆘 Help

### Common Questions

**Q: Do I need GPU?**  
A: No, CPU is sufficient for this dataset size.

**Q: How long does training take?**  
A: 5-15 minutes on a standard laptop.

**Q: Can I use my own data?**  
A: Yes! Replace dataset.csv and update config.yaml.

**Q: How accurate is the model?**  
A: Typically 84-87% accuracy, 88-91% ROC AUC.

**Q: Can I add more models?**  
A: Yes! Edit src/components/model_trainer.py.

### Get Support

- **Issues**: GitHub Issues
- **Questions**: Discussions tab
- **Email**: your.email@example.com

---

## ✅ Success Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Model trained successfully
- [ ] Dashboard launches
- [ ] Can make predictions
- [ ] Artifacts generated
- [ ] Logs created

---

## 🎉 You're Ready!

Your Customer Churn Prediction system is now ready to use!

**Dashboard URL**: http://localhost:8501

**Start predicting customer churn and improve retention!** 🚀

---

## 📞 Support

Having issues? We're here to help!

1. Check **INSTALLATION_GUIDE.md**
2. Review **logs/** directory
3. Open a GitHub Issue
4. Contact via email

---

*Happy Predicting! 🎯*
