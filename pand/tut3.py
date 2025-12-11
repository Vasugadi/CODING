import pandas as pd

#summarizing the data
#information about the data
#df.info()

dict={
    "name":[
        "ram",
        "jaswanth",
        "syam"
    ],
    "age":[20,21,19],
    "city":['hyd','bang','chennai']
}

df=pd.DataFrame(dict)
print(df.info())
print(f'describe: {df.describe()}')


print(df)
