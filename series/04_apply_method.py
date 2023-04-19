# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np


np.random.seed(0)


# %% sigma = 10, mean = 5
s = pd.Series(10 * np.random.randn(20) + 5)

# %%
s.apply(abs)
s.apply(float.is_integer)
s.apply(int)

# %%
s.apply(lambda x: 100 * x)
s.apply(lambda x: abs(x))

s_norm = s.apply(lambda x: (x - np.mean(s)) / np.std(s)) # normalizacja danych

sigmoid = s_norm.apply(lambda x: 1 / (1 + np.exp(x)))

# %%
def more_complex(x):
    return (np.exp(x))**0.5

s.apply(more_complex