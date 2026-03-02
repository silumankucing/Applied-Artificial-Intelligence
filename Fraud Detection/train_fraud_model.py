# Fraud detection model with TensorFlow
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from fraud_keywords import fraud_keywords

# Prepare dataset
fraud_texts = fraud_keywords
not_fraud_texts = [
    "pembayaran berhasil", "saldo telah ditambahkan", "transaksi diterima", "akun anda telah diverifikasi", "selamat datang di layanan kami", "terima kasih atas pembayaran", "pesanan anda diproses", "akun anda aman", "informasi telah diperbarui", "transaksi selesai", "pembayaran diterima", "akun aktif", "pesanan dikirim", "saldo cukup", "akun terdaftar", "pembayaran otomatis", "transaksi valid", "akun diverifikasi", "pesanan diterima", "pembayaran sukses", "akun terhubung"
]
texts = fraud_texts + not_fraud_texts
labels = [1]*len(fraud_texts) + [0]*len(not_fraud_texts)

# Tokenization
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded = pad_sequences(sequences, maxlen=10, padding='post')

# Model
model = Sequential([
    Embedding(1000, 16, input_length=10),
    GlobalAveragePooling1D(),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training
model.fit(padded, np.array(labels), epochs=30, verbose=0)

# Save model and tokenizer
model.save('d:/COMPUTING/Artificial Intelligence/Fraud Detection/fraud_model.h5')
import pickle
with open('d:/COMPUTING/Artificial Intelligence/Fraud Detection/tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)
