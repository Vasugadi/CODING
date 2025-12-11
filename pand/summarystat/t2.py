import pandas as pd
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

df['price'].mean()
df['price'].sum()
df['price'].min()
df['price'].max()
df['price'].median()
df['price'].mode()
df['price'].var()
df['price'].std()
df['price'].describe()
df['price'].skew()#positive skewness
df['price'].kurt()#leptokurtic
df['price'].quantile(0.25)#Q1
df['price'].quantile(0.50)#Q2
df['price'].quantile(0.75)#Q3
