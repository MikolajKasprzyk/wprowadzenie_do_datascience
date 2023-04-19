# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

sns.set()


df = pd.DataFrame(np.random.rand(1000))

# %%
df.hist(bins=40)

# %%
df.plot(kind='hist')

# %%
df = pd.DataFrame(np.random.randn(100000))

# %%
df.hist(bins=100)

# %% multiple histograms
df_mul = pd.DataFrame({'mu_0_sigma_1': np.random.randn(10000),
                   'mu_1_sigma_2': 2 * np.random.randn(10000) + 1,
                   'mu_8_sigma_3': 3 * np.random.randn(10000) + 8})

df_mul.plot.hist(bins=300, cmap='viridis', alpha=0.5,
             title='Different Normal Distribution')

# %%
df_mul['mu_8_sigma_3'].plot.hist(bins=300, cmap='viridis', 
                                 alpha=0.5, cumulative=True)

# %%
df_mul.hist(sharex=True, sharey=True, bins=100, color='green')