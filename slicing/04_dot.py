# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


# %%
df = pd.DataFrame(np.random.randn(20, 5),
                  columns=list('ABCDE'),
                  index=list('abcdefghijklmnoprstu'))

# %%
col_A = df.A

mask = df.A > 0

out = df[mask]

# %%
out = df[df.A > 0]

# %%
mask = (df.A > 0) & (df.C > 0) # dla obiektow z pandas zamiast slowa and uzywamy &

out = df[mask]

# %%

out = df[(df.A > 0) & (df.C > 0)]

# %%

out = df[(df.A > 0) | (df.C > 0)] # or to znak |



























