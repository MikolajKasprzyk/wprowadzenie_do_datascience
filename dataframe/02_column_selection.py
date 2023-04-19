# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)

# %%
print(df.columns)
# %%
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

open_price = df['Open']
open_price = df.iloc[:, 0] # te dwa sa rozsame
high_price = df['High']

# %%
close_price = df.Close # rowniez wycina kolumne Close
volume = df.Volume

# %%
last_column = df.iloc[:, -1]

# %%
two_columns = df[['Open', 'Close']]

three_columns = df.iloc[:, [0, 3, 4]]

# %%
from_open_to_close = df.iloc[1:10, 0:4]


