# =========================================
# EXPLORATORY DATA ANALYSIS (EDA)
# =========================================

# Step 1: Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr

wr.filterwarnings('ignore')

# =========================================
# Step 2: Read Dataset
# =========================================

df = pd.read_csv("WineQT.csv")

print(df.head())

# =========================================
# Step 3: Analyze Data
# =========================================

print(df.shape)

print(df.info())

print(df.describe().T)

print(df.columns.tolist())

# =========================================
# Step 4: Check Missing Values
# =========================================

print(df.isnull().sum())

# =========================================
# Step 5: Check Duplicate Values
# =========================================

print(df.duplicated().sum())

# =========================================
# Step 6: Univariate Analysis
# =========================================

# 1. Bar Plot

quality_counts = df['quality'].value_counts()

plt.figure(figsize=(8, 6))

plt.bar(
    quality_counts.index,
    quality_counts,
    color='deeppink'
)

plt.title('Count Plot of Quality')
plt.xlabel('Quality')
plt.ylabel('Count')

plt.show()

# =========================================
# 2. Histogram + KDE Plot
# =========================================

sns.set_style("darkgrid")

numerical_columns = df.select_dtypes(
    include=["int64", "float64"]
).columns

plt.figure(figsize=(14, len(numerical_columns) * 3))

for idx, feature in enumerate(numerical_columns, 1):

    plt.subplot(len(numerical_columns), 2, idx)

    sns.histplot(df[feature], kde=True)

    plt.title(
        f"{feature} | Skewness: {round(df[feature].skew(), 2)}"
    )

plt.tight_layout()

plt.show()

# =========================================
# 3. Swarm Plot
# =========================================

plt.figure(figsize=(10, 8))

sns.swarmplot(
    x="quality",
    y="alcohol",
    data=df,
    palette='viridis'
)

plt.title('Swarm Plot for Quality and Alcohol')

plt.xlabel('Quality')

plt.ylabel('Alcohol')

plt.show()

# =========================================
# Step 7: Bivariate Analysis
# =========================================

# 1. Pair Plot

sns.set_palette("Pastel1")

sns.pairplot(df)

plt.suptitle('Pair Plot for DataFrame')

plt.show()

# =========================================
# 2. Violin Plot
# =========================================

df['quality'] = df['quality'].astype(str)

plt.figure(figsize=(10, 8))

sns.violinplot(
    x="quality",
    y="alcohol",
    data=df,
    palette={
        '3': 'lightcoral',
        '4': 'lightblue',
        '5': 'lightgreen',
        '6': 'gold',
        '7': 'lightskyblue',
        '8': 'lightpink'
    }
)

plt.title('Violin Plot for Quality and Alcohol')

plt.xlabel('Quality')

plt.ylabel('Alcohol')

plt.show()

# =========================================
# 3. Box Plot
# =========================================

plt.figure(figsize=(10, 8))

sns.boxplot(
    x='quality',
    y='alcohol',
    data=df
)

plt.title('Box Plot')

plt.show()

# =========================================
# Step 8: Multivariate Analysis
# =========================================

plt.figure(figsize=(15, 10))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    fmt='.2f',
    cmap='Pastel2',
    linewidths=2
)

plt.title('Correlation Heatmap')

plt.show()