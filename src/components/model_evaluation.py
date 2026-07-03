"""
Model Evaluation Component
Generates detailed evaluation metrics and visualizations
"""
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, auc
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import load_object, evaluate_model, save_json


@dataclass
class ModelEvaluationConfig:
    """Configuration for Model Evaluation"""
    metrics_path: str = "artifacts/evaluation_metrics.json"
    plots_dir: str = "artifacts/plots"


class ModelEvaluation:
    """Model Evaluation Class"""
    
    def __init__(self):
        """Initialize Model Evaluation"""
        self.config = ModelEvaluationConfig()
        os.makedirs(self.config.plots_dir, exist_ok=True)
        logging.info("Model Evaluation configuration initialized")
    
    def evaluate_best_model(self, model_path, X_test, y_test, feature_names=None):
        """
        Evaluate the best model and generate comprehensive reports
        
        Args:
            model_path: Path to the saved model
            X_test: Test features
            y_test: Test labels
            feature_names: List of feature names
            
        Returns:
            dict: Evaluation metrics
        """
        logging.info("Starting model evaluation")
        
        try:
            # Load model
            model = load_object(model_path)
            
            # Make predictions
            y_pred = model.predict(X_test)
            y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
            
            # Get metrics
            metrics = evaluate_model(y_test, y_pred, y_pred_proba)
            
            # Generate visualizations
            logging.info("Generating evaluation visualizations")
            self._plot_confusion_matrix(metrics['confusion_matrix'])
            
            if y_pred_proba is not None:
                self._plot_roc_curve(y_test, y_pred_proba, metrics.get('roc_auc'))
            
            # Feature importance
            if hasattr(model, 'feature_importances_'):
                self._plot_feature_importance(model, feature_names)
                metrics['feature_importance'] = dict(zip(
                    feature_names if feature_names else [f'feature_{i}' for i in range(X_test.shape[1])],
                    model.feature_importances_.tolist()
                ))
            
            # Save metrics
            save_json(self.config.metrics_path, metrics)
            
            logging.info(f"Model Evaluation completed")
            logging.info(f"Accuracy: {metrics['accuracy']:.4f}")
            logging.info(f"ROC AUC: {metrics.get('roc_auc', 'N/A')}")
            
            return metrics
            
        except Exception as e:
            raise CustomException(e, sys)
    
    def _plot_confusion_matrix(self, cm):
        """Plot confusion matrix"""
        try:
            plt.figure(figsize=(8, 6))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
            plt.title('Confusion Matrix', fontsize=16, fontweight='bold')
            plt.ylabel('Actual', fontsize=12)
            plt.xlabel('Predicted', fontsize=12)
            plt.tight_layout()
            plt.savefig(os.path.join(self.config.plots_dir, 'confusion_matrix.png'), dpi=300)
            plt.close()
            logging.info("Confusion matrix plot saved")
            
        except Exception as e:
            logging.error(f"Error plotting confusion matrix: {str(e)}")
    
    def _plot_roc_curve(self, y_true, y_pred_proba, roc_auc_score):
        """Plot ROC curve"""
        try:
            fpr, tpr, _ = roc_curve(y_true, y_pred_proba, pos_label='Yes')
            
            plt.figure(figsize=(8, 6))
            plt.plot(fpr, tpr, color='darkorange', lw=2, 
                    label=f'ROC curve (AUC = {roc_auc_score:.4f})')
            plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Rate', fontsize=12)
            plt.ylabel('True Positive Rate', fontsize=12)
            plt.title('ROC Curve', fontsize=16, fontweight='bold')
            plt.legend(loc="lower right")
            plt.grid(alpha=0.3)
            plt.tight_layout()
            plt.savefig(os.path.join(self.config.plots_dir, 'roc_curve.png'), dpi=300)
            plt.close()
            logging.info("ROC curve plot saved")
            
        except Exception as e:
            logging.error(f"Error plotting ROC curve: {str(e)}")
    
    def _plot_feature_importance(self, model, feature_names):
        """Plot feature importance"""
        try:
            if feature_names is None:
                feature_names = [f'Feature {i}' for i in range(len(model.feature_importances_))]
            
            importance_df = pd.DataFrame({
                'Feature': feature_names,
                'Importance': model.feature_importances_
            }).sort_values('Importance', ascending=False).head(15)
            
            plt.figure(figsize=(10, 8))
            sns.barplot(data=importance_df, x='Importance', y='Feature', palette='viridis')
            plt.title('Top 15 Feature Importances', fontsize=16, fontweight='bold')
            plt.xlabel('Importance', fontsize=12)
            plt.ylabel('Features', fontsize=12)
            plt.tight_layout()
            plt.savefig(os.path.join(self.config.plots_dir, 'feature_importance.png'), dpi=300)
            plt.close()
            logging.info("Feature importance plot saved")
            
        except Exception as e:
            logging.error(f"Error plotting feature importance: {str(e)}")
