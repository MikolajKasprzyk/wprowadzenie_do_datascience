# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()


# %% loading dataset - przykladowa baza do zabawy w bibliotece
tit = sns.load_dataset('titanic')

# %% grouping by sex and ploting
tit.groupby('sex').size().plot(kind='bar')

tit.groupby(['sex', 'survived']).size()

# %%
tit.groupby('class').size().plot(kind='bar')

tit.groupby('class').mean()['survived'].plot(kind='bar')

# %% tabela przestawna
r = pd.pivot_table(data=tit, values='survived', index='sex', 
                   columns='class', aggfunc='count')
# %% making variable age category and grouping by it
tit['age_bin'] = pd.cut(x=tit['age'], bins=[0, 18, 80])
pv = pd.pivot_table(data=tit, values='survived', index='age_bin', columns='class', aggfunc='count')

# %%
fig, ax = plt.subplots(1, 2, sharey=True)
tit.groupby(['sex', 'survived']).size()['male'].plot(ax=ax[0], kind='bar')
tit.groupby(['sex', 'survived']).size()['female'].plot(ax=ax[1], kind='bar')

ax[0].legend('male')
ax[1].legend('female')

# %%
pv = pd.pivot_table(data=tit, values='embarked', index='survived', columns='sex', aggfunc='count')
# values cos co jest wypełnione w kazdym przypafku, np age ma duzo brakujacych
pv.plot(subplots=False, kind='bar', sharey=True)

# %% jesli chcemy wiecej niz jedna funkcje agregacyjna podajemy je w slowniku
pd.pivot_table(data=tit, index='sex', columns='class', 
               aggfunc={'survived':sum, 'fare':'mean'})









































































