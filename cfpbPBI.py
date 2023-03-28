# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 15:02:23 2023

@author: MWatson717
"""

import pandas as pd

p = pd.read_csv('complaints.csv')


p['Product'] = p['Product'].replace(['Credit reporting', 'Credit card', 'Payday loan', 
                                     'Money transfers', 'Prepaid card', 'Virtual currency'],
                                    
                                    ['Credit reporting, credit repair services, or other personal consumer reports',
                                     'Credit card or prepaid card', 'Payday loan, title loan, or personal loan',
                                     'Money transfer, virtual currency, or money service', 'Credit card or prepaid card',
                                     'Money transfer, virtual currency, or money service'])


tr = ['(CD) Certificate of deposit',
      'Auto debt',
      'Check cashing service',
      'Credit card debt',
      'Credit repair services',
      'Federal student loan servicing',
      'Federal student loan debt',
      'General purpose card',
      'General-purpose prepaid card',
      'Gift card',
      'Home equity loan or line of credit (HELOC)',
      'Medical debt',
      'Other bank product/service',
      'Payday loan debt',
      'Private student loan debt',
      'Traveler’s/Cashier’s checks']

rw = ['CD (Certificate of Deposit)',
      'Auto',
      'Check cashing',
      'Credit card',
      'Credit repair',
      'Federal student loan',
      'Federal student loan',
      'General-purpose credit card or charge card',
      'General-purpose credit card or charge card',
      'Gift or merchant card',
      'Home equity loan or line of credit',
      'Medical',
      'Other banking product or service',
      'Payday loan',
      'Private student loan',
      "Traveler's check or cashier's check"]

p['Sub-product'] = p['Sub-product'].replace(tr, rw)


data = p[['Date received', 'Product', 'Sub-product', 'Company', 'State']]


states = ['AA', 'AE', 'AP', 'AS', 'FM', 'GU', 'MH', 'MP', 'PR', 'PW',
          'UNITED STATES MINOR OUTLYING ISLANDS', 'VI', 'AK', 'HI']

data2 = data[~data['State'].isin(states)] #3458757

data2.isnull().sum() #missing 41127 states

data2 = data2[data2['State'].notna()] #works, left with 3417630, 

data2.isnull().sum()

data2['Sub-product'] = data2['Sub-product'].fillna('(Blank)')

data2.isnull().sum()

data2['Year']  = pd.DatetimeIndex(data2['Date received']).year
data2['Month'] = pd.DatetimeIndex(data2['Date received']).month


panel1 = data2.groupby(by=['Year', 'Month', 'Product', 'Sub-product'], as_index=False).agg(Count=('Product', 'count'))

panel2 = data2.groupby(by=['Year', 'State', 'Product'], as_index=False).agg(Count=('Product', 'count'))

panel3 = data2.groupby(by=['Year', 'Company', 'Product'], as_index=False).agg(Count=('Product', 'count'))

panel1.to_csv('panel1.csv', index=False)
panel2.to_csv('panel2.csv', index=False)
panel3.to_csv('panel3.csv', index=False)

data.to_csv('CFPB_pbi_32823.csv', index=False)
