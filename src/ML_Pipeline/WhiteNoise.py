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


def white_noise(df):
    # Set random seed for reproducibility
    np.random.seed(0)
    
    # Generate white noise
    white_noise = np.random.normal(loc=df.IOT_Sensor_Reading.mean(), scale=df.IOT_Sensor_Reading.std(), size=len(df))
    df["white_noise"] = white_noise
    df.describe()
    
    # Plot the white noise
    plt.plot(white_noise)
    plt.title('White Noise')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.savefig('../output/'+ 'white_noise.png')
    
    return plt.show()