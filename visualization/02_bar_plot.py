# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

sns.set() # ustawia deafaulowy wyglad wykresow na ladniejszy

# %%
df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))

# %%
df = df.cumsum()

# %% bar plot
last_row = df.iloc[-1].apply(abs)

last_row.plot(kind='bar', title='ALABALA', color='green', alpha=0.5)

# %% multiple bar plot vertical

df_bar = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))

df_bar.plot(kind='bar', cmap='viridis')

# %%
df_bar.plot.bar(cmap='viridis') # inny sposob deklarowania rodzaju wykresu

# %% multiple bar horizontal

df_bar.plot.barh(cmap='hot')

# %% stackedbar horizontal
df_bar.plot.barh(cmap='viridis', stacked=True)

# %%
df_bar.plot.bar(cmap='viridis', stacked=True)
