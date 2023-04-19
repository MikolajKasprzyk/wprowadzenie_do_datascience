# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

# %%
tips = sns.load_dataset('tips')

# %%
tips.pivot_table(values='tip', index='sex', columns='day', aggfunc='mean')

pv = tips.pivot_table(values=['tip', 'total_bill'],
                 index='sex', columns='day', aggfunc='mean')

pv = tips.pivot_table(values='tip',
                 index='sex', columns='day', aggfunc='max')

pv = tips.pivot_table(values='tip',
                 index='sex', columns=['smoker', 'day'], aggfunc='mean')

# %%

tips.pivot_table(values='tip', index='sex', columns='day',
                 aggfunc='mean').plot(kind='bar', cmap='viridis', alpha=0.7)

# %%
tips.pivot_table(values='total_bill', index='sex', columns='day', 
                 aggfunc='mean').plot(kind='bar', cmap='viridis', alpha=0.7)
# %%
tips.pivot_table(values='tip', index='day', columns='size',
                 aggfunc='mean').plot(kind='bar', cmap='viridis', alpha=0.7)

# %%
tips.pivot_table(values='tip', index='time', columns='size',
                 aggfunc='mean').plot(kind='bar', cmap='viridis', alpha=0.7)

# %%
vals = tips[['total_bill', 'tip']]
vals.corr()













