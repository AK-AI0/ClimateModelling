import sys
# from data_gen import face_formartion,squares_to_edges,edge_attr,finalData
# from netCDF4 import Dataset
# import torch
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException

df = pd.DataFrame(np.random.rand(3,6),columns=['a','b','c','d','e','f'])
class CustomData:
    def __init__(self,
                 col:str,
                 ):
        
        self.col = col
       
    def get_data_as_dataframe(self):
        try:
            df1 = df[self.col]
            logging.info('Dataframe Gathered')
            return df1
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)
            


