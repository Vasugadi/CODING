#avg salary
import pandas as pd

data={
    "name":[
        "ram","jaswanth","syam"],
    "age":[20,21,19],
    "salary":[20000,30000,25000]
}
df=pd.DataFrame(data)
print(df)

avg_Sal=df['salary'].mean()
print(f'average salary: {avg_Sal}')
