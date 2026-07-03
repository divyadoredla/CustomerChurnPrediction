"""
Streamlit Web Application for Customer Churn Prediction
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import json
import os
from datetime import datetime

from src.pipeline.prediction_pipeline import PredictionPipeline, CustomData
from src.logger import logging


# Page Configuration
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2c3e50;
        font-weight: bold;
        margin-top: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .prediction-box {
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .churn-yes {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
    }
    .churn-no {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
    }
    </style>
""", unsafe_allow_html=True)


def load_prediction_history():
    """Load prediction history from file"""
    history_file = "artifacts/prediction_history.json"
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            return json.load(f)
    return []


def save_prediction(prediction_data):
    """Save prediction to history"""
    history_file = "artifacts/prediction_history.json"
    os.makedirs("artifacts", exist_ok=True)
    
    history = load_prediction_history()
    prediction_data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append(prediction_data)
    
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)


def home_page():
    """Home Page"""
    st.markdown('<h1 class="main-header">🎯 Customer Churn Prediction System</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Welcome to the Customer Churn Prediction Dashboard
    
    This application uses **Machine Learning** to predict customer churn and provides actionable insights 
    for customer retention strategies.
    
    #### 🚀 Features:
    - **Real-time Predictions**: Get instant churn predictions for customers
    - **Model Performance**: View detailed model evaluation metrics
    - **Visualizations**: Interactive charts and graphs
    - **Prediction History**: Track all predictions over time
    - **Business Intelligence**: Actionable recommendations
    
    #### 📊 Project Overview:
    - **Objective**: Predict whether a customer will churn
    - **Models Used**: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost
    - **Best Model**: Automatically selected based on ROC AUC score
    - **Metrics**: Accuracy, Precision, Recall, F1-Score, ROC AUC
    
    #### 🎓 Use Cases:
    - Identify high-risk customers
    - Proactive retention campaigns
    - Resource optimization
    - Revenue protection
    
    ---
    
    ### 👈 Get Started
    Select an option from the sidebar to begin!
    """)
    
    # Display some statistics if model exists
    if os.path.exists("artifacts/model_comparison.json"):
        with open("artifacts/model_comparison.json", 'r') as f:
            comparison = json.load(f)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Best Model</h3>
                <h2>{comparison['best_model']}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Best Accuracy</h3>
                <h2>{comparison['best_score']:.4f}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            history = load_prediction_history()
            st.markdown(f"""
            <div class="metric-card">
                <h3>Total Predictions</h3>
                <h2>{len(history)}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        # Model Comparison Table
        st.markdown("---")
        st.markdown("### 🤖 Models Used in This Project")
        
        # Create DataFrame for model comparison
        models_data = []
        for model_name, metrics in comparison['all_models'].items():
            models_data.append({
                'Model': model_name,
                'Accuracy': f"{metrics['test_accuracy']*100:.2f}%",
                'ROC AUC': f"{metrics['test_roc_auc']*100:.2f}%",
                'Precision': f"{metrics['test_precision']*100:.2f}%",
                'Recall': f"{metrics['test_recall']*100:.2f}%",
                'F1-Score': f"{metrics['test_f1_score']*100:.2f}%"
            })
        
        models_df = pd.DataFrame(models_data)
        
        # Highlight best model
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 1rem; border-radius: 10px; color: white; text-align: center; margin-bottom: 1rem;'>
            <h3>🏆 Best Model: {comparison['best_model']} with {comparison['best_score']*100:.2f}% Accuracy</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Display table with custom styling
        st.dataframe(
            models_df,
            use_container_width=True,
            hide_index=True
        )
        
        st.info(f"✨ The **{comparison['best_model']}** model was automatically selected as the best performer based on Accuracy!")


def prediction_page():
    """Customer Prediction Page"""
    st.markdown('<h1 class="main-header">🔮 Customer Churn Prediction</h1>', unsafe_allow_html=True)
    
    st.markdown("### Enter Customer Information")
    
    # Create two columns for input
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👤 Customer Demographics")
        gender = st.selectbox("Gender", ["Male", "Female"])
        SeniorCitizen = st.selectbox("Senior Citizen", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        Partner = st.selectbox("Partner", ["Yes", "No"])
        Dependents = st.selectbox("Dependents", ["Yes", "No"])
        
        st.markdown("#### 📞 Services")
        PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
        MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
        InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
        OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    
    with col2:
        st.markdown("#### 🔐 Additional Services")
        DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
        TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
        StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
        StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
        
        st.markdown("#### 💳 Account Information")
        Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
        PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
        PaymentMethod = st.selectbox("Payment Method", 
                                     ["Electronic check", "Mailed check", 
                                      "Bank transfer (automatic)", "Credit card (automatic)"])
    
    # Numerical inputs
    st.markdown("#### 💰 Financial Information")
    col3, col4, col5 = st.columns(3)
    
    with col3:
        tenure = st.slider("Tenure (months)", 0, 72, 12)
    with col4:
        MonthlyCharges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=150.0, value=50.0)
    with col5:
        TotalCharges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=500.0)
    
    # Prediction button
    if st.button("🎯 Predict Churn", use_container_width=True):
        with st.spinner("Analyzing customer data..."):
            try:
                # Create custom data object
                custom_data = CustomData(
                    gender=gender,
                    SeniorCitizen=SeniorCitizen,
                    Partner=Partner,
                    Dependents=Dependents,
                    tenure=tenure,
                    PhoneService=PhoneService,
                    MultipleLines=MultipleLines,
                    InternetService=InternetService,
                    OnlineSecurity=OnlineSecurity,
                    OnlineBackup=OnlineBackup,
                    DeviceProtection=DeviceProtection,
                    TechSupport=TechSupport,
                    StreamingTV=StreamingTV,
                    StreamingMovies=StreamingMovies,
                    Contract=Contract,
                    PaperlessBilling=PaperlessBilling,
                    PaymentMethod=PaymentMethod,
                    MonthlyCharges=MonthlyCharges,
                    TotalCharges=TotalCharges
                )
                
                # Get dataframe
                input_df = custom_data.get_data_as_dataframe()
                
                # Make prediction
                pipeline = PredictionPipeline()
                result = pipeline.predict(input_df)
                
                # Display result
                prediction = result['prediction']
                churn_prob = result['churn_probability']
                retention_prob = result['retention_probability']
                confidence = result['confidence']
                risk_level = result['risk_level']
                
                # Save prediction
                save_prediction({
                    'prediction': prediction,
                    'churn_probability': churn_prob,
                    'risk_level': risk_level,
                    'customer_data': input_df.to_dict('records')[0]
                })
                
                # Display prediction box
                box_class = "churn-yes" if prediction == "Yes" else "churn-no"
                st.markdown(f"""
                <div class="prediction-box {box_class}">
                    <h2>{'⚠️ Customer Will Churn' if prediction == 'Yes' else '✅ Customer Will Stay'}</h2>
                    <h3>Risk Level: {risk_level}</h3>
                </div>
                """, unsafe_allow_html=True)
                
                # Probability visualization
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Churn Probability", f"{churn_prob}%", 
                             delta=f"{'High' if churn_prob > 50 else 'Low'} Risk")
                
                with col2:
                    st.metric("Retention Probability", f"{retention_prob}%",
                             delta=f"{'Good' if retention_prob > 50 else 'Poor'}")
                
                with col3:
                    st.metric("Confidence Score", f"{confidence}%")
                
                # Gauge chart
                fig = go.Figure(go.Indicator(
                    mode="gauge+number+delta",
                    value=churn_prob,
                    domain={'x': [0, 1], 'y': [0, 1]},
                    title={'text': "Churn Probability", 'font': {'size': 24}},
                    delta={'reference': 50, 'increasing': {'color': "red"}},
                    gauge={
                        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                        'bar': {'color': "darkblue"},
                        'bgcolor': "white",
                        'borderwidth': 2,
                        'bordercolor': "gray",
                        'steps': [
                            {'range': [0, 30], 'color': '#00ff00'},
                            {'range': [30, 50], 'color': '#ffff00'},
                            {'range': [50, 70], 'color': '#ff9900'},
                            {'range': [70, 100], 'color': '#ff0000'}
                        ],
                        'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': 70
                        }
                    }
                ))
                
                fig.update_layout(height=400)
                st.plotly_chart(fig, use_container_width=True)
                
                # Recommendations
                st.markdown("### 💡 Recommendations")
                if prediction == "Yes":
                    st.error("""
                    **Immediate Actions Required:**
                    - 🎯 Priority customer for retention campaign
                    - 📞 Schedule personalized outreach call
                    - 💰 Consider offering special retention discount
                    - 🎁 Provide loyalty rewards or upgraded services
                    - 📧 Send targeted email with exclusive offers
                    """)
                else:
                    st.success("""
                    **Customer Retention Strategies:**
                    - ✅ Continue current engagement strategy
                    - 📈 Monitor usage patterns regularly
                    - 🎉 Acknowledge loyalty with appreciation messages
                    - 💬 Request feedback for continuous improvement
                    - 🔄 Offer upgrade opportunities
                    """)
                
            except Exception as e:
                st.error(f"Error making prediction: {str(e)}")
                logging.error(f"Prediction error: {str(e)}")


