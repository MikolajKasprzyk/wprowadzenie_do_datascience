# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


# %%
df = pd.DataFrame(np.random.randn(10, 5),
                  columns=list('ABCDE'))

# %%
df.query('(A < B)')

# %%
df.query('(A > B) & (B < C)')

df.query('(A > B) | (B < C)')

# %%
df = df.round(1)

df.query('(C == [0.4, 0.3])')

df.query('[0.4] in C')

