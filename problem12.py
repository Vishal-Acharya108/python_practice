import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# --- 1. Data Generation (Simulating a Dataset) ---
# Let's pretend we are analyzing 'Study Hours' vs 'Exam Scores'
np.random.seed(42)
data_size = 100
study_hours = np.random.uniform(1, 10, data_size)  # 1 to 10 hours
# Score = 10 + 8 * hours + random noise
scores = 10 + 8 * study_hours + np.random.normal(0, 5, data_size)

# Create a DataFrame (Excel-like structure in Python)
df = pd.DataFrame({'Hours_Studied': study_hours, 'Exam_Score': scores})

# --- 2. Data Analysis & Cleaning ---
# Filter out impossible scores (e.g., > 100) just to show cleaning
df = df[df['Exam_Score'] <= 100]

print("First 5 rows of data:")
print(df.head())
print(f"\nAverage Score: {df['Exam_Score'].mean():.2f}")

# --- 3. Visualization ---
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Hours_Studied', y='Exam_Score', data=df, color='blue')
plt.title('Study Hours vs. Exam Score')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.show()

# --- 4. Machine Learning (Prediction) ---
# We want to predict Score (y) based on Hours (X)
X = df[['Hours_Studied']]
y = df['Exam_Score']

# Split into training data (80%) and testing data (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Test the model
prediction = model.predict([[5]]) # Predict score for someone who studies 5 hours
print(f"\nPrediction: If you study 5 hours, you might score: {prediction[0]:.2f}")


