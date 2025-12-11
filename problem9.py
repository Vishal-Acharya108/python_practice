import pandas as pd
import numpy as np

# Creating a synthetic dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Salary': [48000, 52000, 45000, 60000, 58000],
    'Department': ['HR', 'Tech', 'HR', 'Tech', 'Tech']
}

df = pd.read_json(pd.io.json.dumps(data)) # Converting dict to DataFrame
df = pd.DataFrame(data)

print("--- First 3 Rows ---")
print(df.head(3))

print("\n--- Basic Statistics ---")
print(df.describe())  # Gives mean, std, min, max for numeric columns
