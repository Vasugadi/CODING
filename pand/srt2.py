import pandas as pd

data={
    "name":[
        "ram",
        "jaswanth",
        "syam"
    ],
    "age":[20,21,19],
    "salary":[20000,30000,25000],
    "city":['hyd','bang','chennai']
}

d=pd.DataFrame(data)
print(d)
d.to_csv('data.csv') #it will create a csv file in the current directory

d.sort_values(by=['age','salary'],ascending=[False,True],inplace=True) #sort the dataframe by age
print(d)