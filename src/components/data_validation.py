"""
Data Validation Component
Validates data quality and schema
"""
import os
import sys
import pandas as pd
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import load_config, save_json


@dataclass
class DataValidationConfig:
    """Configuration for Data Validation"""
    validation_report_path: str = "artifacts/validation_report.json"


class DataValidation:
    """Data Validation Class"""
    
    def __init__(self):
        """Initialize Data Validation"""
        self.config = DataValidationConfig()
        logging.info("Data Validation configuration initialized")
    
    def validate_data(self, train_path, test_path):
        """
        Validate train and test datasets
        
        Args:
            train_path: Path to training data
            test_path: Path to test data
            
        Returns:
            dict: Validation report
        """
        logging.info("Starting data validation process")
        
        try:
            # Read data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            config = load_config()
            expected_columns = (
                [config['preprocessing']['id_column']] +
                config['preprocessing']['numerical_features'] +
                config['preprocessing']['categorical_features'] +
                [config['preprocessing']['target_column']]
            )
            
            validation_report = {
                'train_data': {},
                'test_data': {},
                'validation_status': 'PASSED'
            }
            
            # Validate train data
            logging.info("Validating training data")
            validation_report['train_data'] = self._validate_dataset(
                train_df, expected_columns, "Training"
            )
            
            # Validate test data
            logging.info("Validating test data")
            validation_report['test_data'] = self._validate_dataset(
                test_df, expected_columns, "Test"
            )
            
            # Check if validation failed
            if (validation_report['train_data']['missing_columns'] or 
                validation_report['test_data']['missing_columns']):
                validation_report['validation_status'] = 'FAILED'
            
            # Save validation report
            save_json(self.config.validation_report_path, validation_report)
            
            logging.info(f"Data validation completed: {validation_report['validation_status']}")
            return validation_report
            
        except Exception as e:
            raise CustomException(e, sys)
    
    def _validate_dataset(self, df, expected_columns, dataset_name):
        """Validate individual dataset"""
        report = {
            'shape': list(df.shape),
            'missing_values': df.isnull().sum().to_dict(),
            'duplicate_records': int(df.duplicated().sum()),
            'data_types': df.dtypes.astype(str).to_dict(),
            'missing_columns': []
        }
        
        # Check for missing columns
        missing_cols = set(expected_columns) - set(df.columns)
        if missing_cols:
            report['missing_columns'] = list(missing_cols)
            logging.warning(f"{dataset_name} data missing columns: {missing_cols}")
        
        # Log statistics
        total_missing = df.isnull().sum().sum()
        logging.info(f"{dataset_name} - Total missing values: {total_missing}")
        logging.info(f"{dataset_name} - Duplicate records: {report['duplicate_records']}")
        
        return report
