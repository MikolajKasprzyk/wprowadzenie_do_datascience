# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['one', 'two', 'three', 'four'])

for row in df.values:
    switch = np.random.choice([0, 1])
    if switch:
        i = np.random.choice([0, 1, 2, 3])
        row[i] = np.nan
        
# %%
df.describe()

# %%
df.dropna(axis=0) # usuwamy wiersze gdzie brakuje danych


# %%
df.dropna(axis=1) # usuwa kolumne gdzie sa jakies braki