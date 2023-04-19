# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['one', 'two', 'three', 'four'])

# %% losowe nadpisywanie wartosci na nan
for row in df.values:
    i = np.random.choice([0, 1, 2, 3])
    row[i] = np.nan
    
# %% losowe nadpisywanie wartosci na nan
for row in df.values:
    switch = np.random.choice([0, 1])
    if switch:
        i = np.random.choice([0, 1, 2, 3])
        row[i] = np.nan
    
# %%
df.isnull()

df['one'].isnull()

df[df['one'].isnull()]
    
df[~df['one'].isnull()] # zaprzeczenie warunku przy pomocy tyldy

# %%
df.notnull() # odwrotnie niz isnull()
df[df.notnull()]
    
# %%
df['five'] = np.nan

# %%

del df['five']
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    