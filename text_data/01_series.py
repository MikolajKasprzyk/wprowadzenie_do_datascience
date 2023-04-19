# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

s = pd.Series(['Apple', '   Microsoft', np.nan, '   Google   ', 'Anazon'],
              name='stock')

# %%
s = s.str.strip()
s = s.str.upper()

s_num = s.str.len()


# %%
df = pd.DataFrame(np.random.randn(10, 2),
                  columns=['                           ID User   ', '    Price   '])

# %%
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(' ', '_')

# %%

                  
































