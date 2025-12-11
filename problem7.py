import pandas as pd

data = {
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Furniture'],
    'Price': [1200, 40, 800, 60, 450],
    'Quantity': [5, 10, 2, 15, 3]
}
df = pd.DataFrame(data)

# Filter: Items more expensive than $100
expensive_items = df[df['Price'] > 100]

# Group By: Average price per category
category_summary = df.groupby('Category')['Price'].mean()

print("--- Expensive Items ---")
print(expensive_items)
print("\n--- Average Price by Category ---")
print(category_summary)
