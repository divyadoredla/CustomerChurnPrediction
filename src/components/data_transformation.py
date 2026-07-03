"""
Data Transformation Component
Handles feature engineering and preprocessing
"""
import os
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import load_config, save_object


@dataclass
class DataTransformationConfig:
    """Configuration for Data Transformation"""
    preprocessor_path: str


class DataTransformation:
    """Data Transformation Class"""
    
    def __init__(self):
        """Initialize Data Transformation with configuration"""
        try:
            config = load_config()
            self.config = DataTransformationConfig(
                preprocessor_path=config['paths']['preprocessor_path']
            )
            self.preprocessing_config = config['preprocessing']
            logging.info("Data Transformation configuration initialized")
            
        except Exception as e:
            raise CustomException(e, sys)
    
    def get_preprocessor_object(self):
        """
        Create preprocessing pipeline
        
        Returns:
            ColumnTransformer: Preprocessing pipeline
        """
        try:
            logging.info("Creating preprocessing pipeline")
            
            numerical_features = self.preprocessing_config['numerical_features']
            
            # Numerical pipeline
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )
            
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', num_pipeline, numerical_features)
                ]
            )
            
            logging.info("Preprocessing pipeline created successfully")
            return preprocessor
            
        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_transformation(self, train_path, test_path):
        """
        Apply transformations to train and test data
        
        Args:
            train_path: Path to training data
            test_path: Path to test data
            
        Returns:
            tuple: Transformed train array, test array, preprocessor path
        """
        logging.info("Starting data transformation process")
        
        try:
            # Read data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info(f"Train data shape before transformation: {train_df.shape}")
            logging.info(f"Test data shape before transformation: {test_df.shape}")
            
            # Separate features and target
            target_column = self.preprocessing_config['target_column']
            id_column = self.preprocessing_config['id_column']
            
            # Drop ID column
            train_df = train_df.drop(columns=[id_column])
            test_df = test_df.drop(columns=[id_column])
            
            # Handle TotalCharges conversion
            train_df['TotalCharges'] = pd.to_numeric(train_df['TotalCharges'], errors='coerce')
            test_df['TotalCharges'] = pd.to_numeric(test_df['TotalCharges'], errors='coerce')
            
            # Feature Engineering
            logging.info("Applying feature engineering")
            train_df = self._feature_engineering(train_df)
            test_df = self._feature_engineering(test_df)
            
            # Encode categorical features
            logging.info("Encoding categorical features")
            categorical_features = self.preprocessing_config['categorical_features']
            
            label_encoders = {}
            for col in categorical_features:
                le = LabelEncoder()
                train_df[col] = le.fit_transform(train_df[col].astype(str))
                test_df[col] = le.transform(test_df[col].astype(str))
                label_encoders[col] = le
            
            # Separate features and target
            X_train = train_df.drop(columns=[target_column])
            y_train = train_df[target_column]
            
            X_test = test_df.drop(columns=[target_column])
            y_test = test_df[target_column]
            
            # Encode target variable for XGBoost compatibility
            target_encoder = LabelEncoder()
            y_train_encoded = target_encoder.fit_transform(y_train)
            y_test_encoded = target_encoder.transform(y_test)
            
            # Get preprocessor
            preprocessor = self.get_preprocessor_object()
            
            # Fit and transform
            logging.info("Fitting preprocessor on training data")
            X_train_transformed = preprocessor.fit_transform(X_train)
            X_test_transformed = preprocessor.transform(X_test)
            
            # Combine all features
            numerical_features = self.preprocessing_config['numerical_features']
            all_features = numerical_features + categorical_features
            
            # Create final arrays
            X_train_final = np.c_[
                X_train_transformed,
                X_train[categorical_features].values
            ]
            
            X_test_final = np.c_[
                X_test_transformed,
                X_test[categorical_features].values
            ]
            
            # Save preprocessor
            save_object(self.config.preprocessor_path, {
                'preprocessor': preprocessor,
                'label_encoders': label_encoders,
                'target_encoder': target_encoder,
                'feature_names': all_features
            })
            
            logging.info(f"Train data shape after transformation: {X_train_final.shape}")
            logging.info(f"Test data shape after transformation: {X_test_final.shape}")
            logging.info("Data transformation completed successfully")
            
            return (
                X_train_final,
                y_train_encoded,
                X_test_final,
                y_test_encoded,
                self.config.preprocessor_path
            )
            
        except Exception as e:
            raise CustomException(e, sys)
    
    def _feature_engineering(self, df):
        """Apply feature engineering"""
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
