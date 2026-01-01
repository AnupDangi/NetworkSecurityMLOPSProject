import sys
import os
import numpy 
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.constant.training_pipeline import DATA_TRANSFOMATION_IMPUTER_PARAMS,TARGET_COLUMN
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.utils.main_utils.utils import save_numpy_array
from networksecurity.entity.artifact_entity import DataValidationArtifact,DataTransformationArtifact
class DataTransformation:
    def __init__(self,data_validation_artifact:DataValidationArtifact,
               data_transformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifact:DataValidationArtifact=data_validation_artifact
            self.data_transformation_config:DataTransformationConfig=data_transformation_config

        except Exception as e:
            raise NetworkSecurityException(e,sys) from e
        
        
