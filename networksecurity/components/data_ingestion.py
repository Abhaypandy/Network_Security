import os
import sys
import numpy as np
import pandas as pd
import pymongo
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv

from networksecurity.exception.exception import networksecurityexception
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise networksecurityexception(e, sys)

    def export_collection_as_dataframe(self):
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name

            mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            
            collection = mongo_client[database_name][collection_name]


            df = pd.DataFrame(list(collection.find()))

            if df.empty:
                raise Exception("No data found in MongoDB collection")

            if "_id" in df.columns:
                df.drop(columns=["_id"], inplace=True)

            df.replace({"na": np.nan}, inplace=True)

            return df

        except Exception as e:
            raise networksecurityexception(e, sys)

    def export_data_into_feature_store(self, dataframe: pd.DataFrame):
        try:
            file_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            dataframe.to_csv(file_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise networksecurityexception(e, sys)

    
    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)

            return DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )

        except Exception as e:
            raise networksecurityexception(e, sys)
        
    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        try:
            train_set, test_set = train_test_split(
            dataframe,
            test_size=self.data_ingestion_config.train_test_split_ratio
        )

            logging.info("Performed train test split on the dataframe")

            dir_path = os.path.dirname(
            self.data_ingestion_config.training_file_path
        )

            os.makedirs(dir_path, exist_ok=True)

            logging.info("Exporting train and test file path.")

            train_set.to_csv(
            self.data_ingestion_config.training_file_path,
            index=False,
            header=True
        )

            test_set.to_csv(
            self.data_ingestion_config.testing_file_path,
            index=False,
            header=True
        )

            logging.info("Exported train and test file path.")

            logging.info(
            "Exited split_data_as_train_test method of Data_Ingestion class"
        )

        except Exception as e:
            raise networksecurityexception(e, sys)