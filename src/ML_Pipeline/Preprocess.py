#importing all required libraries
import pandas as pd

def preprocess(df):
    df.time = pd.to_datetime(df.time, format='%d-%m-%Y %H:%M')
    df = df.sort_values('time')
    del df['Error_Present']
    del df['Sensor_2']
    del df['Sensor_Value']
    df.set_index('time', inplace=True)
    df = df.asfreq('H')
    df.IOT_Sensor_Reading = df.IOT_Sensor_Reading.fillna(method="ffill")
    df.reset_index(inplace=True)
    return df