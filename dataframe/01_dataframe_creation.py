# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# %% DATA FRAME
df = pd.DataFrame(data=[12, 34, 23])

# %%
df = pd.DataFrame(data=[[12, 34, 23],
                        [53, 23, 74]])

# %%
df = pd.DataFrame(data=[[12, 34, 23],
                        [53, 23, 74]],
                        index=['first', 'second'],
                        columns=['col1', 'col2', 'col3'])

# %%

df = pd.DataFrame(data=[[12, 34, 23],
                        [53, 23, 74],
                        [539, 230, 748]],
                        index=['first', 'second', 'third'],
                        columns=['col1', 'col2', 'col3'])

# %%
dct = {'one':pd.Series([1, 2, 3]),
       'two':pd.Series([4, 5, 6]),
       'flag':['yes', 'no', 'no']}

df = pd.DataFrame(dct)

# %%
dct = {'one':pd.Series([1, 2, 3, 9, 10]),
       'two':pd.Series([4, 5, 6]),}

df = pd.DataFrame(dct) # dla brakujacych wartosci wstawia nan

# %%
dct = {'one':pd.Series(np.random.randn(100)),
       'two':pd.Series(np.random.randn(100)),
       'three':pd.Series(np.random.randn(100))}

df = pd.DataFrame(dct)

# %%
df.index
df.columns

# %%
list_od_dicts = [{'apple':1, 'orange':4}, {'apple':3, 'orange':3, 'mango':2}]

df = pd.DataFrame(list_od_dicts)

# %%

for col in df.columns:
    print(col)
    
big_letters = [col.upper() for col in df.columns]    
    
df.columns = big_letters

# %%
d = {'Wig20':['PKN Orlen', 'PKO BP', 'LPP'],
     'mWig40':['Amica', 'Playway', 'Benefit']}

df = pd.DataFrame(d)
    
















