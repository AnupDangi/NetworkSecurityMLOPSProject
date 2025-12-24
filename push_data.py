import os
import sys
import json
from dotenv import load_dotenv
import certifi
import numpy as np
import pandas as pd
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import pymongo
load_dotenv()

MONGODB_URL=os.getenv("MONGODB_URL")

ca=certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def cv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            record=list(json.loads(data.T.to_json()).values())
            return record

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGODB_URL)
            self.database=self.mongo_client[self.database]

            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)


if __name__=="__main__":
    FILE_PATH=os.path.join(os.getcwd(),"NetworkData","phisingData.csv")
    DATABASE_NAME="ANUP_DB"
    COLLECTION_NAME="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.cv_to_json_convertor(file_path=FILE_PATH)
    no_of_records=networkobj.insert_data_to_mongodb(records,DATABASE_NAME,COLLECTION_NAME)
    print(f"Number of records inserted to Mongodb is : {no_of_records}")

