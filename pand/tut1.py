import pandas as pd
df=pd.read_csv("data.csv",encoding='latin1')
print(df)
#to read the data from excel
df=pd.read_excel("data.xlsx",sheet_name="Sheet1")
print(df)
#to read the data from a json
df=pd.read_json("data.json")
print(df)

#creating a new dataframe
data={
    "name":[
        "ram",
        "jaswanth",
        "syam"
    ],
    "age":[20,21,19],
    "city":['hyd','bang','chennai']
}

df=pd.DataFrame(data)
print(df)

#
df.to_csv("newdata.csv",index=False) #index false is used for not writing row indices
df.to_excel("newdata.xlsx",index=False)
df.to_json("newdata.json",index=False)

#understanding data
