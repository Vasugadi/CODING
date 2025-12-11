#sorting 
#sorting is nothing but arranging the data in a particular order
import pandas as pd
data={
    "name":[
        "ram",
        "jaswanth",
        "syam",
        "ajay"
    ],
    "age":[20,21,19,22],
    "city":['hyd','bang','chennai','delhi']
}
#need it in a alphabetical order
data=pd.DataFrame(data)
#sorting data
#sorting data in 1 column sort_values(by=column_name,ascending=True/False)
#df.sort_values(by="name",ascending=True,inplace=True)
data.sort_values(by="age",ascending=False,inplace=True)
print(data)