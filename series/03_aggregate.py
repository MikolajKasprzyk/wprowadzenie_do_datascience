# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


# %% generating some data

np.random.seed(0)

s = pd.Series(np.random.randn(20))

# %% aggregate

minimum = s.aggregate(min) # funkcja min jest wbudowana
maximum = s.aggregate(max)
sum_ = s.aggregate(sum)

mean = s.aggregate(np.mean)
std = s.aggregate(np.std)

# %%
stats = s.aggregate(['min', 'max', 'mean', 'sum'])

stats_np = s.aggregate([np.mean, np.std, np.median])

