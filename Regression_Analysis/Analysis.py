#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

#read to dataframe
crimeDf = pd.read_csv('crime_for_final_project.csv')
healthDf = pd.read_csv('healthFacilityData.csv', dtype={'ZIP CODE': int})
housingDf= pd.read_csv('Rollingsales1.csv', dtype={'ZIP CODE': int})

crimeDf = crimeDf.rename(columns={"ARREST_BORO": "Arrest Count"})
healthDf = healthDf.rename(columns={"Facility Name": "Facility Count"})

#count num of medical facilities and crime
crimeDf.info()
healthDf = healthDf.groupby('ZIP CODE')['Facility Count'].count()
crimeDf = crimeDf.groupby('ZIP CODE')["Arrest Count"].count()


#filter out nonresidential units

housingDf = housingDf.dropna(subset=['ZIP CODE'])
housingDf = housingDf[housingDf["SALE PRICE"] > 50000]
housingDf = housingDf[housingDf['SALE PRICE'] < 50000000]
housingDf = housingDf[housingDf['RESIDENTIAL UNITS'] > 3]

#divide by residental unit
housingDf["Avg House Price"] = housingDf["SALE PRICE"]/housingDf['RESIDENTIAL UNITS']

#compute rental prices for each zipcode
housingDf["Rental Price"] = housingDf["Avg House Price"] * .06

housingDf = housingDf.groupby('ZIP CODE')["Rental Price"].median()



import seaborn as sns


CrimeRent = pd.merge(crimeDf, housingDf, on='ZIP CODE')
RentHealth = pd.merge(healthDf, housingDf, on='ZIP CODE')
CrimeHealth = pd.merge(healthDf, crimeDf, on='ZIP CODE')

#no correlation between hospital count and number of arrest
sns.lmplot(x='Facility Count',y='Arrest Count',data=CrimeHealth,fit_reg=True) 

#no correlation between hospital count and rental prices
sns.lmplot(x='Facility Count',y='Rental Price',data=RentHealth,fit_reg=True) 

#As crime rates increases rental price decreases
sns.lmplot(x='Arrest Count',y='Rental Price',data=CrimeRent,fit_reg=True) 


# In[ ]:




