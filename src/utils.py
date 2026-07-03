"""
Utility functions for the project
"""
import os
import sys
import yaml
import joblib
import json
import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, 
    f1_score, roc_auc_score, confusion_matrix, 
    classification_report, roc_curve
)
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException
from src.logger import logging


def load_config(config_path="config/config.yaml"):
    """Load configuration from YAML file"""
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        logging.info(f"Configuration loaded successfully from {config_path}")
        return config
    except Exception as e:
        raise CustomException(e, sys)


def save_object(file_path, obj):
    """Save Python object using joblib"""
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        joblib.dump(obj, file_path)
        logging.info(f"Object saved successfully at {file_path}")
        
    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    """Load Python object using joblib"""
    try:
        if not os.path.exists(file_path):
            raise Exception(f"File not found: {file_path}")
            
        obj = joblib.load(file_path)
        logging.info(f"Object loaded successfully from {file_path}")
        return obj
        
    except Exception as e:
        raise CustomException(e, sys)


def save_json(file_path, data):
    """Save data as JSON"""
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        logging.info(f"JSON saved successfully at {file_path}")
        
    except Exception as e:
        raise CustomException(e, sys)


def evaluate_model(y_true, y_pred, y_pred_proba=None):
    """
    Evaluate model performance
    
    Args:
        y_true: True labels (can be numeric or string)
        y_pred: Predicted labels (can be numeric or string)
        y_pred_proba: Predicted probabilities (optional)
        
    Returns:
        dict: Dictionary containing all metrics
    """
    try:
        # Handle both numeric and string labels
        if isinstance(y_true[0], (int, np.integer)):
            pos_label = 1
        else:
            pos_label = 'Yes'
        
        metrics = {
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred, pos_label=pos_label, zero_division=0),
            'recall': recall_score(y_true, y_pred, pos_label=pos_label, zero_division=0),
            'f1_score': f1_score(y_true, y_pred, pos_label=pos_label, zero_division=0),
        }
        
        if y_pred_proba is not None:
            # For binary classification with numeric labels
            if isinstance(y_true[0], (int, np.integer)):
                metrics['roc_auc'] = roc_auc_score(y_true, y_pred_proba)
            else:
                # Convert string labels to numeric for ROC AUC
                y_true_numeric = [1 if y == 'Yes' else 0 for y in y_true]
                metrics['roc_auc'] = roc_auc_score(y_true_numeric, y_pred_proba)
        
        metrics['confusion_matrix'] = confusion_matrix(y_true, y_pred).tolist()
        metrics['classification_report'] = classification_report(y_true, y_pred, zero_division=0)
        
        logging.info(f"Model evaluation completed: Accuracy={metrics['accuracy']:.4f}")
        return metrics
        
    except Exception as e:
        raise CustomException(e, sys)


def train_model_with_cv(model, param_grid, X_train, y_train, cv=5):
    """
    Train model with GridSearchCV
    
    Args:
        model: ML model
        param_grid: Parameters for grid search
        X_train: Training features
        y_train: Training labels
        cv: Number of cross-validation folds
        
    Returns:
        Best estimator from grid search
    """
    try:
        logging.info(f"Starting GridSearchCV for {model.__class__.__name__}")
        
        grid_search = GridSearchCV(
            estimator=model,
            param_grid=param_grid,
            cv=cv,
            scoring='roc_auc',
            n_jobs=-1,
            verbose=1
        )
        
        grid_search.fit(X_train, y_train)
        
        logging.info(f"Best parameters: {grid_search.best_params_}")
        logging.info(f"Best score: {grid_search.best_score_:.4f}")
        
        return grid_search.best_estimator_
        
    except Exception as e:
        raise CustomException(e, sys)
