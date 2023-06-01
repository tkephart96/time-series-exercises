'''Prepare Time Series'''

##### IMPORTS #####

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import TimeSeriesSplit


##### FUNCTIONS #####

def prep_superstore(df):
    '''Prep superstore data'''
    # df.sale_date = df.sale_date.astype('datetime64') # takes too long
    # format datetime
    df.sale_date = df.sale_date.str.replace(' 00:00:00 GMT', '')
    df.sale_date = df.sale_date.str.strip()
    df.sale_date = pd.to_datetime(df.sale_date, format = '%a, %d %b %Y')
    # set date as index
    df = df.set_index('sale_date').sort_index()
    # create month and day of week columns
    df = df.assign(month=df.index.month,month_name=df.index.month_name(),day_of_week=df.index.day_name())
    # create total for sales
    df = df.assign(sales_total=(df.sale_amount * df.item_price))
    return df

def plt_dist(df,x):
    '''Plot distribution of x from df'''
    # reset index in case of non-unique index
    sns.histplot(data=df.reset_index(),x=x)
    plt.title(x)
    plt.show()

def prep_german_power(df):
    '''Prep german power data'''
    # format datetime
    df.Date = df.Date.astype('datetime64')
    # set date as index
    df = df.set_index('Date').sort_index()
    # create month and year columns
    df = df.assign(month=df.index.month_name(),year=df.index.year)
    # start first nulls as 0 for wind and solar
    df.loc[df.index==df.index.min(),['Wind','Solar']]=0
    # forward fill so that first nulls are 0, later nulls follow prev days
    df.Wind = df.Wind.ffill()
    df.Solar = df.Solar.ffill()
    # fill nulls with sum of wind and solar
    df['Wind+Solar'] = (df.Wind + df.Solar)
    return df