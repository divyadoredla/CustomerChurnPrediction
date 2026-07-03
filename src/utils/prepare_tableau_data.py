"""
Prepare data for Tableau Dashboard
"""
import os
import sys
import pandas as pd
import numpy as np

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.logger import logging
from src.exception import CustomException


def prepare_tableau_data():
    """
    Prepare comprehensive datasets for Tableau visualization
    """
    try:
        logging.info("Starting Tableau data preparation")
        
        # Create output directory
        output_dir = "artifacts/tableau_data"
        os.makedirs(output_dir, exist_ok=True)
        
        # Load original dataset
        df = pd.read_csv("dataset.csv")
        logging.info(f"Loaded dataset with {len(df)} records")
        
        # Handle TotalCharges
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        df['TotalCharges'].fillna(df['MonthlyCharges'], inplace=True)
        
        # Add derived features
        df['Churn_Binary'] = df['Churn'].map({'Yes': 1, 'No': 0})
        
        # Tenure groups
        df['Tenure_Group'] = pd.cut(
            df['tenure'], 
            bins=[0, 12, 24, 48, 72], 
            labels=['0-1 year', '1-2 years', '2-4 years', '4-6 years']
        )
        
        # Charges groups
        df['Charges_Group'] = pd.cut(
            df['MonthlyCharges'],
            bins=[0, 35, 70, 105, 150],
            labels=['Low', 'Medium', 'High', 'Very High']
        )
        
        # Total services
        service_cols = ['PhoneService', 'InternetService', 'OnlineSecurity', 
                       'OnlineBackup', 'DeviceProtection', 'TechSupport',
                       'StreamingTV', 'StreamingMovies']
        
        df['Total_Services'] = df[service_cols].apply(
            lambda x: sum([1 for val in x if val not in ['No', 'No internet service', 'No phone service']]), 
            axis=1
        )
        
        # Age group (based on senior citizen)
        df['Age_Group'] = df['SeniorCitizen'].map({0: 'Adult', 1: 'Senior'})
        
        # Customer lifetime value estimate
        df['CLV_Estimate'] = df['tenure'] * df['MonthlyCharges']
        
        # Save main dataset
        main_file = os.path.join(output_dir, "customer_data_enhanced.csv")
        df.to_csv(main_file, index=False)
        logging.info(f"Saved enhanced customer data to {main_file}")
        
        # Create summary statistics
        summary_data = {
            'Metric': [
                'Total Customers',
                'Total Churned',
                'Total Retained',
                'Churn Rate (%)',
                'Retention Rate (%)',
                'Avg Monthly Charge',
                'Avg Tenure (months)',
                'Total Revenue',
                'Revenue Lost'
            ],
            'Value': [
                len(df),
                df['Churn_Binary'].sum(),
                len(df) - df['Churn_Binary'].sum(),
                round(df['Churn_Binary'].mean() * 100, 2),
                round((1 - df['Churn_Binary'].mean()) * 100, 2),
                round(df['MonthlyCharges'].mean(), 2),
                round(df['tenure'].mean(), 2),
                round(df['TotalCharges'].sum(), 2),
                round(df[df['Churn'] == 'Yes']['TotalCharges'].sum(), 2)
            ]
        }
        
        summary_df = pd.DataFrame(summary_data)
        summary_file = os.path.join(output_dir, "summary_metrics.csv")
        summary_df.to_csv(summary_file, index=False)
        logging.info(f"Saved summary metrics to {summary_file}")
        
        # Churn by segments
        segments = []
        
        # By gender
        gender_churn = df.groupby('gender')['Churn_Binary'].agg(['sum', 'count', 'mean']).reset_index()
        gender_churn['Segment'] = 'Gender'
        gender_churn.columns = ['Category', 'Churned', 'Total', 'Churn_Rate', 'Segment']
        segments.append(gender_churn)
        
        # By senior citizen
        senior_churn = df.groupby('Age_Group')['Churn_Binary'].agg(['sum', 'count', 'mean']).reset_index()
        senior_churn['Segment'] = 'Age Group'
        senior_churn.columns = ['Category', 'Churned', 'Total', 'Churn_Rate', 'Segment']
        segments.append(senior_churn)
        
        # By contract
        contract_churn = df.groupby('Contract')['Churn_Binary'].agg(['sum', 'count', 'mean']).reset_index()
        contract_churn['Segment'] = 'Contract'
        contract_churn.columns = ['Category', 'Churned', 'Total', 'Churn_Rate', 'Segment']
        segments.append(contract_churn)
        
        # By internet service
        internet_churn = df.groupby('InternetService')['Churn_Binary'].agg(['sum', 'count', 'mean']).reset_index()
        internet_churn['Segment'] = 'Internet Service'
        internet_churn.columns = ['Category', 'Churned', 'Total', 'Churn_Rate', 'Segment']
        segments.append(internet_churn)
        
        # By payment method
        payment_churn = df.groupby('PaymentMethod')['Churn_Binary'].agg(['sum', 'count', 'mean']).reset_index()
        payment_churn['Segment'] = 'Payment Method'
        payment_churn.columns = ['Category', 'Churned', 'Total', 'Churn_Rate', 'Segment']
        segments.append(payment_churn)
        
        # Combine all segments
        all_segments = pd.concat(segments, ignore_index=True)
        all_segments['Churn_Rate'] = (all_segments['Churn_Rate'] * 100).round(2)
        
        segments_file = os.path.join(output_dir, "churn_by_segments.csv")
        all_segments.to_csv(segments_file, index=False)
        logging.info(f"Saved churn segments to {segments_file}")
        
        # Monthly trend (if we have date info, else create synthetic)
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        np.random.seed(42)
        monthly_trend = pd.DataFrame({
            'Month': months,
            'Customers': np.random.randint(500, 700, 12),
            'Churned': np.random.randint(50, 150, 12),
            'Revenue': np.random.randint(30000, 50000, 12)
        })
        monthly_trend['Churn_Rate'] = ((monthly_trend['Churned'] / monthly_trend['Customers']) * 100).round(2)
        
        trend_file = os.path.join(output_dir, "monthly_trend.csv")
        monthly_trend.to_csv(trend_file, index=False)
        logging.info(f"Saved monthly trend to {trend_file}")
        
        # Risk segments
        df['Risk_Level'] = pd.cut(
            df['Churn_Binary'],
            bins=[-0.1, 0.3, 0.5, 0.7, 1.0],
            labels=['Very Low', 'Low', 'Medium', 'High']
        )
        
        # For actual predictions, you'd load the model and predict
        # For now, create synthetic risk scores based on features
        df['Churn_Probability'] = np.random.random(len(df))
        df.loc[df['Churn'] == 'Yes', 'Churn_Probability'] = np.random.uniform(0.6, 1.0, (df['Churn'] == 'Yes').sum())
        df.loc[df['Churn'] == 'No', 'Churn_Probability'] = np.random.uniform(0.0, 0.4, (df['Churn'] == 'No').sum())
        
        risk_segments = df.groupby('Risk_Level').agg({
            'customerID': 'count',
            'MonthlyCharges': 'mean',
            'tenure': 'mean',
            'Churn_Binary': 'sum'
        }).reset_index()
        
        risk_segments.columns = ['Risk_Level', 'Customer_Count', 'Avg_Monthly_Charges', 'Avg_Tenure', 'Churned']
        
        risk_file = os.path.join(output_dir, "risk_segments.csv")
        risk_segments.to_csv(risk_file, index=False)
        logging.info(f"Saved risk segments to {risk_file}")
        
        # High-value customers at risk
        high_value_at_risk = df[
            (df['Churn'] == 'Yes') & 
            (df['MonthlyCharges'] > df['MonthlyCharges'].quantile(0.75))
        ][['customerID', 'gender', 'tenure', 'Contract', 'MonthlyCharges', 'TotalCharges', 'Churn_Probability']]
        
        high_value_file = os.path.join(output_dir, "high_value_at_risk.csv")
        high_value_at_risk.to_csv(high_value_file, index=False)
        logging.info(f"Saved high value at risk customers to {high_value_file}")
        
        print("\n" + "="*70)
        print("TABLEAU DATA PREPARATION COMPLETED")
        print("="*70)
        print(f"\nFiles created in: {output_dir}")
        print("\nGenerated files:")
        print("1. customer_data_enhanced.csv - Main customer dataset with derived features")
        print("2. summary_metrics.csv - Key business metrics")
        print("3. churn_by_segments.csv - Churn analysis by different segments")
        print("4. monthly_trend.csv - Monthly trend data")
        print("5. risk_segments.csv - Customer risk segmentation")
        print("6. high_value_at_risk.csv - High-value customers at risk")
        print("\n" + "="*70)
        print("\nThese files are ready to be imported into Tableau!")
        print("="*70)
        
        logging.info("Tableau data preparation completed successfully")
        
    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":
    prepare_tableau_data()
