# -*- coding: utf-8 -*-

import pandas as pd


s = pd.Series(['#sport#good#time',
               '#workout#free#time',
               '#summer#holiday#hot'],
               name='hashtags')

# %% splitting by hash
s = s.str.split('#')

# %%
hash_1 = s.str.get(1)
hash_2 = s.str.get(2)
hash_3 = s.str.get(3)

# %%
df_concat = pd.concat([hash_1, hash_2, hash_3], ignore_index=True)

# %%
string = df_concat.str.cat(sep=' ')

# %%
df_concat_columns = pd.concat([hash_1, hash_2, hash_3], axis=1)

string = df_concat.str.cat(sep=' * ')

# %%
split_2 = s.str.split('#', expand=True)
split_2 = split_2.drop(0, axis=1)

# %%
s.str.replace('#', ' ')

s.str.replace('#', '_')
























