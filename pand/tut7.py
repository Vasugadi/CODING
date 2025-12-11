#updating the values
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

#to update a particular value
#df.loc[row_index,column_name]=new_value
#df.at[row_index,column_name]=new_value
df.loc[0,"age"]=23
df.at[1,"city"]="delhi"
print(df)
#to update multiple values
#df.loc[condition,column_name]=new_value
df.loc[df["age"]>20,"city"]="mumbai"
print(df)
#increse the salary by 5 percenmt
df["salary"]=df['salary']*1.05
print(df)