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
print(f'shape: {data.shape}') #it gives (3, 3) that means 3 rows and 3 columns
print("\n")
print(f'columns: {data.columns}') #it means the names of the columns
print("\n")
print(f'index: {data.index}') #it means the index of the DataFrame simply we can say that its labels

"""
(10k,20) large data
(5,4) small data
"""

