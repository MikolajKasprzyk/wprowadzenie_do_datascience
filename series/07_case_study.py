# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


# creating a Series
list_of_wig20_stocks = ['Alior', 'CCC', 'CD Projekt', 'Cyfrowy Polsat', 'Dino',
                        'JSW', 'KGHM', 'Lotos', 'LPP', 'mBank', 'Orange',
                        'PEKAO SA', 'PGE', 'PGNIG', 'PKN ORLEN', 'PKO BP',
                        'PLAY', 'PZU', 'Santander', 'Tauron']

wig20 = pd.Series(list_of_wig20_stocks, name='WIG20')

# %%
wig20_names = wig20.apply(lambda word: word.upper())

wig20_names.isin(['CCC'])
wig20_names[wig20_names.isin(['CCC'])]

wig20_names[wig20_names.isin(['CCC', 'PGE'])]

for company in wig20_names:
    print(company)
    
for company in wig20_names:
    company += '_PLN'
    print(company)
    
# %%
stocks_len_4 = pd.Series([item for item in wig20_names if len(item) == 4])

stocks_replace = pd.Series([company.replace(' ', '_') for company in wig20_names])



























