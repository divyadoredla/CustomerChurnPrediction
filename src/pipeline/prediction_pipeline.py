"""
Prediction Pipeline
Handles predictions for new customer data
"""
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import load_object, load_config


@dataclass
class PredictionPipelineConfig:
    """Configuration for Prediction Pipeline"""
    model_path: str = "artifacts/models/best_model.pkl"
    preprocessor_path: str = "artifacts/preprocessor.pkl"


class CustomData:
    """Class for handling custom input data"""
    
    def __init__(self,
                 gender: str,
                 SeniorCitizen: int,
                 Partner: str,
                 Dependents: str,
                 tenure: int,
                 PhoneService: str,
                 MultipleLines: str,
                 InternetService: str,
                 OnlineSecurity: str,
                 OnlineBackup: str,
                 DeviceProtection: str,
                 TechSupport: str,
                 StreamingTV: str,
                 StreamingMovies: str,
                 Contract: str,
                 PaperlessBilling: str,
                 PaymentMethod: str,
                 MonthlyCharges: float,
                 TotalCharges: float):
        
        self.gender = gender
        self.SeniorCitizen = SeniorCitizen
        self.Partner = Partner
        self.Dependents = Dependents
        self.tenure = tenure
        self.PhoneService = PhoneService
        self.MultipleLines = MultipleLines
        self.InternetService = InternetService
        self.OnlineSecurity = OnlineSecurity
        self.OnlineBackup = OnlineBackup
        self.DeviceProtection = DeviceProtection
        self.TechSupport = TechSupport
        self.StreamingTV = StreamingTV
        self.StreamingMovies = StreamingMovies
        self.Contract = Contract
        self.PaperlessBilling = PaperlessBilling
        self.PaymentMethod = PaymentMethod
        self.MonthlyCharges = MonthlyCharges
        self.TotalCharges = TotalCharges
    
    def get_data_as_dataframe(self):
        """Convert input data to DataFrame"""
        try:
            data_dict = {
                'gender': [self.gender],
                'SeniorCitizen': [self.SeniorCitizen],
                'Partner': [self.Partner],
                'Dependents': [self.Dependents],
                'tenure': [self.tenure],
                'PhoneService': [self.PhoneService],
                'MultipleLines': [self.MultipleLines],
                'InternetService': [self.InternetService],
                'OnlineSecurity': [self.OnlineSecurity],
                'OnlineBackup': [self.OnlineBackup],
                'DeviceProtection': [self.DeviceProtection],
                'TechSupport': [self.TechSupport],
                'StreamingTV': [self.StreamingTV],
                'StreamingMovies': [self.StreamingMovies],
                'Contract': [self.Contract],
                'PaperlessBilling': [self.PaperlessBilling],
                'PaymentMethod': [self.PaymentMethod],
                'MonthlyCharges': [self.MonthlyCharges],
                'TotalCharges': [self.TotalCharges]
            }
            
            return pd.DataFrame(data_dict)
            
        except Exception as e:
            raise CustomException(e, sys)


class PredictionPipeline:
    """Pipeline for making predictions"""
    
    def __init__(self):
        """Initialize Prediction Pipeline"""
        self.config = PredictionPipelineConfig()
    
    def predict(self, features_df):
        """
        Make prediction on input features
        
        Args:
            features_df: Input features as DataFrame
            
        Returns:
            dict: Prediction results with probability and confidence
        """
        try:
            logging.info("Starting prediction process")
            
            # Load model and preprocessor
            model = load_object(self.config.model_path)
            preprocessor_obj = load_object(self.config.preprocessor_path)
            
            preprocessor = preprocessor_obj['preprocessor']
            label_encoders = preprocessor_obj['label_encoders']
            target_encoder = preprocessor_obj.get('target_encoder', None)
            
            # Feature engineering
            features_df = self._apply_feature_engineering(features_df)
            
            # Encode categorical features
            config = load_config()
            categorical_features = config['preprocessing']['categorical_features']
            
            for col in categorical_features:
                if col in label_encoders:
                    features_df[col] = label_encoders[col].transform(features_df[col].astype(str))
            
            # Prepare features
            numerical_features = config['preprocessing']['numerical_features']
            
            # Transform numerical features
            X_transformed = preprocessor.transform(features_df)
            
            # Combine with categorical
            X_final = np.c_[
                X_transformed,
                features_df[categorical_features].values
            ]
            
            # Make prediction
            prediction_numeric = model.predict(X_final)[0]
            probability = model.predict_proba(X_final)
            
            # Handle both numeric and string predictions
            if target_encoder is not None:
                # XGBoost or other models using numeric labels
                prediction = target_encoder.inverse_transform([prediction_numeric])[0]
                churn_prob = probability[0][1]
            else:
                # Models using string labels directly
                prediction = prediction_numeric
                churn_prob = probability[0][1] if prediction == 1 or prediction == 'Yes' else probability[0][0]
            
            # Calculate confidence (distance from 0.5 threshold)
            confidence = abs(churn_prob - 0.5) * 2 * 100
            
            result = {
                'prediction': 'Yes' if (prediction == 1 or prediction == 'Yes') else 'No',
                'churn_probability': round(churn_prob * 100, 2),
                'retention_probability': round((1 - churn_prob) * 100, 2),
                'confidence': round(confidence, 2),
                'risk_level': self._get_risk_level(churn_prob)
            }
            
            logging.info(f"Prediction completed: {result}")
            return result
            
        except Exception as e:
            raise CustomException(e, sys)
    
    def _apply_feature_engineering(self, df):
        """Apply same feature engineering as training"""
        try:
            # Tenure groups
            df['tenure_group'] = pd.cut(
                df['tenure'], 
                bins=[0, 12, 24, 48, 72], 
                labels=['0-1 year', '1-2 years', '2-4 years', '4-6 years']
            )
            
            # Monthly charges group
            df['charges_group'] = pd.cut(
                df['MonthlyCharges'],
                bins=[0, 35, 70, 105, 150],
                labels=['Low', 'Medium', 'High', 'Very High']
            )
            
            # Total services
            service_cols = ['PhoneService', 'InternetService', 'OnlineSecurity', 
                          'OnlineBackup', 'DeviceProtection', 'TechSupport',
                          'StreamingTV', 'StreamingMovies']
            
            df['total_services'] = df[service_cols].apply(
                lambda x: sum([1 for val in x if val not in ['No', 'No internet service', 'No phone service']]), 
                axis=1
            )
            
            return df
            
        except Exception as e:
            raise CustomException(e, sys)
    
    def _get_risk_level(self, probability):
        """Determine risk level based on probability"""
        if probability >= 0.7:
            return 'High Risk'
        elif probability >= 0.5:
            return 'Medium Risk'
        elif probability >= 0.3:
            return 'Low Risk'
        else:
            return 'Very Low Risk'
