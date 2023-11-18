import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset2_Anime.csv')

score = df['score']

plt.figure(figsize=(10, 6))
plt.hist(score, bins=30, edgecolor='black')
plt.title("Histogram: Anime Score Distribution")
