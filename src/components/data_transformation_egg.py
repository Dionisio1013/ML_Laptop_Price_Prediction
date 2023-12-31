import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
#from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from src.exception import CustomException
from src.logger import logging
from scipy import sparse
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pk1")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function si responsible for data trnasformation
        
        '''
        try:
            numerical_columns = ["Ghz", "Ssd", "memory/ram"]
            categorical_ordinal_encoding_columns = ["graphics_quality", "resolution", 'Cpu','Brand']

            num_pipeline= Pipeline(
                steps=[
             #   ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())
                ]
            )

            cat_ordinal_encode_pipeline=Pipeline(
                steps=[
              #  ("imputer",SimpleImputer(strategy="most_frequent")),
                ("ordinal_encoder", OrdinalEncoder(handle_unknown = 'use_encoded_value', unknown_value=-1))
                ]
            )


            logging.info(f"Categorical columns: {categorical_ordinal_encoding_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns)
                ,("cat_ordinal_encode_pipeline",cat_ordinal_encode_pipeline,categorical_ordinal_encoding_columns)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="price"
            print("Shape before ASDASD: X data",train_df.shape)

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            print("Shape before preprocessing: X data",input_feature_train_df.shape)

            

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            print("shape of x",input_feature_train_arr.shape)
            print("shape of y",np.array(target_feature_train_df).shape)

       

            input_feature_train_arr =  sparse.csr_matrix(input_feature_train_arr).toarray()
            input_feature_test_arr =  sparse.csr_matrix(input_feature_test_arr).toarray()

            # print("Array Here:",input_feature_train_arr)
            # print("target array here:",np.array(target_feature_train_df))


            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df).reshape(-1,1)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df).reshape(-1,1)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
