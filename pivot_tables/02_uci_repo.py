# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/00492/'
       'Metro_Interstate_Traffic_Volume.csv.gz')
# %%
metro = pd.read_csv(url, compression='gzip', 
                    index_col='date_time', parse_dates=True)
# parse_dates robi to ze daty sa formatem daty a nie string
metro = metro.loc['2016-01-01':] #wycinamy kawałek danych dla latwosci dzialania
# %% plotting traffic
traffic = metro.iloc[:, -1]
#poniżej resamplujemy z czestotliwoscia misiac sumujac dane dla kazdego miesiaca
tr = traffic.resample('M').sum()
tr.plot()

# %% pivot tables
pd.pivot_table(data=metro, values='traffic_volume', 
               index='weather_main').plot(kind='bar')




















