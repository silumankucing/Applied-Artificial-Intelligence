import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("src/simple.xlsx")

data2 = data["A"]
data3 = data["B"]

n = np.array(data2)
m = np.array(data3)

converted_n = str(n)
converted_m = str(m)

o = zip(converted_n, converted_m)

plt.plot(n,m)
plt.show()