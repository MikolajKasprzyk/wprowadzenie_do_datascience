# -*- coding: utf-8 -*-


import pandas as pd
import wget
import os
import zipfile
import seaborn as sns
sns.set()

# %%
url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/00275/'
       'Bike-Sharing-Dataset.zip')

wget.download(url) # pobiera podany adres do folderu roboczego, tyle ze to zip
# %% preprocessing
z = zipfile.ZipFile('Bike-Sharing-Dataset.zip')
z.extractall('./data')

# %%
day = pd.read_csv('./data/day.csv', index_col='dteday')
hour = pd.read_csv('./data/hour.csv', index_col='dteday')

# %%
hour.groupby('weekday').size().plot(kind='bar')
hour.groupby('hr').size().plot(kind='bar')



































