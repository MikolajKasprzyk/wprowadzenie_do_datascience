# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


np.random.seed(0)

A = np.random.randint(0, 10, 10)
series = pd.Series(A, name='los')

# %%
series.dtype # typ danych
series.iloc[3] # wycinanie elementu z indeksem 3, w sumie to samo co sam nawias
series.iloc[-1]
series.index
series.name
series.shape

array_A = series.values

# %%
N = np.random.randn(10)
M = np.random.randn(10)

series_N = pd.Series(N)
series_M = pd.Series(M)

# %% basic methods

series_N.abs() # zwraca wartosci bezwzględne
series_N.add(series_M)
series_N.subtract(series_M)
series_N.divide(series_M)
series.drop_duplicates() # usuwa duplikaty

series[4] = np.nan
series.dropna() # usuwa wartosci nan

series.idxmax() # zwraca indeks najwyższej wartosci
series.idxmin() # indek m=najmniejszej wartosci
series.count() # zlicza wartosci 

series_N.cumsum() # zwraca po kolei sumę z kolumny
series_M.cummin() # zwraca minimum z kolejnych elementow kolumny
series_M.cummax()

series.value_counts() # zwraca czestosc wystapienia wartosci i od razu sortuje

series.sum()
series.std() # odchylenie standardowe
series.describe() # podstawowe dane statystyczne

# %% histogram
hist_data = pd.Series(np.random.randn(10000))
hist_data.hist(bins=80, color='red')

# %%
top_3 = series_N.nlargest(3)

bottom_3 = series_N.nsmallest(3)

q_1 = series_N.quantile(0.25)
q_2 = series_N.quantile(0.5)

series_N.round(3)

# %%
shift_1 = series.shift(1)
shift_replace = series.shift(2).fillna(0) # przesuwa i uzupelnia zerami wart nan

# %%
sorted_series = series.sort_values(ascending=False)

























