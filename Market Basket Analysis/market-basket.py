# Contoh Market Basket Analysis dengan Apriori
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Contoh data transaksi
# Setiap baris adalah transaksi, setiap kolom adalah produk
# 1 = dibeli, 0 = tidak dibeli

data = {
    'Roti': [1, 0, 1, 1, 0],
    'Susu': [1, 1, 1, 0, 0],
    'Keju': [0, 1, 1, 1, 1],
    'Telur': [1, 1, 0, 1, 0],
    'Mentega': [0, 0, 1, 0, 1]
}
df = pd.DataFrame(data)

# Apriori untuk mencari itemset yang sering muncul
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

# Aturan asosiasi
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
