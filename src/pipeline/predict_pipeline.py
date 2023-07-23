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
        TypeName: str,
        Company: str,
        OpSys: str,
        Ram: int,
        Memory: str,
        Resolution: str,
        Ghz: float,
        Touchscreen: bool,
        IPS: bool,
        is_4K: bool,
        Processor: str,
        Gpu_Brand: str):
    
        self.TypeName = TypeName
        self.Company = Company
        self.OpSys = OpSys
        self.Ram = Ram
        self.Memory = Memory
        self.Resolution = Resolution
        self.Ghz = Ghz
        self.Touchscreen = Touchscreen
        self.IPS = IPS
        self.is_4K = is_4K
        self.Processor = Processor
        self.Gpu_Brand = Gpu_Brand
        
    # This will return inputs to a form of a data frame
    def get_data_as_data_frame(self):
        try: 
            custom_data_input_dict = {
                "TypeName": [self.TypeName],
                "Company": [self.Company],
                "OpSys": [self.OpSys],
                "Ram": [self.Ram],
                "Memory": [self.Memory],
                "Resolution": [self.Resolution],
                "Ghz": [self.Ghz],
                "Touchscreen": [self.Touchscreen],
                "IPS": [self.IPS],
                "is_4K": [self.is_4K],
                "Processor": [self.Processor],
                "Gpu_Brand": [self.Gpu_Brand]
            }
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)