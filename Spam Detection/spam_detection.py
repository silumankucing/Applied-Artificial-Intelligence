# Contoh Spam Detection dengan Machine Learning
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Contoh data sederhana
texts = [
    "Dapatkan hadiah besar sekarang!",
    "Transfer uang ke rekening ini segera",
    "Promo diskon terbatas hanya hari ini",
    "Halo, bagaimana kabar Anda?",
    "Terima kasih atas pesanan Anda",
    "Silakan klik link untuk verifikasi",
    "Akun Anda telah diverifikasi",
    "Menangkan undian berhadiah!",
    "Pesanan Anda sedang diproses",
    "Pinjaman kilat tanpa jaminan"
]
labels = [1, 1, 1, 0, 0, 1, 0, 1, 0, 1]  # 1=spam, 0=not spam

# Vectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

y = labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluasi
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Prediksi kalimat baru
kalimat = ["Segera transfer dana untuk hadiah"]
X_new = vectorizer.transform(kalimat)
pred = model.predict(X_new)
print("Spam" if pred[0]==1 else "Not Spam")
