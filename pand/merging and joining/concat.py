import pandas as pd

df_reional=pd.DataFrame({
    "customer_id":[1,2,3,4],
    "customer_name":["john","jane","jack","jim"],
})

df_sales=pd.DataFrame({
    "customer_id":[1,2,3,4],
    "sales":[100,200,300,400]
})

# df=pd.concat([df_reional,df_sales],axis=1)
# print(df)

df=pd.concat([df_reional,df_sales],axis=0)
print(df)