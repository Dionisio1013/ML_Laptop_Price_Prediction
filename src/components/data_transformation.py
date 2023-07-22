import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from src.exception import CustomException
from src.logger import logging
from scipy import sparse
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")


# class OrdinalEncoder:
#     def __init__(self):
        

# class FrequencyEncoder:
#     # Creating an empty dictionary for the categorical variable columns
#     def __init__(self):
#         self.frequency_map = {}
    
#     def fit(self, X, y=None):
#         for column in X.columns:
#             self.frequency_map[column] = X[column].value_counts(normalize = True)
#         return self
    
#     def transform(self, X):
#         for column in X.columns:
#             X[column] = X[column].map(self.frequency_map[column])
#         return X
    



class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function si responsible for data trnasformation
        
        '''
        try:
            numerical_columns = ["Inches", "4K", "IPS", "Weight", "Touchscreen", "Ghz", "Ram"]
            categorical_ordinal_columns = ["Resolution","Memory"]
            categorical_frequency_columns = ["Company", "TypeName","Gpu_Brand","OpSys","Processor"]

            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )

            cat_frequency_pipeline=Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("label_encoder", OneHotEncoder())
                ]
            )


            logging.info(f"Categorical columns: {categorical_frequency_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns)
                ,("cat_frequency_pipeline",cat_frequency_pipeline,categorical_frequency_columns)

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

            target_column_name="Price_euros"
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

            # You get a weird fucking array if you don't transform this

            input_feature_train_arr =  sparse.csr_matrix(input_feature_train_arr).toarray()
            input_feature_test_arr =  sparse.csr_matrix(input_feature_test_arr).toarray()

            print("Shit here:",input_feature_train_arr)
            print("fuck me here:",np.array(target_feature_train_df))


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






        