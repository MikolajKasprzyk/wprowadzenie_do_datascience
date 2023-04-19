# -*- coding: utf-8 -*-

import pandas as pd


# %% import data
df = pd.read_csv('./data/Consumer_Reviews_Amazon.csv', index_col=0)

# %%
df.describe()

# %%
for col in df.columns:
    print(col)
# zamieniamy kropka na podloge bo kropka moze narobic problemow
df.columns = [col.replace('.', '_') for col in df.columns]

# %% wycinamy tylko interesujace nas kolumny
df = df[['name', 'primaryCategories', 'reviews_rating', 'reviews_text']]

# %%
df.columns = ['name', 'category', 'rating', 'text']
df.info()
df.describe()

# %%
df.to_csv('./data/reviews_clean.csv')
















