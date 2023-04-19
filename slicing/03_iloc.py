# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


# %%
df = pd.DataFrame(np.random.randn(20, 5),
                  columns=list('ABCDE'),
                  index=list('abcdefghijklmnoprstu'))

# %%
col_0 = df.iloc[:, 0]

col_A_B = df.iloc[:, 0:2] # indeks 2 juz nie wchodzi
col_A_B_C = df.iloc[:, [0, 1, 2]]

# %%
row_0 = df.iloc[0, :] # series
row_0 = df.iloc[[0], :] # DataFrame

# %%
df_ = df.iloc[[0, -1], [0, -1]]



























