# Tableau Dashboard Guide - Customer Churn Prediction

## 📊 Overview

This guide helps you create comprehensive Tableau dashboards using the prepared data from the Customer Churn Prediction project.

---

## 🗂️ Data Preparation

### Step 1: Generate Tableau Data

Run the data preparation script:

```bash
python src/utils/prepare_tableau_data.py
```

This creates 6 CSV files in `artifacts/tableau_data/`:

1. **customer_data_enhanced.csv** - Main dataset with all features
2. **summary_metrics.csv** - Key business metrics
3. **churn_by_segments.csv** - Churn analysis by segments
4. **monthly_trend.csv** - Time series data
5. **risk_segments.csv** - Customer risk segmentation
6. **high_value_at_risk.csv** - Priority customers

---

## 📥 Importing Data to Tableau

### Method 1: Direct CSV Import

1. Open Tableau Desktop
2. Click **Connect** → **Text file**
3. Navigate to `artifacts/tableau_data/`
4. Select **customer_data_enhanced.csv**
5. Click **Open**

### Method 2: Multiple Data Sources

1. Import **customer_data_enhanced.csv** as primary
2. Add **churn_by_segments.csv** as secondary
3. Create relationship on common fields if needed

---

## 📊 Dashboard 1: Executive Summary

### Purpose
High-level overview for C-suite executives and stakeholders.

### KPIs to Create

#### 1. Total Customers
- **Calculation**: `COUNT([Customer ID])`
- **Format**: Number with thousands separator
- **Color**: Blue

#### 2. Total Churned
- **Calculation**: `SUM([Churn_Binary])`
- **Format**: Number
- **Color**: Red

#### 3. Churn Rate
- **Calculation**: `SUM([Churn_Binary]) / COUNT([Customer ID])`
- **Format**: Percentage (1 decimal)
- **Color**: Orange
- **Alert**: Red if > 25%, Green if < 20%

#### 4. Total Revenue
- **Calculation**: `SUM([Total Charges])`
- **Format**: Currency
- **Color**: Green

#### 5. Average Revenue Per User (ARPU)
- **Calculation**: `AVG([Monthly Charges])`
- **Format**: Currency
- **Color**: Purple

### Charts to Include

#### Revenue Trend Line
- **Type**: Line Chart
- **X-axis**: Month (if available) or Tenure Group
- **Y-axis**: SUM(Total Charges)
- **Color**: Gradient blue
- **Trend Line**: Yes

#### Churn Distribution Pie Chart
- **Type**: Pie Chart
- **Angle**: Churn (Yes/No)
- **Color**: Red (Yes), Green (No)
- **Labels**: Percentage and Count

---

## 📊 Dashboard 2: Customer Demographics

### Charts to Create

#### 1. Churn by Gender
- **Type**: Bar Chart
- **Rows**: Gender
- **Columns**: COUNT(Customer ID)
- **Color**: Churn
- **Sort**: Descending by count

#### 2. Churn by Age Group
- **Type**: Stacked Bar Chart
- **Rows**: Age_Group (Senior Citizen)
- **Columns**: COUNT(Customer ID)
- **Color**: Churn
- **Labels**: Show percentage

#### 3. Partner & Dependents Impact
- **Type**: Heat Map
- **Rows**: Partner
- **Columns**: Dependents
- **Color**: Churn Rate
- **Labels**: Count and Churn %

#### 4. Customer Lifetime Value
- **Type**: Histogram
- **Bins**: CLV_Estimate (10 bins)
- **Y-axis**: Count of Customers
- **Color**: Churn
- **Overlay**: Average line

---

## 📊 Dashboard 3: Service Analysis

### Charts to Create

#### 1. Churn by Contract Type
- **Type**: Bar Chart
- **Rows**: Contract
- **Columns**: Churn Rate
- **Color**: Gradient red-green
- **Sort**: Descending by churn rate
- **Labels**: Both count and percentage

**Insight**: Month-to-month contracts typically show highest churn.

#### 2. Churn by Internet Service
- **Type**: Grouped Bar Chart
- **Rows**: Internet Service
- **Columns**: COUNT(Customer ID)
- **Color**: Churn
- **Labels**: Yes

**Insight**: Fiber optic users may have higher churn.

#### 3. Payment Method Analysis
- **Type**: Stacked Bar Chart
- **Rows**: Payment Method
- **Columns**: COUNT(Customer ID)
- **Color**: Churn
- **Sort**: By churn count descending

#### 4. Services Adoption Matrix
- **Type**: Heat Map
- **Rows**: Service names (Phone, Internet, Security, etc.)
- **Columns**: Adoption Rate
- **Color**: Churn Rate by service
- **Format**: Percentage

