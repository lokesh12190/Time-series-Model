#importing all required libraries
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller,kpss
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
import numpy as np
import sys

#create a class for autoregressor model
def AR_model(df):
    # Create AR model
    order = 1  # Order of the AR model
    model = AutoReg(df['IOT_Sensor_Reading'], lags=order)
    
    # Fit the model
    model_fit = model.fit()
    
    # Get the fitted values
    fitted_values = model_fit.fittedvalues
    
    rmse = np.sqrt(mean_squared_error(df['IOT_Sensor_Reading'][:-1], fitted_values))
    with open('../output/'+ 'log.txt', 'a') as f:
        sys.stdout = f
        print("***************************AR1 Model*******************************")
        print(f"RMSE of AR1 model: {rmse}")
        print(model_fit.summary())
    sys.stdout = sys.__stdout__
    
    # Plot the original data and the fitted values
    plt.plot(df['IOT_Sensor_Reading'], label='Original Data')
    plt.plot(fitted_values, label='Fitted Values')
    plt.legend()
    plt.title('First-Order AR Model')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.savefig('../output/'+ 'AR_Model.png')
    plt.show()
    
    
    # Print model summary
    return model_fit.summary()
