import pandas as pd

data1 = pd.read_csv("src/trumpworld.csv", names=['A','B','C','D','E','F'], header=0)
data2 = pd.DataFrame(data1)

data3 = data1.set_index("A", drop = False)
data4 = data1["B"]
data5 = data1[data1['A'].str.contains("Person") & data1['C'].str.contains("Person")]
data6 = data1[data1['B'].str.contains("AARON SCHOCK")]

print(data4) 