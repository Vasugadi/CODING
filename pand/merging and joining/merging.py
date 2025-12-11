#merging is nothing but combining the data based on some common columns
#pd.merge(df1,df2,on="key",how="type") #it will merge based on the common column key
import pandas as pd
data1={
    "key":[1,2,3,4],
    "name":["ram","syam","ajay","vijay"],
    "age":[20,21,19,22]
}
data2={
    "key":[1,2,3,4],
    "city":["hyd","bang","chennai","pune"],
    "salary":[20000,25000,30000,35000]
}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
df=pd.merge(df1,df2,on="key",how="inner") #inner will give the common values
df=pd.merge(df1,df2,on="key",how="outer") #outer will give all the values
