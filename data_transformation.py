import pandas as pd
import numpy as np

df = pd.read_csv("employees.csv")

# 1. Mathematical Transformation
df["Salary_Log"] = np.log(df["Salary"])

# 2. Date/Time Extraction
df["Join_Date"] = pd.to_datetime(df["Join_Date"])
df["Join_Year"] = df["Join_Date"].dt.year

# 3. Conditional Logic
df["Bonus"] = np.where(df["Salary"] > 50000,
                       "High Bonus",
                       "Low Bonus")

print(df)