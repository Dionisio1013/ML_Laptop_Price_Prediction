import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts/model.pk1'
            preprocessor_path = 'artifacts/preprocessor.pk1'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print(preprocessor)
            data_scaled=preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(   self,
        Ram: int,
        Ssd: int,
        Resolution: str,
        Ghz: float,
        Graphics: str):
    
        self.Ram = Ram
        self.Ssd = Ssd
        self.Resolution = Resolution
        self.Ghz = Ghz
        self.Graphics = Graphics
        
    # This will return inputs to a form of a data frame
    def get_data_as_data_frame(self):
        try: 
            custom_data_input_dict = {
                "memory/ram": [self.Ram],
                "Ssd": [self.Ssd],
                "resolution": [self.Resolution],
                "Ghz": [self.Ghz],
                "graphics_quality": [self.Graphics]
            }
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)