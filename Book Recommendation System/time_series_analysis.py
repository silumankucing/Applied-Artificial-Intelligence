import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_consumption = pd.read_excel("opsd_germany.xlsx", names=['Date','Consumption','Wind','Solar','Wind+Solar'], header=0)
data_consumption["Date"] = pd.to_datetime(data_consumption["Date"])

data_consumption = data_consumption.set_index('Date')

data_freq = data_consumption.asfreq('D', method = 'ffill')

data_columns = ['Consumption', 'Wind', 'Solar', 'Wind+Solar']
data_7d_rol = data_consumption[data_columns].rolling(window = 7, center = True).mean()

plt.plot(data_7d_rol)
plt.show()

#print(data_7d_rol)