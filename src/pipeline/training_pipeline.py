"""
Training Pipeline
Orchestrates the complete ML training workflow
"""
import sys

from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation


class TrainingPipeline:
    """Complete ML Training Pipeline"""
    
    def __init__(self):
        """Initialize Training Pipeline"""
        logging.info("="*70)
        logging.info("CUSTOMER CHURN PREDICTION - TRAINING PIPELINE STARTED")
        logging.info("="*70)
    
    def run_pipeline(self):
        """Execute the complete training pipeline"""
        try:
            # Step 1: Data Ingestion
            logging.info("\n" + "="*70)
            logging.info("STEP 1: DATA INGESTION")
            logging.info("="*70)
            data_ingestion = DataIngestion()
            train_path, test_path = data_ingestion.initiate_data_ingestion()
            
            # Step 2: Data Validation
            logging.info("\n" + "="*70)
            logging.info("STEP 2: DATA VALIDATION")
            logging.info("="*70)
            data_validation = DataValidation()
            validation_report = data_validation.validate_data(train_path, test_path)
            
            if validation_report['validation_status'] == 'FAILED':
                raise Exception("Data validation failed. Please check validation report.")
            
            # Step 3: Data Transformation
            logging.info("\n" + "="*70)
            logging.info("STEP 3: DATA TRANSFORMATION")
            logging.info("="*70)
            data_transformation = DataTransformation()
            X_train, y_train, X_test, y_test, preprocessor_path = \
                data_transformation.initiate_data_transformation(train_path, test_path)
            
            # Step 4: Model Training
            logging.info("\n" + "="*70)
            logging.info("STEP 4: MODEL TRAINING")
            logging.info("="*70)
            model_trainer = ModelTrainer()
            model_path, comparison_report = model_trainer.initiate_model_training(
                X_train, y_train, X_test, y_test
            )
            
            # Step 5: Model Evaluation
            logging.info("\n" + "="*70)
            logging.info("STEP 5: MODEL EVALUATION")
            logging.info("="*70)
            model_evaluation = ModelEvaluation()
            metrics = model_evaluation.evaluate_best_model(
                model_path, X_test, y_test
            )
            
            # Pipeline Summary
            logging.info("\n" + "="*70)
            logging.info("TRAINING PIPELINE COMPLETED SUCCESSFULLY")
            logging.info("="*70)
            logging.info(f"Best Model: {comparison_report['best_model']}")
            logging.info(f"ROC AUC Score: {comparison_report['best_score']:.4f}")
            logging.info(f"Model saved at: {model_path}")
            logging.info(f"Preprocessor saved at: {preprocessor_path}")
            logging.info("="*70)
            
            return {
                'model_path': model_path,
                'preprocessor_path': preprocessor_path,
                'best_model': comparison_report['best_model'],
                'best_score': comparison_report['best_score'],
                'metrics': metrics
            }
            
        except Exception as e:
            logging.error("Training pipeline failed")
            raise CustomException(e, sys)


if __name__ == "__main__":
    pipeline = TrainingPipeline()
    pipeline.run_pipeline()
