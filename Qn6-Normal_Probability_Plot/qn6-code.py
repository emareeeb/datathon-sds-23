import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import probplot

df = pd.read_csv('Dataset2_Anime.csv')

ratings = df['score'].dropna()

probplot(ratings, plot=plt)
plt.title('Normal Probability Plot of Anime Ratings')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')
plt.show()
