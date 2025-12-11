import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("C:/Users/HP/OneDrive/Desktop/numpy/indian employee dataset/indian_employee_data_100.csv")

# Display initial rows and missing value summary
print(df.head())
print(df.isnull().sum())

# Fill missing values in specific columns
df['Salary (INR)'] = df['Salary (INR)'].fillna(df['Salary (INR)'].mean())
df['Performance Rating'] = df['Performance Rating'].fillna(df['Performance Rating'].mean())

# Replace infinite values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill remaining missing values in numeric columns using mean
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Replace negative salaries with the mean salary
df['Salary (INR)'] = np.where(df['Salary (INR)'] < 0, df['Salary (INR)'].mean(), df['Salary (INR)'])

# Remove outliers beyond 3 standard deviations
salary_mean = df['Salary (INR)'].mean()
salary_std = df['Salary (INR)'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)
df = df[(df['Salary (INR)'] >= lower_bound) & (df['Salary (INR)'] <= upper_bound)]

# Save the cleaned dataset
df.to_csv('cleaned_indian_employee_data.csv', index=False)
print("✅ Data cleaning completed and saved to cleaned_indian_employee_data.csv")