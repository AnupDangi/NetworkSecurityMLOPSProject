from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys
from networksecurity.logging.logger import logging
from networksecurity.components.validation_config import DataValidation

if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.info("Exporting collection data as dataframe")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(data_ingestion_artifact=dataingestionartifact,data_validation_config=data_validation_config)
        logging.info("Starting data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info("Data validation completed")

    except Exception as e:
        raise NetworkSecurityException(e,sys)


