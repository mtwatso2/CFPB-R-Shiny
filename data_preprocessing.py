# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:05:57 2020

@author: MWatson717
"""

#Code for Project Milestone

import pandas as pd
import matplotlib.pyplot as plt
import operator


p = pd.read_csv('complaints2.csv')


####### 5/28 Lookikng at companies??? ###############

p['Company'].value_counts()[:10].sum()

comp = p['Company'].value_counts()[:10]

lst = comp.index.to_list()

p2 = p[p.Company.isin(lst)]

c = p2[['Date received', 'Product', 'Company']]

c['Year'] = pd.DatetimeIndex(c['Date received']).year

c['Month'] = pd.DatetimeIndex(c['Date received']).month

c2 = pd.crosstab([c.Year, c.Month, c.Company], c.Product)

c2 = c2.reset_index()

c2['Total'] = c2.iloc[:, 3:].sum(axis=1)

c2['Credit card or prepaid card'] = c2['Credit card or prepaid card'] + c2['Credit card'] + c2['Prepaid card']

c2['Checking or savings account'] = c2['Checking or savings account'] + c2['Bank account or service']

c2['Payday loan, title loan, or personal loan'] = c2['Payday loan, title loan, or personal loan'] + c2['Consumer Loan'] + c2['Payday loan']

c2['Credit reporting, credit repair services, or other personal consumer reports'] = c2['Credit reporting'] + c2['Credit reporting, credit repair services, or other personal consumer reports'] + c2['Other financial service']

c2['Money transfer, virtual currency, or money service'] = c2['Money transfer, virtual currency, or money service'] + c2['Money transfers'] 

vars_to_drop = ['Credit card', 'Prepaid card', 'Bank account or service', 'Consumer Loan', 'Payday loan',
                'Credit reporting', 'Other financial service', 'Money transfers']

c2 = c2.drop(columns = vars_to_drop)

######### Data for Line/Bar plots #############

time = p[['Date received', 'Product']]

time['Year'] = pd.DatetimeIndex(time['Date received']).year

time['Month'] = pd.DatetimeIndex(time['Date received']).month

time2 = pd.crosstab([time.Year, time.Month], time.Product)

time2 = time2.reset_index()

time2['Total'] = time2.iloc[:, 2:].sum(axis=1)

time2['Credit card or prepaid card'] = time2['Credit card or prepaid card'] + time2['Credit card'] + time2['Prepaid card']

time2['Checking or savings account'] = time2['Checking or savings account'] + time2['Bank account or service']

time2['Payday loan, title loan, or personal loan'] = time2['Payday loan, title loan, or personal loan'] + time2['Consumer Loan'] + time2['Payday loan']

time2['Credit reporting, credit repair services, or other personal consumer reports'] = time2['Credit reporting'] + time2['Credit reporting, credit repair services, or other personal consumer reports'] + time2['Other financial service']

time2['Money transfer, virtual currency, or money service'] = time2['Money transfer, virtual currency, or money service'] + time2['Money transfers'] + time2['Virtual currency']

vars_to_drop = ['Credit card', 'Prepaid card', 'Bank account or service', 'Consumer Loan', 'Payday loan',
                'Credit reporting', 'Other financial service', 'Money transfers', 'Virtual currency']

time2 = time2.drop(columns = vars_to_drop)

c2 = c2.append(time2)

c2 = c2.fillna("All")

#c2.to_csv('panel1.csv', index=False)


######## Data for Map visualization: All Years/Companies ###########

mapData = pd.crosstab(p.State, p.Product)

mapData = mapData.drop(['AA', 'AE', 'AP', 'AS', 'FM', 'GU', 'MH', 'MP', 'PR', 'PW', 'UNITED STATES MINOR OUTLYING ISLANDS', 'VI'], axis=0)

mapData['Credit card or prepaid card'] = mapData['Credit card or prepaid card'] + mapData['Credit card'] + mapData['Prepaid card']

mapData['Checking or savings account'] = mapData['Checking or savings account'] + mapData['Bank account or service']

mapData['Payday loan, title loan, or personal loan'] = mapData['Payday loan, title loan, or personal loan'] + mapData['Consumer Loan'] + mapData['Payday loan']

mapData['Credit reporting, credit repair services, or other personal consumer reports'] = mapData['Credit reporting'] + mapData['Credit reporting, credit repair services, or other personal consumer reports'] + mapData['Other financial service']

mapData['Money transfer, virtual currency, or money service'] = mapData['Money transfer, virtual currency, or money service'] + mapData['Money transfers'] + mapData['Virtual currency']

mapData = mapData.drop(columns = vars_to_drop)

mapData['Total'] = mapData.iloc[:, 0:10].sum(axis=1)

mapData = mapData.reset_index()

mapData['State'] = mapData['State'].astype(str)


#######Data for Map and Bar chart

p['Year'] = pd.DatetimeIndex(p['Date received']).year

mbData = pd.crosstab([p.State, p.Year], p.Product)

mbData = mbData.drop(['AA', 'AE', 'AP', 'AS', 'FM', 'GU', 'MH', 'MP', 'PR', 'PW', 'UNITED STATES MINOR OUTLYING ISLANDS', 'VI'], axis=0)

mbData['Credit card or prepaid card'] = mbData['Credit card or prepaid card'] + mbData['Credit card'] + mbData['Prepaid card']

mbData['Checking or savings account'] = mbData['Checking or savings account'] + mbData['Bank account or service']

mbData['Payday loan, title loan, or personal loan'] = mbData['Payday loan, title loan, or personal loan'] + mbData['Consumer Loan'] + mbData['Payday loan']

mbData['Credit reporting, credit repair services, or other personal consumer reports'] = mbData['Credit reporting'] + mbData['Credit reporting, credit repair services, or other personal consumer reports'] + mbData['Other financial service']

mbData['Money transfer, virtual currency, or money service'] = mbData['Money transfer, virtual currency, or money service'] + mbData['Money transfers'] + mbData['Virtual currency']

mbData = mbData.drop(columns = vars_to_drop)

mbData['Total'] = mbData.iloc[:, 0:10].sum(axis=1)

mbData = mbData.reset_index()

mbData['Year'] = mbData['Year'].astype('str')

mbData = mbData.append(mapData)

mbData = mbData.fillna("All")


###### Data for companies ###########
p2['Year'] = pd.DatetimeIndex(p2['Date received']).year

cd = pd.crosstab([p2.State, p2.Company, p2.Year], p2.Product)

cd = cd.drop(['AA', 'AE', 'AP', 'AS', 'FM', 'GU', 'MH', 'MP', 'PR', 'PW', 'UNITED STATES MINOR OUTLYING ISLANDS', 'VI'], axis=0)

cd['Credit card or prepaid card'] = cd['Credit card or prepaid card'] + cd['Credit card'] + cd['Prepaid card']

cd['Checking or savings account'] = cd['Checking or savings account'] + cd['Bank account or service']

cd['Payday loan, title loan, or personal loan'] = cd['Payday loan, title loan, or personal loan'] + cd['Consumer Loan'] + cd['Payday loan']

cd['Credit reporting, credit repair services, or other personal consumer reports'] = cd['Credit reporting'] + cd['Credit reporting, credit repair services, or other personal consumer reports'] + cd['Other financial service']

cd['Money transfer, virtual currency, or money service'] = cd['Money transfer, virtual currency, or money service'] + cd['Money transfers'] 

vars_to_drop = ['Credit card', 'Prepaid card', 'Bank account or service', 'Consumer Loan', 'Payday loan',
                'Credit reporting', 'Other financial service', 'Money transfers']

cd = cd.drop(columns = vars_to_drop)

cd['Total'] = cd.iloc[:, 0:10].sum(axis=1)

cd = cd.reset_index()

cd2 = pd.crosstab([p2.State, p2.Company], p2.Product)

cd2 = cd2.drop(['AA', 'AE', 'AP', 'AS', 'FM', 'GU', 'MH', 'MP', 'PR', 'PW', 'UNITED STATES MINOR OUTLYING ISLANDS', 'VI'], axis=0)

cd2['Credit card or prepaid card'] = cd2['Credit card or prepaid card'] + cd2['Credit card'] + cd2['Prepaid card']

cd2['Checking or savings account'] = cd2['Checking or savings account'] + cd2['Bank account or service']

cd2['Payday loan, title loan, or personal loan'] = cd2['Payday loan, title loan, or personal loan'] + cd2['Consumer Loan'] + cd2['Payday loan']

cd2['Credit reporting, credit repair services, or other personal consumer reports'] = cd2['Credit reporting'] + cd2['Credit reporting, credit repair services, or other personal consumer reports'] + cd2['Other financial service']

cd2['Money transfer, virtual currency, or money service'] = cd2['Money transfer, virtual currency, or money service'] + cd2['Money transfers'] 

cd2 = cd2.drop(columns = vars_to_drop)

cd2['Total'] = cd2.iloc[:, 0:10].sum(axis=1)

cd2 = cd2.reset_index()

cd2['Year'] = 'All'

cd = cd.append(cd2)

cd = cd.append(mbData)

cd = cd.fillna("All")

cd = cd.drop('Virtual currency', axis=1)

#cd.to_csv('panel2.csv', index=False)



############# Data with new categories for complaint type #################

lda = pd.read_csv('complaints_5000_LDA.csv')

lda2 = lda[['Date received', 'State', 'LDA_Topic']]

nonstates = ['AE', 'AP', 'AS', 'GU', 'PR', 'VI']

for i in nonstates:
    lda2 = lda2[lda2.State != i]

lda2['Year'] = pd.DatetimeIndex(lda2['Date received']).year

lda_ct1 = pd.crosstab([lda2.Year, lda2.State], lda2.LDA_Topic)

lda_ct1['Total'] = lda_ct1.iloc[:, 0:3].sum(axis=1)

lda_ct1 = lda_ct1.reset_index()

lda_ct2 = pd.crosstab(lda2.State, lda2.LDA_Topic)

lda_ct2['Year'] = 'All'

lda_ct2['Total'] = lda_ct2.iloc[:, 0:3].sum(axis=1)

lda_ct2 = lda_ct2.reset_index()

lda3 = lda_ct1.append(lda_ct2)

#lda3.to_csv('map2.csv', index = False)

