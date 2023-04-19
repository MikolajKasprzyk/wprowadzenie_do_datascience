# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# %%
idx = pd.Index(['8967', '9823', '1234', '3814'])

df = pd.DataFrame(np.random.randn(4, 5),
                  columns=list('ABCDE'),
                  index=idx)



















