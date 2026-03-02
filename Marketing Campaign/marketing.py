# Contoh Machine Learning untuk Targeting Marketing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Contoh data pelanggan
# Fitur: usia, pendapatan, status menikah, respon campaign

data = {
    'usia': [25, 34, 45, 23, 54, 31, 40, 29, 38, 50],
    'pendapatan': [3500, 4200, 6000, 3200, 8000, 4100, 5200, 3900, 4800, 7000],
    'menikah': [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    'respon': [1, 0, 1, 0, 1, 0, 1, 0, 1, 1]  # 1=tertarik, 0=tidak
}
df = pd.DataFrame(data)

X = df[['usia', 'pendapatan', 'menikah']]
y = df['respon']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prediksi dan evaluasi
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Contoh prediksi targeting
calon = pd.DataFrame({'usia': [28], 'pendapatan': [4500], 'menikah': [0]})
prediksi = model.predict(calon)
print('Targeting:', 'Tertarik' if prediksi[0]==1 else 'Tidak Tertarik')
