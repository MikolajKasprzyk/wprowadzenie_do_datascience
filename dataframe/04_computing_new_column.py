# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# %%
df['Average'] = (df['Open'] + df['Close']) / 2.

# %%
df['Daily_Change'] = df['Close'] / df['Close'].shift(1) - 1

# %%
df = df.assign(avg=(df['Open'] + df['Close']) / 2.)

# %%
max_daily_change = df['Daily_Change'].aggregate(max)
min_daily_change = df['Daily_Change'].aggregate(min)

# %%
avg_daily_change = df['Daily_Change'].aggregate(np.mean)

# %%
df['Daily_Change'].hist(bins=100)

# %%
df['Flag'] = df['Daily_Change'] > 0

# %%
df['Flag'].aggregate(sum) # liczba dni gdzie stopa zwrotu byla dodatnia

#stosunek dni z dodatnia stopa zwrotu do wszystkich
days_positive_return = df['Flag'].aggregate(sum) / df['Flag'].aggregate('count')

























