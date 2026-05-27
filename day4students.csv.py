# 
# ==============================
# PANDAS COMPLETE PROGRAMS
# ==============================

import pandas as pd
import numpy as np

# =========================================
# 1. SERIES BASICS
# =========================================

print("\n===== Program 1: Creating Series =====")

data = [10, 20, 30, 40]

s = pd.Series(data)

print(s)


print("\n===== Program 2: Series with Custom Index =====")

s = pd.Series(
    [90, 85, 95],
    index=["Math", "Science", "English"]
)

print(s)

# =========================================
# 2. DATAFRAME BASICS
# =========================================

print("\n===== Program 3: Creating DataFrame =====")

data = {
    "Name": ["Darshini", "Rahul", "Anu"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 95]
}

df = pd.DataFrame(data)

print(df)


print("\n===== Program 4: Accessing Columns =====")

print(df["Name"])


print("\n===== Program 5: Accessing Rows =====")

print(df.loc[0])

# =========================================
# 3. DATA INPUT AND OUTPUT
# =========================================

print("\n===== Program 6: Reading CSV =====")

# Create sample dataframe
students_df = pd.DataFrame({
    "Name": ["Darshini", "Rahul", "Anu"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 95]
})

# Save as CSV
students_df.to_csv("students.csv", index=False)

# Read CSV
df_csv = pd.read_csv("students.csv")

print(df_csv)


print("\n===== Program 7: Writing CSV =====")

data = {
    "Name": ["A", "B"],
    "Marks": [70, 80]
}

df_output = pd.DataFrame(data)

df_output.to_csv("output.csv", index=False)

print("output.csv File Saved Successfully")


print("\n===== Program 8: Reading Excel =====")

# Create Excel file
students_df.to_excel("students.xlsx", index=False)

# Read Excel file
df_excel = pd.read_excel("students.xlsx")

print(df_excel)

# =========================================
# 4. DATA CLEANING OPERATIONS
# =========================================

print("\n===== Program 9: Finding Null Values =====")

data = {
    "Name": ["A", "B", None],
    "Marks": [90, None, 80]
}

df_null = pd.DataFrame(data)

print(df_null.isnull())


print("\n===== Program 10: Removing Null Values =====")

data = {
    "Name": ["A", None, "C"],
    "Marks": [90, 85, None]
}

df_drop = pd.DataFrame(data)

new_df = df_drop.dropna()

print(new_df)


print("\n===== Program 11: Filling Missing Values =====")

data = {
    "Marks": [90, None, 80]
}

df_fill = pd.DataFrame(data)

df_fill.fillna(0, inplace=True)

print(df_fill)


print("\n===== Program 12: Removing Duplicate Rows =====")

data = {
    "Name": ["A", "B", "A"],
    "Marks": [90, 80, 90]
}

df_dup = pd.DataFrame(data)

print(df_dup.drop_duplicates())

# =========================================
# 5. DATA FILTERING
# =========================================

print("\n===== Program 13: Filtering Data =====")

data = {
    "Name": ["A", "B", "C"],
    "Marks": [90, 60, 85]
}

df_filter = pd.DataFrame(data)

print(df_filter[df_filter["Marks"] > 80])

# =========================================
# 6. SORTING
# =========================================

print("\n===== Program 14: Sorting Data =====")

print(df_filter.sort_values(by="Marks"))

# =========================================
# 7. GROUPBY OPERATIONS
# =========================================

print("\n===== Program 15: GroupBy =====")

data = {
    "Department": ["IT", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 45000, 40000]
}

df_group = pd.DataFrame(data)

print(df_group.groupby("Department")["Salary"].mean())

# =========================================
# 8. MERGING DATAFRAMES
# =========================================

print("\n===== Program 16: Merge DataFrames =====")

df1 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["A", "B"]
})

df2 = pd.DataFrame({
    "ID": [1, 2],
    "Marks": [90, 80]
})

result = pd.merge(df1, df2, on="ID")

print(result)

# =========================================
# 9. ADVANCED OPERATIONS
# =========================================

print("\n===== Program 17: Applying Functions =====")

data = {
    "Marks": [50, 60, 70]
}

df_apply = pd.DataFrame(data)

df_apply["Updated"] = df_apply["Marks"].apply(
    lambda x: x + 5
)

print(df_apply)


print("\n===== Program 18: Pivot Table =====")

data = {
    "Name": ["A", "A", "B", "B"],
    "Subject": ["Math", "Science", "Math", "Science"],
    "Marks": [90, 85, 80, 88]
}

df_pivot = pd.DataFrame(data)

table = df_pivot.pivot_table(
    values="Marks",
    index="Name",
    columns="Subject"
)

print(table)


print("\n===== Program 19: Value Counts =====")

data = {
    "City": ["Hyd", "Hyd", "Vizag", "Hyd"]
}

df_city = pd.DataFrame(data)

print(df_city["City"].value_counts())


print("\n===== Program 20: Descriptive Statistics =====")

data = {
    "Marks": [50, 60, 70, 80, 90]
}

df_stats = pd.DataFrame(data)

print(df_stats.describe())