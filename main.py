from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys
from networksecurity.logging.logger import logging

if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        data_ingestion=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(data_ingestion_config=data_ingestion)
        logging.info("Exporting collection data as dataframe")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)


