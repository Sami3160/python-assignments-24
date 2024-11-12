import pandas as pd
import numpy as np

data = {
    'Name': ['Aarav', 'Vivaan', 'Aditya', 'Vihaan', 'Arjun'],
    'Age': [25, 30, 22, 35, 28],
    'City': ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai']
}

df = pd.DataFrame(data)

print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df['Name'])
print(df[['Name', 'City']])
print(df.iloc[0])
print(df.iloc[:, 0])
print(df.loc[0])
print(df.loc[:, 'Name'])
print(df[df['Age'] > 25])
print(df.sort_values(by='Age'))
print(df.groupby('City').mean())
print(df.isnull().sum())
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Age'] = df['Age'].replace(25, 26)
df['New_Column'] = np.where(df['Age'] > 30, 'Senior', 'Junior')
df.drop('New_Column', axis=1, inplace=True)
df.dropna(inplace=True)
df.to_csv('output.csv', index=False)
df2 = pd.read_csv('output.csv')
print(df2)