# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# %% importing dataset
df  = pd.read_csv('./data/ten.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
clean_price = df[['Open', 'High', 'Low', 'Close']]

# %% computing correlation matrix
corr_matrix = clean_price.corr()

# %% corr between series
df['Open'].corr(df['Close'])

# %% plot corr matrix
plt.matshow(corr_matrix)

# %%
sns.heatmap(corr_matrix)










