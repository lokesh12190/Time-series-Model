import numpy as np
#importing all required libraries
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller,kpss
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error


def autocovariance(df):
    df.set_index('time', inplace=True)
    print("###############################")
    print(df)
    # Calculate the autocovariance matrix
    autocov_matrix = np.cov(df, rowvar=False)
    
    print("Autocovariance Matrix:")
    print(autocov_matrix)
    
    return autocov_matrix