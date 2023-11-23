import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ast

file_path = "Dataset2_Anime.csv"
df= pd.read_csv(file_path)

df['genre'] = df['genre'].apply(ast.literal_eval)
df_exploded = df.explode('genre')

plt.figure(figsize=(10,6))
sns.boxplot(x='genre', y='score', data=df_exploded)
plt.xticks(rotation=90)
plt.show()
