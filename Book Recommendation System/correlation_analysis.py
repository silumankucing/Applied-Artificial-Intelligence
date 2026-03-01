import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts

data = pd.read_excel("src/farmdata.xlsx", names=['Jenis tanaman', 'Nama Tanaman', 'Luas Sisa Tanaman Tahun lalu', 'Tambah Tanam', 'Luas Tanaman', 'Luas tanaman Panen Habis Tahunan', 'Produksi', 'Sisa tanaman', 'Tanaman Yang diBongkar'])

sisa_tanaman = data["Luas Sisa Tanaman Tahun lalu"]
tambah_tanam = data["Tambah Tanam"]
produksi = data["Produksi"]

n = np.array(sisa_tanaman)
m = np.array(tambah_tanam)
o = np.array(produksi)

pearson_param = sts.pearsonr(n,o)
spearman_param = sts.spearmanr(n,o)
kendalltau_param = sts.kendalltau(n,o)

print(pearson_param)
print(spearman_param)
print(kendalltau_param)

#test