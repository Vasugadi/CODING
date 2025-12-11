import pandas as pd

#create the sales data for pizza with 6 col and 5 rows

data={
    "OrderID":[1,2,3,4,5],
    "CustomerID":[101,102,103,104,105],
    "Item":["Pizza","Burger","Pizza","Pasta","Pizza"],
    "Quantity":[2,1,3,2,1],
    "Price":[20.5,10.0,30.75,15.0
,25.0],
    "Total":[41.0,10.0,91.25,30.0,25.0]
}

df=pd.DataFrame(data)

print(df)

print(df.describe())

print(df.info())

print(df.head())

print(df.tail())

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.index)

print(df.values)

print(df['Item'])

print(df[['Item','Price']])

# print(df.iloc[0])

# print(df.iloc[0:3])

# print(df.loc[0])

# print(df.loc[0:3])