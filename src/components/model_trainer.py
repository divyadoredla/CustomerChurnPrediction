"""
Model Training Component
Trains multiple models, performs hyperparameter tuning, and selects best model
"""
import os
import sys
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import load_config, save_object, train_model_with_cv, evaluate_model, save_json


@dataclass
class ModelTrainerConfig:
    """Configuration for Model Training"""
    best_model_path: str
    models_dir: str


class ModelTrainer:
    """Model Training Class"""
    
    def __init__(self):
        """Initialize Model Trainer"""
        try:
            config = load_config()
            self.config = ModelTrainerConfig(
                best_model_path=config['paths']['best_model_path'],
                models_dir=config['paths']['models_dir']
            )
            self.model_config = config['model_training']
            os.makedirs(self.config.models_dir, exist_ok=True)
            logging.info("Model Trainer configuration initialized")
            
        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_model_training(self, X_train, y_train, X_test, y_test):
        """
        Train multiple models and select the best one
        
        Args:
            X_train: Training features
            y_train: Training labels
            X_test: Test features
            y_test: Test labels
            
        Returns:
            tuple: Best model path and comparison report
        """
        logging.info("Starting model training process")
        
        try:
            # Define models
            models = {
                'Logistic Regression': LogisticRegression(),
                'Decision Tree': DecisionTreeClassifier(),
                'Random Forest': RandomForestClassifier(),
                'Gradient Boosting': GradientBoostingClassifier(),
                'XGBoost': XGBClassifier(eval_metric='logloss')
            }
            
            # Define parameter grids
            param_grids = {
                'Logistic Regression': self.model_config['models']['logistic_regression']['params'],
                'Decision Tree': self.model_config['models']['decision_tree']['params'],
                'Random Forest': self.model_config['models']['random_forest']['params'],
                'Gradient Boosting': self.model_config['models']['gradient_boosting']['params'],
                'XGBoost': self.model_config['models']['xgboost']['params']
            }
            
            # Train and evaluate all models
            model_report = {}
            trained_models = {}
            
            for model_name, model in models.items():
                logging.info(f"\n{'='*50}")
                logging.info(f"Training {model_name}")
                logging.info(f"{'='*50}")
                
                try:
                    # Train with GridSearchCV
                    best_model = train_model_with_cv(
                        model=model,
                        param_grid=param_grids[model_name],
                        X_train=X_train,
                        y_train=y_train,
                        cv=5
                    )
                    
                    # Make predictions
                    y_train_pred = best_model.predict(X_train)
                    y_test_pred = best_model.predict(X_test)
                    
                    # Get probability predictions if available
                    if hasattr(best_model, 'predict_proba'):
                        y_test_proba = best_model.predict_proba(X_test)[:, 1]
                    else:
                        y_test_proba = None
                    
                    # Evaluate
                    train_metrics = evaluate_model(y_train, y_train_pred)
                    test_metrics = evaluate_model(y_test, y_test_pred, y_test_proba)
                    
                    # Store results
                    model_report[model_name] = {
                        'train_accuracy': train_metrics['accuracy'],
                        'test_accuracy': test_metrics['accuracy'],
                        'test_precision': test_metrics['precision'],
                        'test_recall': test_metrics['recall'],
                        'test_f1_score': test_metrics['f1_score'],
                        'test_roc_auc': test_metrics.get('roc_auc', None)
                    }
                    
                    trained_models[model_name] = best_model
                    
                    logging.info(f"{model_name} - Test Accuracy: {test_metrics['accuracy']:.4f}")
                    logging.info(f"{model_name} - Test ROC AUC: {test_metrics.get('roc_auc', 'N/A')}")
                    
                except Exception as e:
                    logging.error(f"Error training {model_name}: {str(e)}")
                    continue
            
            # Select best model based on Accuracy
            logging.info("\n" + "="*50)
            logging.info("MODEL COMPARISON REPORT")
            logging.info("="*50)
            
            comparison_df = pd.DataFrame(model_report).T
            logging.info(f"\n{comparison_df.to_string()}")
            
            # Find best model by accuracy
            best_model_name = comparison_df['test_accuracy'].idxmax()
            best_model = trained_models[best_model_name]
            best_score = comparison_df.loc[best_model_name, 'test_accuracy']
            
            logging.info(f"\nBest Model: {best_model_name}")
            logging.info(f"Best Accuracy Score: {best_score:.4f}")
            
            # Save best model
            save_object(self.config.best_model_path, best_model)
            
            # Save comparison report
            comparison_report = {
                'best_model': best_model_name,
                'best_score': float(best_score),
                'selection_metric': 'accuracy',
                'all_models': {k: {key: float(val) if val is not None else None 
                              for key, val in v.items()} 
                              for k, v in model_report.items()}
            }
            
            save_json('artifacts/model_comparison.json', comparison_report)
            
            logging.info("Model training completed successfully")
            
            return self.config.best_model_path, comparison_report
            
        except Exception as e:
            raise CustomException(e, sys)
