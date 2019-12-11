import pandas as pd

#read to dataframe
crimeDf = pd.read_csv('CrimeAnalysis.csv')
healthDf = pd.read_csv('HospitalAnalysis.csv', dtype={'ZIP CODE': int})
housingDf= pd.read_csv('HousingSalesAnalysis.csv', dtype={'ZIP CODE': int})

crimeDf = crimeDf.rename(columns={"ARREST_BORO": "Crime Count"})
healthDf = healthDf.rename(columns={"Facility Name": "Hospital Count"})

#count num of medical facilities and crime
healthDf = healthDf.groupby('ZIP CODE')['Hospital Count'].count()
crimeDf = crimeDf.groupby('ZIP CODE')["Crime Count"].count()


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
sns.lmplot(x='Crime Count',y='Hospital Count',data=CrimeHealth,fit_reg=True) 

#no correlation between hospital count and rental prices
sns.lmplot(x='Hospital Count',y='Rental Price',data=RentHealth,fit_reg=True) 

#As crime rates increases rental price decreases
sns.lmplot(x='Crime Count',y='Rental Price',data=CrimeRent,fit_reg=True) 

print('Hospital Count vs Crime Count-', CrimeHealth['Hospital Count'].corr(CrimeHealth['Crime Count']))
print('Hospital Count vs Rental Price-', RentHealth['Hospital Count'].corr(RentHealth['Rental Price']))
print('Crime Count vs Rental Price-', CrimeRent['Crime Count'].corr(CrimeRent['Rental Price']))