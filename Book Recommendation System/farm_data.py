import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("src/farmdata.xlsx", names=['Jenis tanaman', 'Nama Tanaman', 'Luas Sisa Tanaman Tahun lalu', 'Tambah Tanam', 'Luas Tanaman', 'Luas tanaman Panen Habis Tahunan', 'Produksi', 'Sisa tanaman', 'Tanaman Yang diBongkar'])

sisa_tanaman = data["Luas Sisa Tanaman Tahun lalu"]
tambah_tanam = data["Tambah Tanam"]
produksi = data["Produksi"]

n = np.array(sisa_tanaman)
m = np.array(tambah_tanam)
o = np.array(produksi)

plt.plot(n, m, color='g')
plt.xlabel("A", color='y')
plt.ylabel("C", color='r')

plt.twinx()
plt.plot(n, o, color='y')
plt.ylabel("B", color='b')

plt.show()