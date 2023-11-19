import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset2_Anime.csv')

plt.figure(figsize=(10, 6))
sns.boxplot(x='score', data=df)

plt.title('Boxplot of Ratings for Anime')
plt.show()
