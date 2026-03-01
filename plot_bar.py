import matplotlib.pyplot as barr
import pandas as pd
import numpy as np

data = pd.read_excel("src/farmdata.xlsx", names=['Jenis tanaman', 'Nama Tanaman', 'Luas Sisa Tanaman Tahun lalu', 'Tambah Tanam', 'Luas Tanaman', 'Luas tanaman Panen Habis Tahunan', 'Produksi', 'Sisa tanaman', 'Tanaman Yang diBongkar'])

data2 = data["Nama Tanaman"]
data3 = data["Luas Sisa Tanaman Tahun lalu"]

a = np.array(data2)
b = np.array(data3)

barr.bar(a, b)
barr.show()
barr.xticks(rotation = 45)