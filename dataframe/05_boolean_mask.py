# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# %%
df_bool = df > 150

# aplikuje maske na caly dataframe - tam gdzie True zostaje wartosc tam gdzie
# False wstawia wartosc nan
df_ = df[df_bool]

# %%
df_ = df[df > 150] # rownowazne z powyzsza komorka

# %%
df_2019 = df['2019-01-01':]

# %%
df_01_2019 = df['2019-01-01':'2019-01-31']

# %%
df_01_2019.query('Close > 40')



