import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig, ax = plt.subplots()

data1 = pd.read_excel("src/regression_data2.xlsx", names=['A','B'])

data_a = data1['A']
data_b = data1['B']

data_a_convert = np.array(data_a)
data_b_convert = np.array(data_b)

ax.hist(data_a_convert)
ax.set_title("Test")
ax.set_xlabel("A")
ax.set_ylabel("B")

plt.show()