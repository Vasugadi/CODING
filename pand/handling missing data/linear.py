import pandas as pd

data={
    "Time":[
        1,2,3,4,5
    ],
    "Value":[10,None,30,None,50],
    
}


df=pd.DataFrame(data)
print("before interpolation")
print(df)
print("\n")
print("after interpolation")
df["Value"]=df["Value"].interpolate(method="linear")
print(df)

"""
    1-timer series data
    2-numeric data with trends
    3-data should be sorted
    4-avoid dropping missing values 

"""