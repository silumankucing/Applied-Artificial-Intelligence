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

sum_sisa_tanaman = np.sum(n)
jumlah_data = len(n)
nilai_rata2 = sum_sisa_tanaman/jumlah_data
deviasi_standard = np.std(sum_sisa_tanaman)
variansi = np.var(sum_sisa_tanaman)

print("Jumlah data : ", jumlah_data)
print("Jumlah sisa tanaman :", sum_sisa_tanaman)
print("Nilai rata-rata :", nilai_rata2)
print("Deviasi standard :", deviasi_standard)
print("Variansi", variansi)