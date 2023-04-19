# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

d1 = {'date': ['2019-01-01', '2019-01-01', '2019-01-02', '2019-01-02'],
      'id_trans': ['0001', '0002', '0003', '0004'],
      'product_id': ['343', '523', '151', '522']}

d2 = {'date': ['2019-01-01', '2019-01-02', '2019-01-02', '2019-01-03'],
      'id_trans': ['0001', '0002', '0003', '0004'],
      'price': ['99', '149', '59', '199']}

left = pd.DataFrame(d1)
right = pd.DataFrame(d2)

# %% inner
df_inner = pd.merge(left, right, on=['date', 'id_trans'])

# %% outer
df_outer = pd.merge(left, right, how='outer')

# %% left
df_left = pd.merge(left, right, how='left', on=['date', 'id_trans'])

# %% right
df_right = pd.merge(left, right, how='right', on=['date', 'id_trans'])