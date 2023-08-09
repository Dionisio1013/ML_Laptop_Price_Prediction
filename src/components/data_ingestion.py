# Code related to reading the data
import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd


from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation_egg import DataTransformation

from src.components.model_trainer import ModelTrainer


# This set of code will be passed  
@dataclass
# dataclass can directly define my class variable

# We are creating a path to save all the files in this path 
class DataIngestionConfig:
    # All the outputs will be put into the artifacts folder
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        # creating a variable which consists of the three values. Varialbe with subobject from the three train,test,raw
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Read the dataset
            df = pd.read_csv('notebook/newegg.csv')
            logging.info('Read the dataset as dataframe')

            
            graphics_order = df.groupby('graphics_quality')['price'].mean().sort_values(ascending = True).index

            df['graphics_quality'] = pd.Categorical(df['graphics_quality'], categories = graphics_order)
            
            # This code is basically telling the computer that there is an order between these cateogrical variables 
            # making them ordinal

            resolution_ordered = ['1366x768','1536x1024','1600x900','1920x1028','1920x1080',
                                   '1920x1200','1920x1280','2220x1080','2240x1400','2256x1504',
                                   '2260x1400','2400x1600','2496x1664','2560x1440','2560x1600',
                                   '2736x1824','2800x1620','2880x1620','2880x1800','2880x1920',
                                   '3000x2000','3072x1920','3200x2000','3240x2160','3300x2200',
                                   '3840x2160','3840x2400']
            
            print(pd.Categorical(df['resolution'], categories=resolution_ordered, ordered = True))

            df['resolution'] = pd.Categorical(df['resolution'], categories=resolution_ordered, ordered = True)

            brand_order = df.groupby('Brand')['price'].mean().sort_values(ascending = True).index
            df['Brand'] = pd.Categorical(df['Brand'], categories = brand_order, ordered = True)

            cpu_order = df.groupby('Cpu')['price'].mean().sort_values(ascending = True).index
            df['Cpu'] = pd.Categorical(df['Brand'], categories = cpu_order, ordered = True)

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42)

            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)

            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
        
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj=DataIngestion()
    train_data, test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)
        # Keep writing logs so you can know where the problems are with your code
    
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_trainer(train_arr,test_arr)
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))