# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# %%
df = pd.read_clipboard()

# %%
df.columns = [col.strip() for col in df.columns]

# %%
df = df.drop(['Czas', '1r 3m'], axis=1)

# %%
df['Wolumen'] = df['Wolumen'].apply(lambda x: int(x.replace(' ', '')))

df['Obrót'] = df['Obrót'].apply(lambda x: int(x.replace(' ', '')))

df['Udział'] = df['Udział'].apply(lambda x: float(x.replace('%', '')))

df['Zmiana %'] = df['Zmiana %'].apply(lambda x: float(x.replace('%', '')[1:-2]))



















