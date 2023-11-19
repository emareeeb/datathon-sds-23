import pandas as pd
from ast import literal_eval
from scipy.stats import ttest_ind

df = pd.read_csv('Dataset2_Anime.csv')

df['genre'] = df['genre'].apply(literal_eval)

df['main_genre'] = df['genre'].apply(lambda x: x[0] if x else None)

genre1 = 'Shounen'
genre2 = 'Shoujo'

genre1_subset = df[df['main_genre'] == genre1].head(10)['score'].dropna()
genre2_subset = df[df['main_genre'] == genre2].head(10)['score'].dropna()

t_stat, p_value = ttest_ind(genre1_subset, genre2_subset, nan_policy='omit')

print(f'T-statistic: {t_stat}')
print(f'P-value: {p_value}')

alpha = 0.05
if p_value < alpha:
    print(f'There is a significant difference in ratings between {genre1} and {genre2} anime.')
else:
    print(f'There is no significant difference in ratings between {genre1} and {genre2} anime.')
