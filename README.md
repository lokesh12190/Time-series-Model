# Time-series-Model-with-Autoregressive-and-Moving-Average-Techniques
"Developing an Enhanced Time Series Model: Integrating Autoregressive and Moving Average Techniques"
# Time Series

Time series is a sequence of information which attaches a time period to each value.
The value can be pretty much anything measurable.
It depends on time in some way, like prices, humidity or number of people.
As long as the values we record are unambiguous, any medium could be measured with Time series.
There aren't any limitations regarding the total time span of our Time series.
It could be a minute, a day, a month or even a century.
All we need is a starting and an ending point.


## Autoregressor

The auto regressive model or a model for short, relies on past period values and past periods only to predict current period values.
It's a linear model where current period values are a sum of past outcomes multiplied by a numeric factor.
Value of phi lies between -1 and 1.

## Basics

- Chronological Data
- Cannot be shuffled
- Each row indicate specific time record
- Train – Test split happens chronologically
- Data is analyzed univariately (for given use case)
- Nature of the data represents if it can be predicted or not

## Code Description

    File Name : Preprocess.py
    File Description : Class to preprocess the data, handle missing values, set time as index and QQ plots



    File Name : Engine.py
    File Description : Main class for starting different parts and processes of the lifecycle



    File Name : WhiteNoise.py
    File Description : Steps to test if the visualization is white noise or not



    File Name : RandomWalk.py
    File Description : Steps to test if the visualization is random walk or not



    File Name : Stationarity.py
    File Description : Steps to test if the visualization is stationary or not



    File Name : AcfAndPacf.py
    File Description : Steps to test the visualization of lag features



    File Name : Autoregressor.py
    File Description : Training the model on autoregression with log likelyhood

    
    
    File Name : RollingWindow.py
    File Description : Steps to verify the mean and Std

## Steps to Run

There are two ways to execute the end to end flow.

- Modular Code
- IPython

### Modular code
- Create virtualenv

Windows:

    Open the command prompt.
    Navigate to the desired directory where you want to create the virtual environment.
    Run the following command to create a virtual environment named "venv":

    `python -m venv venv`
    Activate the virtual environment by running:

    `venv\Scripts\activate`


Linux:

    Open the terminal.
    Navigate to the desired directory where you want to create the virtual environment.
    Run the following command to create a virtual environment named "venv":
    
    `python3 -m venv venv`
    Activate the virtual environment by running:

    `source venv/bin/activate`

macOS:

    Open the terminal.
    Navigate to the desired directory where you want to create the virtual environment.
    Run the following command to create a virtual environment named "venv":

    `python3 -m venv venv`
    Activate the virtual environment by running:

    `source venv/bin/activate`
    
    Once the virtual environment is activated, you can install packages and dependencies specific to that environment without interfering with the global Python installation.


- Install requirements `pip install -r requirements.txt`
- Run Code `python Engine.py`
- Check output for all the visualization

### IPython Google Colab

Follow the instructions in the notebook `TimeSeries_AutoRegressor_RollingWindow.ipynb`


```
modular_code
├─ input
│  └─ Data-Chillers.csv
├─ lib
│  └─ TS workbook.ipynb
├─ output
├─ Readme.md
├─ requirements.txt
└─ src
   ├─ Engine.py
   └─ ML_Pipeline
      ├─ acf.py
      ├─ autocovariance.py
      ├─ Autoregressor.py
      ├─ EDA.py
      ├─ MA_model.py
      ├─ pacf.py
      ├─ Preprocess.py
      ├─ RandomWalk.py
      ├─ Stationarity.py
      ├─ WhiteNoise.py

```



