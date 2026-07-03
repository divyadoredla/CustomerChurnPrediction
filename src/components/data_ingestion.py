"""
Data Ingestion Component
Handles reading data and splitting into train/test sets
"""
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import load_config


@dataclass
class DataIngestionConfig:
    """Configuration for Data Ingestion"""
    raw_data_path: str
    train_data_path: str
    test_data_path: str
    test_size: float
    random_state: int


class DataIngestion:
    """Data Ingestion Class"""
    
    def __init__(self):
        """Initialize Data Ingestion with configuration"""
        try:
            config = load_config()
            self.config = DataIngestionConfig(
                raw_data_path=config['data']['raw_data_path'],
                train_data_path=config['data']['train_data_path'],
                test_data_path=config['data']['test_data_path'],
                test_size=config['data']['test_size'],
                random_state=config['data']['random_state']
            )
            logging.info("Data Ingestion configuration initialized")
            
        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_ingestion(self):
        """
        Read data and split into train/test
        
        Returns:
            tuple: Paths to train and test datasets
        """
        logging.info("Starting data ingestion process")
        
        try:
            # Read dataset
            logging.info(f"Reading data from {self.config.raw_data_path}")
            df = pd.read_csv(self.config.raw_data_path)
            
            logging.info(f"Dataset shape: {df.shape}")
            logging.info(f"Dataset columns: {df.columns.tolist()}")
            
            # Create artifacts directory
            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)
            
            # Split data
            logging.info("Splitting data into train and test sets")
            train_set, test_set = train_test_split(
                df, 
                test_size=self.config.test_size, 
                random_state=self.config.random_state,
                stratify=df['Churn']
            )
            
            # Save train and test data
            train_set.to_csv(self.config.train_data_path, index=False, header=True)
            test_set.to_csv(self.config.test_data_path, index=False, header=True)
            
            logging.info(f"Train set shape: {train_set.shape}")
            logging.info(f"Test set shape: {test_set.shape}")
            logging.info("Data ingestion completed successfully")
            
            return (
                self.config.train_data_path,
                self.config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e, sys)
