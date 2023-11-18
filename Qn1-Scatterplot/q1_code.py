import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset2_Anime.csv')

episodes = df['episodes']
members = df['members']

plt.figure(figsize=(10, 6))
plt.scatter(episodes, members, alpha=0.5)
plt.title('Scatter Plot: Episodes vs Members')
plt.xlabel('Number of Episodes')
plt.ylabel('Number of Members')
plt.grid(True)
plt.show()
