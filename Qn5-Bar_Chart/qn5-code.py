import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset2_Anime.csv')

df['genre'] = df['genre'].apply(eval)

flat_categories = [category for sublist in df['genre'].values for category in sublist]

category_counts = pd.Series(flat_categories).value_counts()

top_categories = category_counts.head(10)

top_categories.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Most Common Anime Categories')
plt.xlabel('Category')
plt.ylabel('Frequency')
plt.show()
