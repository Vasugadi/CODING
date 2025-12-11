import pandas as pd

data={
    "name":[
        "ram","jaswanth","syam","myam","kram","swanth","sam"],
    "age":[20,21,19,22,20,21,19],
    "salary":[20000,30000,25000,40000,22000,32000,27000],
    'city':['hyd','bang','chennai','hyd','bang','chennai','hyd']
}

df=pd.DataFrame(data)

#group by city and get average salary
grouped=df.groupby('city')['salary'].sum()
goruped3=df.groupby(['age','name'])["salary"].sum()
print(goruped3)
print(grouped)














# df['salary'].plot(kind='bar')
# df.plot(kind='bar')
# df.plot(kind='bar',x='name',y='salary')
# df.plot(kind='bar',x='name',y='salary',color='red')
# df.plot(kind='bar',x='name',y='salary',color='red',figsize=(10,5))