import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load dataset
df = pd.read_csv('resource/financial_fraud_detection_dataset.csv')

# Basic preprocessing: drop rows with missing values
df = df.dropna()

# Assume the label column is named 'is_fraud' (change if different)
X = df.drop('is_fraud', axis=1)
y = df['is_fraud']

# If there are categorical columns, encode them
X = pd.get_dummies(X)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test

# --- TensorFlow text fraud detection ---
model = tf.keras.models.load_model('d:/COMPUTING/Artificial Intelligence/Fraud Detection/fraud_model.h5')
with open('d:/COMPUTING/Artificial Intelligence/Fraud Detection/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

def predict_fraud(sentence):
    seq = tokenizer.texts_to_sequences([sentence])
    pad = pad_sequences(seq, maxlen=10, padding='post')
    pred = model.predict(pad)[0][0]
    return "FRAUD" if pred > 0.5 else "NOT-FRAUD"

if __name__ == "__main__":
    kalimat = input("Masukkan kalimat: ")
    hasil = predict_fraud(kalimat)
    print("Hasil deteksi:", hasil)