def model_performance_page():
    """Model Performance Page"""
    st.markdown('<h1 class="main-header">📈 Model Performance</h1>', unsafe_allow_html=True)
    
    # Load model comparison
    if os.path.exists("artifacts/model_comparison.json"):
        with open("artifacts/model_comparison.json", 'r') as f:
            comparison = json.load(f)
        
        st.markdown("### 🏆 Best Model")
        st.success(f"**{comparison['best_model']}** - ROC AUC: {comparison['best_score']:.4f}")
        
        # Model comparison table
        st.markdown("### 📊 Model Comparison")
        models_df = pd.DataFrame(comparison['all_models']).T
        models_df = models_df.round(4)
        st.dataframe(models_df, use_container_width=True)
        
        # Bar chart
        fig = px.bar(models_df, x=models_df.index, y='test_roc_auc',
                    title='Model Comparison - ROC AUC Scores',
                    labels={'test_roc_auc': 'ROC AUC Score', 'index': 'Model'},
                    color='test_roc_auc',
                    color_continuous_scale='viridis')
        st.plotly_chart(fig, use_container_width=True)
        
    else:
        st.warning("Model comparison data not found. Please train the model first.")
    
    # Load evaluation metrics
    if os.path.exists("artifacts/evaluation_metrics.json"):
        with open("artifacts/evaluation_metrics.json", 'r') as f:
            metrics = json.load(f)
        
        st.markdown("### 🎯 Detailed Metrics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Accuracy", f"{metrics['accuracy']:.4f}")
        with col2:
            st.metric("Precision", f"{metrics['precision']:.4f}")
        with col3:
            st.metric("Recall", f"{metrics['recall']:.4f}")
        with col4:
            st.metric("F1 Score", f"{metrics['f1_score']:.4f}")
        
        # Classification Report
        st.markdown("### 📋 Classification Report")
        st.text(metrics['classification_report'])
        
        # Display plots if they exist
        if os.path.exists("artifacts/plots/confusion_matrix.png"):
            st.markdown("### 🔢 Confusion Matrix")
            st.image("artifacts/plots/confusion_matrix.png")
        
        if os.path.exists("artifacts/plots/roc_curve.png"):
            st.markdown("### 📉 ROC Curve")
            st.image("artifacts/plots/roc_curve.png")
        
        if os.path.exists("artifacts/plots/feature_importance.png"):
            st.markdown("### 🎯 Feature Importance")
            st.image("artifacts/plots/feature_importance.png")


