import pandas as pd

data={
    "name":[
        "ram",
        "jaswanth",
        "syam",
        None
    ],
    "age":[20,21,None,19],
    "city":['hyd','bang',None,'chennai']
}

df=pd.DataFrame(data)
print(df)
#linear,polynomial,time
df.interpolate(method="linear",axis=0,inplace=True) #linear interpolation
print(df)
#df.interpolate(method="polynomial",order=2,axis=0,inplace=True)
