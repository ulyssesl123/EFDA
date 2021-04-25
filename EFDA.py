#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import requests
import pandas as pd
import yfinance as yf
import datetime
import time
import requests
import io
from pandas_datareader import data as pdr
from yahoo_fin.stock_info import*


# In[ ]:


get_ipython().system('pip install pulp')


# In[ ]:


get_ipython().system('pip install PyPortfolioOpt')


# In[ ]:


get_ipython().system('pip install cvxopt')


# In[ ]:


conda install -c conda-forge cvxpy


# In[ ]:


get_ipython().system('pip install gl')


# In[ ]:


get_ipython().system('pip install cvxpy')


# In[ ]:


#conda install -c conda-forge glpk


# In[ ]:


company_1 = input("Enter the ticker symbol for the company: ").upper()
company_2 = input("Enter the ticker symbol for the company: ")
company_3 = input("Enter the ticker symbol for the company: ")
company_4 = input("Enter the ticker symbol for the company: ")
company_5 = input("Enter the ticker symbol for the company: ")
company_6 = input("Enter the ticker symbol for the company: ")
company_7 = input("Enter the ticker symbol for the company: ")
company_8 = input("Enter the ticker symbol for the company: ")
company_9 = input("Enter the ticker symbol for the company: ")
company_10 = input("Enter the ticker symbol for the company: ")


# In[ ]:


ticker_list = [company_1, company_2, company_3, company_4, company_5, company_6, company_7, company_8, company_9, company_10]


# In[ ]:


yf.pdr_override()


# In[ ]:


data = pdr.get_data_yahoo([company_1, company_2, company_3, company_4, company_5, company_6, company_7, company_8, company_9, company_10], period='max')


# In[ ]:


data.drop(columns=['Volume','Close','Low','High','Open'], axis=1, inplace=True)


# In[ ]:


print(data)


# In[ ]:


assets = data.columns


# In[ ]:


from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns


# In[ ]:


mean = expected_returns.mean_historical_return(data)
S = risk_models.sample_cov(data)


# In[ ]:


ef = EfficientFrontier(mean, S)
weights  = ef.max_sharpe()
clean_weights  = ef.clean_weights()
print(clean_weights)
ef.portfolio_performance(verbose=True)


# In[ ]:


Investment_fund = float(input("Enter how much you want to invest: $"))


# In[ ]:


from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

portfolio_value = Investment_fund
latest_prices = get_latest_prices(data)
weights = clean_weights
da = DiscreteAllocation(weights, latest_prices, total_portfolio_value = portfolio_value)
allocation, leftover = da.lp_portfolio()
print('Discrete Allocation', allocation)
print('Remaining Funds: $',leftover)


# In[ ]:


discrete_allocation_list = []
for symbol in allocation:
    discrete_allocation_list.append(allocation.get(symbol))


# In[ ]:


portfolio_df = pd.DataFrame(columns=['Company_Ticker', 'Discrete_value_' +str(portfolio_value)])


# In[ ]:


portfolio_df['Company_Ticker'] = allocation
portfolio_df['Discrete_value' +str(portfolio_value)] = discrete_allocation_list


# In[ ]:


portfolio_df


# In[ ]:


import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 400


# In[ ]:


data.describe()


# In[ ]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


((data.pct_change()+1).cumprod()).plot(figsize=(10,7))

plt.legend()

plt.title("Returns", fontsize=16)

plt.ylabel('Cumulative Returns', fontsize=14)

plt.grid(which="major", color='k', linestyle='-.', linewidth=.05)


# In[ ]:


data =  yf.download(ticker_list,'2017-1-1')['Adj Close']


# In[ ]:


((data.pct_change()+1).cumprod()).plot(figsize=(10,7))

plt.legend()

plt.title("Returns", fontsize=16)

plt.ylabel('Cumulative Returns', fontsize=14)

plt.grid(which="major", color='k', linestyle='-.', linewidth=.05)


# In[ ]:


data.shape


# In[ ]:


get_income_statement(company_1)


# In[ ]:


get_quote_table(company_1)


# In[ ]:


get_quote_table(company_2)


# In[ ]:


from bs4 import BeautifulSoup


# In[ ]:


soup = BeautifulSoup("Beta")


# In[ ]:




