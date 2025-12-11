#understanding data
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
print(data)

a=data.head(1)
b=data.tail(2)
print(a)
print(b)