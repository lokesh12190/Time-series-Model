#importing all required libraries
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller,kpss
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error

def pacf(df):
    df.set_index('time', inplace=True)
    # Plot PACF
    plt.figure(figsize=(12, 4))
    plot_pacf(df['IOT_Sensor_Reading'], lags=30)
    plt.xlabel('Lag')
    plt.ylabel('Partial Autocorrelation')
    plt.title('Partial Autocorrelation Function (PACF)')
    plt.savefig('../output/'+ 'pacf.png')
    return plt.show()