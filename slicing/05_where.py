# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


# %%
df = pd.DataFrame(np.random.randn(31, 2),
                  columns=list('ab'),
                  index=pd.date_range(start='20190101', periods=31))

s = pd.Series(np.random.randn(20))

# %%
out = s[s > 0] # usuwa wartosci nie spalniajace warunku

out = s.where(s > 0) # tam gdzie warunek nie jest spelniny wtawia nan

# %%
out = df[df > 0] # tutaj uzupelnia nan wartosci nie spalniajace

out = df.where(df > 0) # to dziala tak jak powyzej

out = df.where(df > 0, 'alabala') # zamiast nan wstawia zadana wartosc

out = df.where(df > 0, 0).where(df < 1, 1)

# %%
df 
































