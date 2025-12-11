import pandas as pd
import numpy as np

# Load the dataset
df=pd.read_csv("C:/Users/HP/OneDrive/Desktop/numpy/indian employee dataset/indian_employee_data_100.csv")
print(df.head())
print("missing values in each column")
print(df.isnull().sum())

df['Salary (INR)'].fillna(df['Salary (INR)'].mean(),inplace=True)
df['Performance Rating'].fillna(df['Performance Rating'].median(),inplace=True)
df.replace([np.inf,-np.inf],np.nan,inplace=True)
df.fillna(df.mean(),inplace=True)
#remove duplicates
df.drop_duplicates(inplace=True)
# replace negative salaries
df['Salary (INR)']=np.where(df['Salary (INR)']<0,df['Salary (INR)'].mean(),df['Salary (INR)'])
salary_mean=df['Salary (INR)'].mean()
salary_std=df['Salary (INR)'].std()
lower_bound=salary_mean-(3*salary_std)
upper_bound=salary_mean+(3*salary_std)
# #remove where salary is out of bound high or lowe
df=df[(df['Salary (INR)']>=lower_bound) & (df['Salary (INR)']<=upper_bound)]

df.to_csv('cleaned_indian_employee_data.csv',index=False)
print("Data cleaning completed and saved to cleaned_indian_employee_data.csv")