# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

# %%
df = pd.read_csv('./data/googleplaystore.csv')

# %% preprocessing
df.info()
col = list(df.columns)
# lub col = [col for col in df.columns]
df.columns = [col.replace(' ', '_') for col in df.columns]
df = df.drop(10472) # usuniecie wiersza z uszkodzonymi danymi
df = df.reset_index() # po usunieciu wiersza reset indexow

df.Reviews = pd.to_numeric(df.Reviews) # zmiana typu danych na 
                                        #liczbowe w kolumnie 'Reviews'
# %% categories frequency
tmp = df.groupby('Category').size().rename('Count')
tmp.plot(kind='bar')

# %% type frequency
tmp = df.groupby('Type').size().rename('Count')
tmp.plot(kind='bar')

# %%
df = df[['Genres', 'Rating', 'Type']]
tmp = df.groupby(['Genres', 'Type']).agg({'Rating':['count', 'mean']})
tmp.columns = ['_'.join(x) for x in tmp.columns.ravel()]
tmp = tmp.sort_values('Rating_count', ascending=False)
tmp = tmp[tmp['Rating_count'] > 100]
tmp.plot(kind='bar', subplots=True)

# %%
top_5 = tmp.nlargest(5, 'Rating_count')['Rating_count']
top_5.plot(kind='pie')

