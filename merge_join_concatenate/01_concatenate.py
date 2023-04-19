# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# %%
df1 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df2 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df3 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
s = pd.Series(np.random.rand(10), name='x')

# %% concat
# połączenie obiektów dataframe o kolumnach o tych samych nazwach

df = pd.concat([df1, df2, df3], ignore_index=True)

# %%
df = pd.concat([df1, df2, df3])
df = df.reset_index()

# %%
# połączenie obiektów z innymi nazwami kolumn

df1 = pd.DataFrame(np.random.rand(10, 4), columns=list('abcd'))
df2 = pd.DataFrame(np.random.rand(10, 4), columns=list('efgh'))

df = pd.concat([df1, df2], axis=1) # łączy po kolumnach

# %% outer, inner
df1 = df1[::2]
 
# %%
df = pd.concat([df1, df2], axis=1)

# %%

df_outer = pd.concat([df1, df2], axis=1, join='outer') # join='outer' jest domyslnie
df_inner = pd.concat([df1, df2], axis=1, join='inner')

# %%
# append Series to DataFrame

df = pd.concat([df2, s], axis=1)





















































