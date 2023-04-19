# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import mathplotlib as plt
import seaborn as sns

sns.set() # ustawia deafaulowy wyglad wykresow na ladniejszy

# %%
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('2019-01-01', periods=1000))

# %%
ts = ts.cumsum()

# %%
ts.plot()

# %%
ts = ts.cummin()
ts.plot()

# %%
df = pd.DataFrame(np.random.randn(1000, 5),
                  index=pd.date_range('2019-01-01', periods=1000),
                  columns=list('ABCDE'))

# %%
df = df.cumsum()
df.plot()

# %%
df['B'].plot(kind='bar')

# %%
abs(df.iloc[5]).plot(kind='bar', title='ALABALA')

# %%
def sinplot(n=10, flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, n + 1):
        plt.pyplot.plot(x, np.sin(x + i * .5) * (n + 2 - i) * flip)
        
sinplot()