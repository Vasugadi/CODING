import pandas as pd

data={
    "name":[
        "ram",
        "jaswanth",
        "syam"
    ],
    "age":[20,21,19],
    "city":['hyd','bang','chennai']
}
data=pd.DataFrame(data)
col=data["name"]
print(col)
cols=data[["name","age"]]
print(cols)

#filtering
filtered_data=data[data["age"]>20]
filt=data[data["age"]]
print(filtered_data)

filtered_data=data[(data["age"]>18) & (data["age"]<22)]
print(filtered_data)
