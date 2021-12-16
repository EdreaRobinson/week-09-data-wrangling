import numpy as np
import pandas as pd

df=pd.read_csv('Mobile_Food_Facility_Permit.csv')
print(df.info())

print(df[['NOISent', 'dayshours', 'Approved']].head(20))

print(df.isnull())
print(df.isnull().any)
print(df.isnull().any(axis=1))
print(df.isnull().all)
print(df.isnull().all(axis=1))
print(df.isnull().all(axis=1).any()) #check for completely empty rows

print(df.notnull().all())


print(df.drop(columns='NOISent', inplace=True))

print(df.duplicated().any)

df.drop_duplicates(inplace=True)

print(df[['permit', 'Schedule', 'lot']])
print(df[['blocklot', 'block', 'Zip Codes']])

new_df = df['Zip Codes'].dropna()
print(new_df.to_string())

# df['Zip Codes'] = df['Zip Codes'].fillna(0, inplace=True)
# df['Zip Codes'].astype('int64')
# print(df['Zip Codes'].to_string())