#### 5. Tenure vs Charges Scatter
- **Type**: Scatter Plot
- **X-axis**: Tenure
- **Y-axis**: Monthly Charges
- **Color**: Churn
- **Size**: Total Charges
- **Trend Line**: Yes (separate for each churn group)

**Insight**: Identify clusters of high-risk customers.

---

## 📊 Dashboard 4: Financial Analysis

### Charts to Create

#### 1. Revenue by Customer Segment
- **Type**: Tree Map
- **Size**: SUM(Total Charges)
- **Color**: Churn Rate
- **Labels**: Segment name and revenue

#### 2. Monthly Charges Distribution
- **Type**: Histogram with Density Curve
- **X-axis**: Monthly Charges (bins of $10)
- **Y-axis**: Count of Customers
- **Color**: Churn
- **Reference Line**: Median

#### 3. Revenue at Risk
- **Type**: Bar Chart
- **Calculation**: `SUM(IF [Churn] = "Yes" THEN [Total Charges] END)`
- **Breakdown**: By Contract Type or Service
- **Color**: Red gradient

#### 4. ARPU Trend
- **Type**: Line Chart
- **X-axis**: Tenure Group
- **Y-axis**: AVG(Monthly Charges)
- **Color**: Churn Status
- **Markers**: Yes

---

## 📊 Dashboard 5: Churn Prediction & Risk

### Charts to Create

#### 1. Risk Level Distribution
- **Type**: Donut Chart
- **Angle**: COUNT(Customer ID)
- **Color**: Risk_Level (Very Low → High)
- **Labels**: Count and Percentage

#### 2. High-Risk Customers Table
- **Type**: Text Table
- **Rows**: Customer ID, Tenure, Contract, Monthly Charges
- **Filter**: Risk_Level = "High"
- **Sort**: By Churn Probability descending
- **Highlight**: Top 100 customers

#### 3. Churn Probability Distribution
- **Type**: Histogram
- **X-axis**: Churn Probability (bins of 0.1)
- **Y-axis**: Count
- **Color**: Risk Level
- **Reference Lines**: 0.3, 0.5, 0.7

#### 4. Feature Importance
- **Type**: Bar Chart
- **Rows**: Feature Name
- **Columns**: Importance Score
- **Color**: Gradient
- **Sort**: Descending
- **Top N**: 15 features

#### 5. Retention Opportunities
- **Type**: Bubble Chart
- **X-axis**: Monthly Charges
- **Y-axis**: Tenure
- **Size**: Total Charges
- **Color**: Churn Probability
- **Filter**: Show only high-value at-risk customers

---

## 🎨 Design Best Practices

### Color Schemes

#### Churn Status
- **Yes (Churned)**: #FF4444 (Red)
- **No (Retained)**: #44FF44 (Green)

#### Risk Levels
- **Very Low**: #00FF00 (Green)
- **Low**: #90EE90 (Light Green)
- **Medium**: #FFA500 (Orange)
- **High**: #FF0000 (Red)

#### General
- **Primary**: #1f77b4 (Blue)
- **Secondary**: #ff7f0e (Orange)
- **Accent**: #2ca02c (Green)

### Layout Tips

1. **Dashboard Size**: 1200x800 pixels (standard desktop)
2. **Margins**: 10-20 pixels around elements
3. **Spacing**: Consistent between charts
4. **Font**: Tableau Book (default) or Tableau Medium for headers
5. **Title Size**: 14-16pt
6. **Label Size**: 10-12pt

---

## 🔧 Calculated Fields

### Essential Calculations

#### 1. Churn Rate
```
SUM([Churn_Binary]) / COUNT([Customer ID])
```

#### 2. Retention Rate
```
1 - ([Churn Rate])
```

#### 3. Revenue at Risk
```
SUM(IF [Churn] = "Yes" THEN [Total Charges] END)
```

#### 4. Customer Lifetime Value
```
[Tenure] * [Monthly Charges]
```

#### 5. Is High Value Customer
```
IF [Monthly Charges] > WINDOW_PERCENTILE(SUM([Monthly Charges]), 0.75) 
THEN "High Value" 
ELSE "Standard"
END
```

#### 6. Tenure Segment
```
IF [Tenure] <= 12 THEN "0-1 Year"
ELSEIF [Tenure] <= 24 THEN "1-2 Years"
ELSEIF [Tenure] <= 48 THEN "2-4 Years"
ELSE "4+ Years"
END
```

