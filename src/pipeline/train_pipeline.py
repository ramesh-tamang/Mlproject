import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.exception import XGBRegressor
from src.logger import logging

from  src.utils import save_object

@dataclass
class ModelTrainConfig:
    trained_model_file_path=os.path.join("artifacts","modul.pkl")
    
    class ModelTrainer:
        def __init__(self):
            self.model_trainer_confing=ModelTrainConfig()

        def initiate_model_trainer(self,trainer_array,test_array,preprocessor_path):
        
            try:
                logging.info("Split training and test input data")
                X_train,y_taing,X_test,y_test=(
                    trainer_array
                )         
            except:
                pass

    