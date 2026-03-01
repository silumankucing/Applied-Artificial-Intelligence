import numpy as np
import pandas as pad
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data_excel = pad.read_excel("src/regression_data2.xlsx", names=['A','B'])

data_a = data_excel["A"]
data_b = data_excel["B"]

data_a_array = np.array(data_a).reshape(-1,1)
data_b_array = np.array(data_b)

#--result

model_reg = LinearRegression().fit(data_a_array, data_b_array)
score_model = model_reg.score(data_a_array, data_b_array)

#--predict

res_predict = model_reg.predict(data_a_array)

print(score_model)

#--plot 

#plt.title("plot data excel")
#plt.xlabel("A")
#plt.ylabel("B")
#plt.plot(data_a_array, data_b_array)
#plt.show()