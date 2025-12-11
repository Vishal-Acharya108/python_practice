import pandas as pd
import numpy as np

# Creating data with missing values (NaN)
data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Sales': [100, np.nan, 150, np.nan, 200],
    'Region': ['North', 'South', np.nan, 'West', 'North']
}
df = pd.DataFrame(data)

print("--- Original Data ---")
print(df)

# Fill missing numeric values with the Mean
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())

# Drop rows where Region is missing
df = df.dropna(subset=['Region'])

print("\n--- Cleaned Data ---")
print(df)
