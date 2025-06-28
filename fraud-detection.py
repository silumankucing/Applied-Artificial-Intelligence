import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

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