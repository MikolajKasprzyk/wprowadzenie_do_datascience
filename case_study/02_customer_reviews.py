# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

# %%
df = pd.read_csv('./data/reviews_clean.csv')

# %% plotting
df['category'].value_counts().plot(kind='pie')

# %% sort index dlatego ze z automatu sie plotuje od najwiekszej liczby
# wystapien do najmniejszej a nie wg indexu
df['rating'].value_counts().sort_index().plot(kind='bar', legend=True)

# %% extract 3 most rating products
tmp = df.groupby('name').count()['rating'].rename('count').nlargest(3)

# %% 3  najwyzej oceniane produkty
df.groupby('name').agg('mean').rename(columns={'rating':'avg_rating'}).\
                   nlargest(3, columns='avg_rating')
                   
                   
























