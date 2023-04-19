# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# %%

df = pd.read_csv('./data/cdr_d.csv', index_col=0)


# %%
# pomija 200 wierszy przy imporcie
df = pd.read_csv('./data/cdr_d.csv', index_col=0, skiprows=200)

# %% 100 pierwszych wierszy
df = pd.read_csv('./data/cdr_d.csv', index_col=0, nrows=100)

# %%
df = pd.read_csv('./data/reviews_clean.csv')































