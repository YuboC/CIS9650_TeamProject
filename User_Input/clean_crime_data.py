# Christopher Chong
# Professor Ali Koc
# CIS 9650
# 1 December 2019

# This file cleans the crime data file

import pandas as pd
import math

df = pd.read_csv('NYPD_Arrest_Data__Year_to_Date_.csv')
df = df.dropna()
df = df[['ARREST_BORO','Latitude','Longitude']]
df = df[df['ARREST_BORO'] == 'M']


zf = pd.read_csv('REAL_ZIPCODES.csv')
zf['ZIP'] = zf['ZIP'].astype(int)
zf = zf[(zf['ZIP'] > 9999) & (zf['ZIP'] < 10300)]
zf['ZIP'] = zf['ZIP'].astype(str)

correspondingZip = ''
correspondingZips = []

for i,j in df.iterrows():
    smallest = 999999999999999999999999999999999
    for p,q in zf.iterrows():
        distance = math.sqrt(math.pow((q['LAT'] - j['Latitude']), 2) + math.pow((q['LNG'] - j['Longitude']), 2))
        if distance < smallest:
            smallest = distance
            correspondingZip = q['ZIP']
    correspondingZips.append(correspondingZip)
    print(len(correspondingZips))
        
df['zipcode'] = correspondingZips

print(df)

df.to_csv('crime_for_final_project.csv', encoding='utf-8', index=False)