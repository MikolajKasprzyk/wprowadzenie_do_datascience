# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib as plt
import seaborn as sns
sns.set()


"""
count() - number of non-null observations
sum()
mean()
median()
min()
max()
std()
var() - unbiased variance
skew() - skewness - 3 moment
kurt() - kurtosis - 4 moment
quantile()
apply()
cov()
corr()
"""

df = pd.read_csv('./data/ten.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
clean_price = df[['Open', 'High', 'Low', 'Close']]

# %% Series
vol = df['Volume']
cum_vol = vol.cumsum()

# %%
cum_vol.plot()

# %% plot moving average

close = df['Close']
close_rolling_avg = close.rolling(window=30).mean()

close.plot()
close_rolling_avg.plot(style='k--')

# %% moving averages
close.plot(color='black')
for i in [5, 8, 12, 60, 65, 70]:
    close_rolling_avg = close.rolling(window=i).mean()
    close_rolling_avg.plot()

# %% simple strategy
close.plot(color='black')
for i in [5]:
    close_rol_min = close.rolling(5).min()
    close_rol_min.plot()

    close_rol_max = close.rolling(5).max()
    close_rol_max.plot()
    
# %% DataFrame
clean_price.rolling(window=20).mean().plot()
close.plot(color='black')

# %%
close.rolling(window=15).std().plot()
close.plot(color='black')

# %% DataFrame Subplots
clean_price.rolling(window=20).mean().plot(subplots=True)

# %% apply custom indicator
xxx = close.rolling(window=10).apply(lambda x: (x - x.mean()).mean())
xxx.plot()