#### 7. Risk Label
```
IF [Churn_Probability] >= 0.7 THEN "High Risk"
ELSEIF [Churn_Probability] >= 0.5 THEN "Medium Risk"
ELSEIF [Churn_Probability] >= 0.3 THEN "Low Risk"
ELSE "Very Low Risk"
END
```

---

## 📱 Interactive Features

### Filters to Add

1. **Contract Type**: Multi-select dropdown
2. **Internet Service**: Multi-select dropdown
3. **Tenure Range**: Slider (0-72 months)
4. **Monthly Charges Range**: Slider ($0-$150)
5. **Risk Level**: Multi-select
6. **Churn Status**: Single select (All/Yes/No)

### Actions to Implement

1. **Highlight Action**: Click on any chart highlights related data
2. **Filter Action**: Select segment to filter entire dashboard
3. **URL Action**: Click customer ID to open CRM (if applicable)
4. **Tooltip**: Show detailed customer info on hover

### Parameters

#### Risk Threshold
```
Name: Risk Threshold
Data Type: Float
Current Value: 0.5
Allowable Values: Range (0.0 to 1.0)
```

Use in filter: `[Churn_Probability] > [Risk Threshold]`

---

## 📊 Dashboard Assembly

### Dashboard 1: Executive Summary Layout
```
+------------------+------------------+------------------+
|   Total          |   Churned        |   Churn Rate    |
|   Customers      |   Customers      |                  |
+------------------+------------------+------------------+
|   Total Revenue  |   Revenue at     |   ARPU          |
|                  |   Risk           |                  |
+------------------+------------------+------------------+
|                                                        |
|              Revenue Trend Line Chart                 |
|                                                        |
+-------------------------------------------------------+
|                    |                                   |
|  Churn Pie Chart   |   Top 10 Risk Customers Table   |
|                    |                                   |
+-------------------------------------------------------+
```

### Dashboard 2: Demographics Layout
```
+---------------------------+---------------------------+
|                           |                           |
|   Gender Bar Chart        |   Age Group Bar Chart    |
|                           |                           |
+---------------------------+---------------------------+
|                           |                           |
|   Partner/Dependents      |   CLV Histogram          |
|   Heat Map                |                           |
+---------------------------+---------------------------+
```

---

## 🔄 Refresh Strategy

### Automatic Refresh
1. Go to **Server** → **Publish Data Source**
2. Select refresh schedule (e.g., Daily at 2 AM)
3. Set up incremental refresh if data is large

### Manual Refresh
1. Right-click data source
2. Select **Refresh**
3. All worksheets update automatically

---

## 📤 Publishing to Tableau Server

### Steps

1. **Save Workbook**: File → Save to Tableau Public/Server
2. **Select Data Source**: Choose embedded or published
3. **Set Permissions**: Configure user access
4. **Schedule Refreshes**: Set automatic updates
5. **Share URL**: Distribute dashboard link

---

## 🎯 Key Metrics Summary

| Metric | Target | Action Required |
|--------|---------|-----------------|
| Churn Rate | < 20% | Alert if > 25% |
| Retention Rate | > 80% | Monitor monthly |
| ARPU | > $60 | Track by segment |
| High Risk Customers | < 15% | Weekly review |
| Revenue at Risk | < $50K | Monthly action plan |

---

## 💡 Tips & Tricks

1. **Use Dashboard Actions**: Make dashboards interactive
2. **Optimize Performance**: Use extracts instead of live connections
3. **Mobile Layout**: Create separate layout for mobile view
4. **Storytelling**: Use Tableau Stories to guide users
5. **Consistent Formatting**: Apply same style across all charts
6. **Context Filters**: Use for better query performance
7. **Level of Detail (LOD)**: For complex calculations
8. **Sets**: Create dynamic customer groups

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: Data not refreshing
- **Solution**: Check data source connection and extract schedule

**Issue**: Slow dashboard performance
- **Solution**: Use filters, reduce marks, optimize calculations

**Issue**: Charts showing "NULL"
- **Solution**: Check data quality, add IF/IFNULL in calculations

**Issue**: Colors not matching
- **Solution**: Edit color legend and manually set colors

---

## 📚 Resources

- [Tableau Official Documentation](https://help.tableau.com/)
- [Tableau Community Forums](https://community.tableau.com/)
- [Tableau Public Gallery](https://public.tableau.com/gallery/)
- [Best Practices Guide](https://help.tableau.com/current/pro/desktop/en-us/best_practices.htm)

---

**Created by**: ML Engineering Team  
**Version**: 1.0  
**Last Updated**: 2024

Happy Visualizing! 📊✨
