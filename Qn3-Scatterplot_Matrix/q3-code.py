import pandas as pd
from seaborn import pairplot
import matplotlib.pyplot as plt
df = pd.read_csv('Dataset2_Anime.csv')
numerical_features = ['episodes', 'score', 'ranked']
scatterplot_matrix = pairplot(df[numerical_features])
plt.suptitle('Scatterplot Matrix of Numerical Features', y=1.02)
plt.show()
