# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import pytz # biblioteka ze strefami czasowymi

"""
Symbol  |  Meaning
------------------
D - Calendar Day
B - Business Day
W - Weekly
M - Month End
MS - Month Start
BM - Business Month End
BMS - Business Month Start
Q - Quarter End
QS - Quarter Start
BQ - Business Quarter End
BQS - Business Quarter Start
A - Year End
AS - Year Start
BA - Business Year End
BAS - Business Year Start
H - Hours
BH - Business Hours
T - Minutes
S - Seconds
L - Miliseconds
U - Microseconds
N - Nanoseconds
offset:
-------
QS-FEB
A-MAR
W-MON
"""

# %% creating DatetimeIndex object
# default frequency: day
rng = pd.date_range('2019-01-01', periods=100)

rng = pd.date_range('2019-01-01', periods=100, freq='S')
rng = pd.date_range('2019-01-01', periods=100, freq='M')
rng = pd.date_range('2019-01-01', periods=100, freq='MS')
rng = pd.date_range('2019-01-01', periods=100, freq='3M')
rng = pd.date_range('2019-01-01', periods=100, freq='H')
rng = pd.date_range('2019-01-01', periods=100, freq='6H')
rng = pd.date_range('2019-01-01', periods=100, freq='B')
rng = pd.date_range('2019-01-01', periods=100, freq='Q')
rng = pd.date_range('2019-01-01', periods=100, freq='QS')
rng = pd.date_range('2019-01-01', periods=100, freq='MIN')
rng = pd.date_range('2019-01-01', periods=100, freq='T')
rng = pd.date_range('2019-01-01', periods=100, freq='W')
rng = pd.date_range('2019-01-01', periods=100, freq='A')
rng = pd.date_range('2019-01-01', periods=100, freq='QS-FEB')
rng = pd.date_range('2019-01-01', periods=100, freq='W-MON')
rng = pd.date_range('2019-01-01', periods=100, freq='2H30T')

# %% getting all avilable time zones
time_zones = list(pytz.all_timezones)
europe = [tz for tz in time_zones if tz.startswith('Europe')]
# %% date range with Europe/Warsaw time
rng = pd.date_range('2019-01-01', periods=100, tz='Europe/Warsaw', freq='MS')

us = rng.tz_convert(tz='US/Central')
# %%
rng = pd.date_range('2019-01-01', periods=100, freq='MIN', tz='Europe/Warsaw')
ts = pd.Series(np.random.rand(100), index=rng)
ts_period = ts.to_period()

ts_period.plot()

# %% resample method
ts_sample = ts.resample('5MIN').sum()


































