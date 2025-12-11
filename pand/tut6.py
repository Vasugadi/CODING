#adding column

import pandas as pd

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
#to create a new column without data
df["country"]=None
print(df)
#to create a new column with data
df["class"]=["A","B","A"]
print(df)
#to create a new column with some operation on existing column
df["age after 5 years"]=df["age"]+5
print(df)

#creating a column by using insert function
#insert function takes 3 arguments
#insert(index,column_name,column_values)
#index is the position where you want to insert the column
#column_name is the name of the column
#column_values is the values of the column

df.insert(0,"std id",[1,2,3])
print(df)

