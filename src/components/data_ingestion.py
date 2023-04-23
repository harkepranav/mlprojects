# Read the file from datastream
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation, DataTransformationConfig


@dataclass
class DataIngestionConfig:
    # Trained data will be stored in this path
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered in the data ingestion method or component")
        try:
            df = pd.read_csv(r'C:\Users\EL-Dorado\Downloads\Data Science & ML\Projects\mlprojects\notebook\data\StudentsPerformance.csv')
            logging.info('Read the dataset as dataframe')
            # Create data path and make directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)  # Saved train file
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)  # Saved test file

            logging.info('Data Ingestion has been completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.error(f"Exception occurred during data ingestion: {e}")
            raise CustomException("Failed to ingest data", str(e))


if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data_path, test_data_path)
