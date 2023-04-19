# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# %%
sample_10 = df.sample(n=10) # losuje 10 elementów

# %%
sample_10_procent = df.sample(frac=0.1) # losuje 10 % danych