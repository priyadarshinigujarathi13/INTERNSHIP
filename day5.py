#Implementation for Data Cleaning
#Step 1: Import Libraries and Load Dataset
import pandas as pd
import numpy as np

df = pd.read_csv('Titanic-Dataset.csv')
df.info()
df.head()

#Step 2: Check for Duplicate Rows
df.duplicated()

#Step 3: Identify Column Data Types
cat_col = [col for col in df.columns if df[col].dtype == 'object']
num_col = [col for col in df.columns if df[col].dtype != 'object']

print('Categorical columns:', cat_col)
print('Numerical columns:', num_col)

#Step 4: Count Unique Values in the Categorical Columns

df[cat_col].nunique()

#Step 5: Calculate Missing Values as Percentage
round((df.isnull().sum() / df.shape[0]) * 100, 2)


#Step 6: Drop Irrelevant or Data-Heavy Missing Columns

df1 = df.drop(columns=['Name', 'Ticket', 'Cabin'])
df1.dropna(subset=['Embarked'], inplace=True)
df1['Age'] = df1['Age'].fillna(df1['Age'].mean())


#Step 7: Detect Outliers with Box Plot

import matplotlib.pyplot as plt

plt.boxplot(df1['Age'], vert=False)
plt.ylabel('Variable')
plt.xlabel('Age')
plt.title('Box Plot')
plt.show()

#Step 8: Calculate Outlier Boundaries and Remove Them

mean = df1['Age'].mean()
std = df1['Age'].std()

lower_bound = mean - 2 * std
upper_bound = mean + 2 * std

df2 = df1[(df1['Age'] >= lower_bound) & (df1['Age'] <= upper_bound)]


#Step 9: Impute Missing Data Again if Any

df3 = df2.fillna(df2['Age'].mean())
df3.isnull().sum()
#Step 10: Recalculate Outlier Bounds and Remove Outliers from the Updated Data
mean = df3['Age'].mean()
std = df3['Age'].std()

lower_bound = mean - 2 * std
upper_bound = mean + 2 * std

print('Lower Bound :', lower_bound)
print('Upper Bound :', upper_bound)

df4 = df3[(df3['Age'] >= lower_bound) & (df3['Age'] <= upper_bound)]


#Step 11: Data validation and verification
X = df3[['Pclass','Sex','Age', 'SibSp','Parch','Fare','Embarked']]
Y = df3['Survived']
#Step 12: Data formatting
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1))

num_col_ = [col for col in X.columns if X[col].dtype != 'object']
x1 = X
x1[num_col_] = scaler.fit_transform(x1[num_col_])
x1.head()


