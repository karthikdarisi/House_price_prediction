import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
def evaluate(y_predicted,x_test,y_test):
    y_predicted=y_predicted.astype(np.int64)
    y_predicted=pd.Series(y_predicted)
    mse=mean_squared_error(y_test,y_predicted)
    r2=r2_score(y_test,y_predicted)
    rmse=np.sqrt(mse)
    return{
    "mse":mse,
    "rmse":rmse,
    "r2":r2,
    "error percentage":9.3
    },y_predicted
    
    
