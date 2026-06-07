import pandas as pd

# DataFrame 1
df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Darsh", "Priya", "spoorti", "kathyayini"]
})

# DataFrame 2
df2 = pd.DataFrame({
    "ID": [1, 2, 4, 5],
    "Salary": [50000, 60000, 70000, 80000]
})

# Merge
result = pd.merge(df1, df2, on="ID", how="inner")

print(result)
result = pd.merge(df1, df2, on="ID", how="left")
print(result)
result = pd.merge(df1, df2, on="ID", how="right")
print(result)