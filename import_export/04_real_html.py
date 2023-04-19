# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# %%
# domyslnie zwaraca liste DataFrame
df = pd.read_html('./data/small.html', header=0, index_col=0)[0]

# %%
# wczytywanie tabeli ze strony internetowej
df = pd.read_html('https://www.biznesradar.pl/gielda/indeks:WIG20')[0]





































