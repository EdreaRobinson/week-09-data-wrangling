import numpy as np
import pandas as pd

df=pd.read_csv('Mobile_Food_Facility_Permit.csv')
# print(df.head())

# ############ SELECTING AND INDEXING ###############

# BASICS

# print(df['Applicant'])
# print(df['Applicant'][44])
# print(df.Applicant) #don't use this syntax
#
dft = df.T
# print(dft)
# print(dft.columns)
# print(dft[44])
# print(dft[44]['FoodItems'])

# INDEXING WITH LISTS AND SLICES

# print(df[['Applicant', 'Address', 'FoodItems']])
# print(df['FoodItems'][[1,9,24,25,44,444]])
#
# print(df[100:106])
# print(df[100:106][['Applicant', 'Address', 'FoodItems']])
#
# print(df[607:])
# print(df[607:][['Applicant', 'Address', 'FoodItems']])
#
# print(df['Location'])
# print(df['Location'][:20])
#
# print(dft[:44])
# print(dft['Address':'FoodItems'])

# INDEXING USING LOC AND ILOC
# loc and iloc allow you to select rows, columns, or single cells
# the first one selects rows, the second one selects columns
# loc uses labels; iloc uses positions(integers)
# loc can use integers, but only if index labels are integers

capitals = pd.DataFrame(
    [
    ["Ngerulmud",391,1.87],
    ["Vatican City",826,100],
    ["Yaren",1100,10.91],
    ["Funafuti",4492,45.48],
    ["City of San Marino",4493]
    ],
    index = ["Palau", "Vatican City", "Nauru", "Tuvalu", "San Marino"],
    columns=['Capital', 'Population', 'Percentage'])

# print(capitals)
#
# print(capitals.loc['Nauru', 'Population']) #takes 1 operation and is preferred method
#
# print(capitals['Population']['Nauru']) #chained indexing - takes 2 operations
#
# print(capitals.loc['Palau':'Nauru', ['Population', 'Percentage']])
#
# print(capitals.loc[['San Marino', 'Vatican City']])
#
# print(capitals.iloc[[4,1]])
# print(capitals.iloc[[4,1], 1:])
#
# print(capitals.iloc[:,2])  #iloc allows you to select a column by position, which cannot be done with column-based indexing

############################# FILTERING ###########################

print(df['locationid'] < 1000000)
print(df[df['locationid']< 1000000])

print(df.sort_index())
print(df.sort_index(inplace=True))
print(df.sort_index(inplace=True, ascending=False))
print(df.sort_index(axis=1))

print(df.sort_values(by='FoodItems'))
print(df.sort_values(by=['FoodItems', 'Address']))