import pandas as pd

df_Customers= pd.DataFrame({
    'CustomerID':[1,2,3,4],
    'CustomerName':['John','Jane','Jim','Jack']
})

df_Orders= pd.DataFrame({
    
    'CustomerID':[5,2,6,4],
    'Order Amount':[100,200,150,300]
    
})
#inner join-----common values
#outer join-----all the values from both the dataframes 
#left join-----all the values from left dataframe
#right join-----all the values from right dataframe
merged=pd.merge(df_Customers,df_Orders,on='CustomerID',how='inner')
mer=pd.merge(df_Customers,df_Orders,on='CustomerID',how='outer')
print(merged)
print(mer)
#m rows n rows 
#cross join----m*n rows
cross=pd.merge(df_Customers,df_Orders,on='CustomerID',how='cross')
print(cross)

#concatenating is nothing but stacking the data vertically or horizontally