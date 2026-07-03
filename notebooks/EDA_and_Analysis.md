# Exploratory Data Analysis - Customer Churn Dataset

## Overview
This document provides insights from exploratory data analysis of the customer churn dataset.

## Dataset Summary

### Basic Information
- **Total Records**: 7,043 customers
- **Features**: 21 columns
- **Target Variable**: Churn (Yes/No)
- **Problem Type**: Binary Classification

### Feature Categories

#### 1. Demographic Features
- `gender`: Male/Female
- `SeniorCitizen`: 0 (No) / 1 (Yes)
- `Partner`: Yes/No
- `Dependents`: Yes/No

#### 2. Service Features
- `PhoneService`: Yes/No
- `MultipleLines`: Yes/No/No phone service
- `InternetService`: DSL/Fiber optic/No
- `OnlineSecurity`: Yes/No/No internet service
- `OnlineBackup`: Yes/No/No internet service
- `DeviceProtection`: Yes/No/No internet service
- `TechSupport`: Yes/No/No internet service
- `StreamingTV`: Yes/No/No internet service
- `StreamingMovies`: Yes/No/No internet service

#### 3. Account Features
- `tenure`: Number of months with company (0-72)
- `Contract`: Month-to-month/One year/Two year
- `PaperlessBilling`: Yes/No
- `PaymentMethod`: Electronic check/Mailed check/Bank transfer/Credit card
- `MonthlyCharges`: Monthly bill amount ($18-$118)
- `TotalCharges`: Total amount charged ($18-$8,684)

## Key Insights

### 1. Churn Distribution
- **Churn Rate**: ~26.5% (approximate)
- **Class Imbalance**: Moderate (73.5% retained vs 26.5% churned)

### 2. Important Patterns

#### Contract Type
- Month-to-month contracts show significantly higher churn
- Two-year contracts have lowest churn rate
- **Recommendation**: Incentivize long-term contracts

#### Internet Service
- Fiber optic customers have higher churn rates
- DSL customers are more stable
- **Possible Issue**: Service quality or pricing concerns with fiber optic

#### Payment Method
- Electronic check users churn more frequently
- Automatic payments (bank transfer, credit card) correlate with retention
- **Recommendation**: Promote automatic payment methods

#### Tenure
- New customers (0-12 months) have highest churn risk
- Churn rate decreases significantly after 12 months
- **Critical Period**: First year of service

#### Monthly Charges
- Higher monthly charges correlate with higher churn
- Customers paying $70+ are at higher risk
- **Price Sensitivity**: Important factor in churn

#### Services
- Customers with security and support services churn less
- Streaming services alone don't prevent churn
- **Value Addition**: Support services are retention drivers

### 3. Data Quality Issues

#### Missing Values
- `TotalCharges`: Contains some blank values (converted to 0 or imputed)
- Solution: Imputation using median or monthlyCharges * tenure

#### Data Type Issues
- `TotalCharges`: Stored as string but should be numeric
- `SeniorCitizen`: Stored as integer (0/1) but categorical in nature

## Feature Engineering Opportunities

### 1. Tenure Groups
```python
- '0-1 year': High risk
- '1-2 years': Medium risk
- '2-4 years': Lower risk
- '4-6 years': Very low risk
```

### 2. Charges Groups
```python
- 'Low': $0-35
- 'Medium': $35-70
- 'High': $70-105
- 'Very High': $105+
```

### 3. Total Services Count
Count of all services subscribed (0-8)
- More services = Higher retention

### 4. Customer Lifetime Value (CLV)
```python
CLV = tenure * MonthlyCharges
```

### 5. Service Diversity Score
Ratio of services used to services available

## Recommended Visualizations for Tableau

### Executive Dashboard
1. **KPI Cards**:
   - Total Customers
   - Churn Count & Rate
   - Retention Rate
   - Total Revenue
   - Revenue at Risk

2. **Trend Charts**:
   - Monthly churn trend
   - Revenue trend
   - Customer acquisition vs churn

### Customer Analysis Dashboard
1. **Demographics**:
   - Churn by Gender (Bar chart)
   - Churn by Age Group (Pie chart)
   - Churn by Partner/Dependents (Stacked bar)

2. **Behavioral**:
   - Tenure distribution (Histogram)
   - Service adoption (Heat map)
   - Payment method distribution

### Service Analysis Dashboard
1. **Service Impact**:
   - Churn by Internet Service type
   - Churn by Contract type
   - Service bundle analysis

2. **Financial**:
   - Monthly charges distribution
   - Charges vs Tenure (Scatter plot)
   - Revenue by segment

### Risk Dashboard
1. **Prediction Results**:
   - Risk level distribution
   - High-risk customer list
   - Probability distribution

2. **Retention Opportunities**:
   - High-value customers at risk
   - Recommended actions
   - Expected retention impact

## Model Features Priority

### High Importance Features (Based on Business Logic)
1. Contract type
2. Tenure
3. Internet Service type
4. Monthly Charges
5. Total Charges
6. Payment Method
7. Tech Support
8. Online Security

### Medium Importance Features
1. Total Services count
2. Paperless Billing
3. Multiple Lines
4. Streaming Services
5. Senior Citizen

### Lower Importance Features
1. Gender
2. Partner
3. Dependents
4. Phone Service

## Business Recommendations

### Immediate Actions
1. **Target Month-to-Month Customers**: Offer incentives for contract upgrades
2. **First-Year Focus**: Implement welcome program for new customers
3. **Payment Method Migration**: Encourage automatic payments
4. **Service Bundling**: Promote security and support services

### Medium-term Strategies
1. **Fiber Optic Investigation**: Review pricing and quality
2. **Price Optimization**: Test different pricing tiers
3. **Loyalty Program**: Reward long-tenure customers
4. **Proactive Support**: Reach out to high-risk customers

### Long-term Initiatives
1. **Predictive Monitoring**: Real-time churn risk scoring
2. **Personalization**: Tailored retention offers
3. **Customer Success Team**: Dedicated retention specialists
4. **Product Improvements**: Based on churn reasons

## Statistical Tests to Perform

1. **Chi-Square Test**: Categorical features vs Churn
2. **T-Test**: Numerical features vs Churn groups
3. **Correlation Analysis**: Feature relationships
4. **ANOVA**: Multiple group comparisons

## Next Steps

1. ✅ Complete EDA
2. ✅ Feature Engineering
3. ✅ Model Training
4. ✅ Model Evaluation
5. ✅ Deployment Pipeline
6. ⬜ A/B Testing Framework
7. ⬜ Real-time Monitoring
8. ⬜ Feedback Loop Integration

---

**Date**: 2024
**Analyst**: ML Engineering Team
**Version**: 1.0
