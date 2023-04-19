# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %% importing dataset
df  = pd.read_csv('./data/ten.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# %% pct_change daily
df['Daily_change'] = df['Close'].pct_change()

# %% pct_change daily
df['5_Daily_change'] = df['Close'].pct_change(periods=5)

# %%
df['Close_to_open'] = df[['Open', 'Close']].pct_change(axis=1).drop('Open', axis=1)

# %%
clean_price = df[['Open', 'High', 'Low', 'Close']]

daily_changes = clean_price.pct_change()






































