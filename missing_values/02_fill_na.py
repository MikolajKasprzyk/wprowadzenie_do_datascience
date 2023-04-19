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
df = df.fillna(0) # wpisuje zadaną wartosc zamiast nan

# %%
df = df.fillna('alabala')

# %%
df['two'] = df['two'].fillna(0) # wstawia zera na miejsce nan w kolumnie two

# %%
df = df.fillna(df.mean()) # uzupelnia braki srednia w kazdej kolumnie

# %%
df['four'] = df['four'].fillna(df['four'].median())

