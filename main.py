"""
Main Script to Execute Training Pipeline
"""
from src.pipeline.training_pipeline import TrainingPipeline
from src.logger import logging


def main():
    """Execute the complete ML pipeline"""
    try:
        # Initialize and run training pipeline
        pipeline = TrainingPipeline()
        results = pipeline.run_pipeline()
        
        print("\n" + "="*70)
        print("TRAINING PIPELINE EXECUTION SUMMARY")
        print("="*70)
        print(f"Best Model: {results['best_model']}")
        print(f"ROC AUC Score: {results['best_score']:.4f}")
        print(f"Accuracy: {results['metrics']['accuracy']:.4f}")
        print(f"Precision: {results['metrics']['precision']:.4f}")
        print(f"Recall: {results['metrics']['recall']:.4f}")
        print(f"F1 Score: {results['metrics']['f1_score']:.4f}")
        print("="*70)
        print("\nArtifacts saved in 'artifacts/' directory")
        print("Logs saved in 'logs/' directory")
        print("="*70)
        
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")
        raise


if __name__ == "__main__":
    main()
