# -*- coding: utf-8 -*-

from pandas_datareader.stooq import StooqDailyReader
import pandas as pd


companies = {'MSFT.US': 'Microsoft Corporation', 'AAPL.US': 'Apple Inc.',
             'GOOGLE.US': 'Alphabet Inc.', 'META.US': 'Facebook', 'CSCO.US':
             'Cisco Systems', 'INTC.US': 'Intel Corporation', 'ORCL.US':
             'Oracle Corporation', 'SAP.US': 'SAP SE', 'CRM.US':
             'Salesforce.com Inc.', 'IBM.US': 'IBM Corporation',
             'NVDA.US': 'Nividia Corporation', 'VMW.US': 'Vmware, Inc.',
             'UBER.US': 'Uber Technologies', 'RHT.US': 'Red Hat, Inc.',
             'TEAM.US': 'Altassian Corporation', 'TWTR.US': 'Twitter, Inc.',
             }
    
# %%
tickers = sorted([ticker  for ticker in companies.keys()])

# %% pobieranie danych przy pomocy biblioteki datareader
df = StooqDailyReader(symbols='META.US').read()

# %%
def download_data(ticker):
    df = StooqDailyReader(symbols=ticker).read()
    cols = {col: col + '_' + ticker for col in df.columns}
    df = df.rename(columns=cols)
    return df

# %%
def create_dataframe(n=2):
    frames = []
    for ticker in tickers[:n]:
        df = download_data(ticker)
        frames.append(df)
    return pd.concat(frames, axis=1, join='outer')
        

# %%
big_df = create_dataframe(10)

# %%
close_col = [col for col in big_df.columns if col.startswith('Close')]
close_df = big_df[close_col]
c = close_df.corr()


