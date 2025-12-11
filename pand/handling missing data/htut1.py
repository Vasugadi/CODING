#missing data
#what actually missing data is?
#null values
#NaN values NOT A NUMBER
#None values for object data type
#how to handle missing data?
#1. remove the missing data
#2. fill the missing data with some value
#3. fill the missing data with some statistical value like mean,median,mode
#4. fill the missing data with some forward value or backward value
#isnull() function is used to check the missing values 
#if true means missing value
#if false means non-missing value
#notnull() function is used to check the non-missing values
#if true means non-missing value
#if false means missing value
#dropna() function is used to remove the missing values
#fillna() function is used to fill the missing values


import pandas as pd

dict={
    "name":[
        "ram",
        "jaswanth",
        "syam",
        None
    ],
    "age":[20,21,19,None],
    "city":['hyd','bang','chennai',None]
}

df=pd.DataFrame(dict)
print(df)
print(df.isnull()) #boolean value
print(df.isnull().sum()) #count of missing values in each column


print(df.notnull())
print(df.dropna())
print(df.fillna(0))
# print(df.fillna(method='ffill'))
# print(df.fillna(method='bfill'))
