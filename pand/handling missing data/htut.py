#dropna()
# its used to remove the missing values

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
print(df.dropna(inplace=True)) #it will remove the rows which have any missing values
print(df.dropna(axis=0,inplace=True)) #axis 0 is used to remove the rows
print(df.dropna(axis=1)) #axis 1 is used to remove the columns
print(df)


#instead of removing we can fill the missing values with some value
print(df.fillna(0,inplace=True)) #it will fill the missing values with 0

#to fill the mean value in the place of missing values
df['age'].fillna(df['age'].mean(),inplace=True)
print(df)
#to fill the median value in the place of missing values
df['age'].fillna(df['age'].median(),inplace=True)
print(df)

#to fill the mode value in the place of missing values
df['age'].fillna(df['age'].mode()[0],inplace=True)
print(df)

#to fill the missing values with a specific value
df['age'].fillna("unknown",inplace=True)
