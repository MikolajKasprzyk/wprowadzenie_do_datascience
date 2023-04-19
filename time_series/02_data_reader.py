# -*- coding: utf-8 -*-

import pandas as pd
from pandas_datareader.data import DataReader
import matplotlib.pyplot as plt
import seaborn as sns
sns.set() # ustawienie domyslnego stylu z biblioteki seaborn


# %%
# DataReader importuje dane dane dla amazon z serwisu stooq
amazon = DataReader('AMZN', 'stooq')
amazon.to_csv('data/data.csv') 
# zapisujemy lokalnie bo serwisy moga dać blokade
# jeli za dużo na raz sie sciąga

# %%
# wycianmy cene close i robimy wykres tej ceny
amazon['Close'].plot()
amazon['Close'].plot(alpha=0.5)

# %%
amazon['Close'].plot(alpha=0.7)
# wycinamy probki danych z czestotliwoscia BQ - business quarter i liczymy 
# rednią (mean) w tych kwartałach
amazon.resample('BQ').mean()['Close'].\
       plot(color='green', style='--', alpha=0.7)

plt.legend(['price', 'quarter average'])

# %% shifting
# metoda subplot z biblioteki matplotlib.pyplot
fig, ax = plt.subplots(3, sharex=True)

amazon['Close'].plot(ax=ax[0])
amazon['Close'].shift(365).plot(ax=ax[1]) # przesuniete 365 okresow do tylu
amazon['Close'].shift(-365).plot(ax=ax[2]) # przesuniete 365 okresow do przodu

ax[0].legend(['input'])
ax[1].legend(['shift by 365'])
ax[2].legend(['shift by -365'])

# %% ROI
ROI = 100 * (amazon.shift(15) / amazon - 1)
ROI['Close'].plot()

# %% rolling windows
amazon = amazon.sort_index() # dla pewnosci sortujemy po indeksie


fig, ax = plt.subplots(2, sharex=True)
amazon['Close'].plot(ax=ax[0])
amazon['Close'].rolling(120).mean().plot(ax=ax[0], logy=True)
amazon['Close'].rolling(16).std().plot(ax=ax[1], logy=True)

ax[0].legend(['price', 'rolling_mean'])
ax[1].legend(['rolling_std'])