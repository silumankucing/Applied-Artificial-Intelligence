import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

file_path = r'd:\Artificial Intelligence\Customer Segmentation\src\Mall_Customers.csv'
data = pd.read_csv(file_path)

X = data[['Annual_Income_(k$)', 'Spending_Score']]

kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(X)

plt.figure(figsize=(10, 6))
for cluster in range(5):
    cluster_data = data[data['Cluster'] == cluster]
    plt.scatter(cluster_data['Annual_Income_(k$)'], cluster_data['Spending_Score'], label=f'Cluster {cluster}')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X', label='Centroids')
plt.title('Customer Segmentation')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score')
plt.legend()
plt.show()

print(data.head())