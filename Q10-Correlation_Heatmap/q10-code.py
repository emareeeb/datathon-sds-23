import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset2_Anime.csv')

numerical_features = ['ranked', 'score', 'episodes']

correlation_matrix = df[numerical_features].corr()

plt.figure(figsize=(10, 8))

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)

plt.title('Correlation Heatmap of Numerical Features')
plt.show()
