#removing colums
import pandas as pd
data={
    "name":[
        "ram",
        "jaswanth",
        "syam"
    ],
    "age":[20,21,19],
    "city":['hyd','bang','chennai']
}
df=pd.DataFrame(data)
print(df)
#to remove the column we use drop function
df.drop(columns=["age"],inplace=True) #inplace true is used for changing the original dataframe
#to remove multiple columns
#df.drop(columns=["age","city"],inplace=True)
print(df)
#to remove the row we use index
df.drop(index=0,inplace=True)
print(df)
#to remove multiple rows
#df.drop(index=[0,1],inplace=True)
#print(df)
# to remove rows based on condition
#df.drop(index=df[df["age"]>20].index,inplace=True)
#print(df)



