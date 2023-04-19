# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)

# %% select first n rows
first_50_rows = df.iloc[0:50]
rows_10_70 = df.iloc[10:70]

some_rows_some_columns = df.iloc[[0,10,30], [0,2,4]]

every_second_row = df.iloc[::2]
