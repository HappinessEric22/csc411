import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import matplotlib.mlab
import seaborn as sns

file = pd.read_csv(r'C:\Users\user\Desktop\Nigeria.csv')
df = pd.DataFrame(file)
print(df)

print('Number of missing data is :',df.isnull().sum().sum())
print(df.describe().head(5))


print("length of rows are:")
print(len(df))
print('length of columns are:')
print(len(df.columns))

first_5 = df.head(5)
print(first_5)


df2 =df['Date'].value_counts()
print(df2)

df3 = df['States Affected'].value_counts()
print(df3)
df3.plot(kind='bar', figsize=(12,6))
plt.xlabel("States Affected")
plt.ylabel("Value count")

plt.title("States affected with Covid-19 in Nigeria ")
df3.plot(kind='bar', color ='y', width = 0.50)
plt.savefig('covid nigeria16.png')



