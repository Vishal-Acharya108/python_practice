import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Dataset
data = {
    'StudyHours': [1, 2, 3, 4, 5, 6, 7, 8],
    'SleepHours': [8, 7, 7, 6, 6, 5, 5, 4],
    'ExamScore': [60, 65, 70, 75, 80, 85, 90, 92]
}
df = pd.DataFrame(data)

# Calculate correlation matrix
corr_matrix = df.corr()

# Plot heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Feature Correlation Matrix')
plt.show()