def prediction_history_page():
    """Prediction History Page"""
    st.markdown('<h1 class="main-header">📜 Prediction History</h1>', unsafe_allow_html=True)
    
    history = load_prediction_history()
    
    if history:
        st.markdown(f"### Total Predictions: {len(history)}")
        
        # Convert to dataframe
        history_df = pd.DataFrame(history)
        
        # Summary statistics
        if 'prediction' in history_df.columns:
            churn_count = (history_df['prediction'] == 'Yes').sum()
            retention_count = (history_df['prediction'] == 'No').sum()
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Total Predictions", len(history))
            with col2:
                st.metric("Predicted Churns", churn_count)
            with col3:
                st.metric("Predicted Retentions", retention_count)
            
            # Pie chart
            fig = px.pie(values=[churn_count, retention_count], 
                        names=['Churn', 'Retention'],
                        title='Prediction Distribution',
                        color_discrete_sequence=['#ff6b6b', '#4ecdc4'])
            st.plotly_chart(fig, use_container_width=True)
        
        # Display history table
        st.markdown("### 📊 Prediction Details")
        st.dataframe(history_df, use_container_width=True)
        
        # Download button
        csv = history_df.to_csv(index=False)
        st.download_button(
            label="📥 Download Prediction History",
            data=csv,
            file_name=f"prediction_history_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    else:
        st.info("No predictions made yet. Go to the Prediction page to make your first prediction!")


def about_page():
    """About Project Page"""
    st.markdown('<h1 class="main-header">ℹ️ About Project</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Customer Churn Prediction & Business Intelligence Dashboard
    
    ### 🎯 Project Objective
    Develop a production-ready end-to-end machine learning system that predicts customer churn 
    and provides actionable business intelligence insights.
    
    ### 🏗️ Architecture
    ```
    ├── Data Ingestion → Data Validation → Data Transformation
    ├── Model Training → Model Selection → Model Evaluation
    └── Prediction Pipeline → Web Application → Dashboard
    ```
    
    ### 🔬 Machine Learning Pipeline
    
    #### 1. Data Ingestion
    - Reads raw customer data
    - Stratified train-test split (80-20)
    - Preserves data integrity
    
    #### 2. Data Validation
    - Schema validation
    - Missing value detection
    - Duplicate record identification
    - Data type verification
    
    #### 3. Data Transformation
    - Feature engineering (tenure groups, service aggregation)
    - Label encoding for categorical features
    - Standard scaling for numerical features
    - Missing value imputation
    
    #### 4. Model Training
    - **Models Evaluated:**
        - Logistic Regression
        - Decision Tree
        - Random Forest
        - Gradient Boosting
        - XGBoost
    - GridSearchCV for hyperparameter tuning
    - ROC AUC based model selection
    
    #### 5. Model Evaluation
    - Accuracy, Precision, Recall, F1-Score
    - ROC AUC Score
    - Confusion Matrix
    - Feature Importance Analysis
    
    ### 🛠️ Tech Stack
    - **Language:** Python 3.8+
    - **ML Libraries:** Scikit-learn, XGBoost
    - **Data Processing:** Pandas, NumPy
    - **Visualization:** Matplotlib, Seaborn, Plotly
    - **Web Framework:** Streamlit
    - **Configuration:** YAML
    - **Serialization:** Joblib
    - **Logging:** Python logging module
    
    ### 📊 Key Features
    - ✅ Modular and reusable code
    - ✅ Comprehensive logging and exception handling
    - ✅ Configuration-driven architecture
    - ✅ Production-ready code structure
    - ✅ Interactive web dashboard
    - ✅ Real-time predictions
    - ✅ Model performance visualization
    - ✅ Prediction history tracking
    - ✅ Business recommendations
    
    ### 👨‍💻 Developer
    **ML Engineer Portfolio Project**
    
    ### 📝 License
    This project is open source and available for educational purposes.
    
    ---
    
    ### 🚀 Future Enhancements
    - Deploy on cloud (AWS/Azure/GCP)
    - REST API development
    - Real-time monitoring dashboard
    - A/B testing framework
    - Model retraining automation
    - Integration with CRM systems
    """)


def main():
    """Main Application"""
    
    # Sidebar
    st.sidebar.title("🎯 Navigation")
    
    page = st.sidebar.radio(
        "Go to",
        ["🏠 Home", "🔮 Customer Prediction", "📈 Model Performance", 
         "📜 Prediction History", "ℹ️ About Project"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Project Info")
    st.sidebar.info("""
    **Customer Churn Prediction**
    
    Version: 1.0.0
    
    ML-powered system for predicting customer churn and retention
    """)
    
    # Route to pages
    if page == "🏠 Home":
        home_page()
    elif page == "🔮 Customer Prediction":
        prediction_page()
    elif page == "📈 Model Performance":
        model_performance_page()
    elif page == "📜 Prediction History":
        prediction_history_page()
    elif page == "ℹ️ About Project":
        about_page()
    
    # Footer with signature
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 2rem; color: #666;'>
        <p style='font-size: 1.1rem; font-weight: 500;'>
            Created with ❤️ by <span style='color: #667eea; font-weight: bold;'>Divya Sri Doredla</span>
        </p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
