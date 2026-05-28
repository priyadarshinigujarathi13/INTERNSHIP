import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


# Sample Data
data = {
    'Name': ['ANSH', 'SAHIL', 'JAYAN', 'ANURAG'],
    'Age': [21, 23, 20, 24]
}

df = pd.DataFrame(data)


# 1. Line Plot
plt.figure(figsize=(5, 4))
sns.lineplot(x=df.index, y='Age', data=df)
plt.title("Line Plot")
plt.xlabel("Index")
plt.ylabel("Age")
plt.show()


# 2. Scatter Plot
plt.figure(figsize=(5, 4))
sns.scatterplot(x=df.index, y='Age', data=df)
plt.title("Scatter Plot")
plt.show()


# 3. Box Plot
plt.figure(figsize=(5, 4))
sns.boxplot(y='Age', data=df)
plt.title("Box Plot")
plt.show()


# 4. Violin Plot
plt.figure(figsize=(5, 4))
sns.violinplot(y='Age', data=df)
plt.title("Violin Plot")
plt.show()


# 5. Swarm Plot
plt.figure(figsize=(5, 4))
sns.swarmplot(x=df.index, y='Age', data=df)
plt.title("Swarm Plot")
plt.show()


# 6. Bar Plot
plt.figure(figsize=(5, 4))
sns.barplot(x='Name', y='Age', data=df)
plt.title("Bar Plot")
plt.show()


# 7. Point Plot
plt.figure(figsize=(5, 4))
sns.pointplot(x='Name', y='Age', data=df)
plt.title("Point Plot")
plt.show()


# 8. Count Plot
count_data = {
    'Name': ['ANSH', 'SAHIL', 'ANSH', 'JAYAN',
             'ANURAG', 'ANURAG', 'ANURAG', 'SAHIL']
}

count_df = pd.DataFrame(count_data)

plt.figure(figsize=(5, 4))
sns.countplot(x='Name', data=count_df)
plt.title("Count Plot")
plt.show()


# 9. KDE Plot
iris = load_iris()

iris_df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

iris_df['Species'] = iris.target

iris_df['Species'] = iris_df['Species'].map({
    0: 'Setosa',
    1: 'Versicolor',
    2: 'Virginica'
})

plt.figure(figsize=(5, 4))
sns.kdeplot(
    data=iris_df[iris_df['Species'] == 'Virginica'],
    x='sepal length (cm)',
    fill=True,
    label='Virginica'
)

plt.title("KDE Plot")
plt.legend()
plt.show()