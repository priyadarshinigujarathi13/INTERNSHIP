# GROUPBY()
# Group by Single Column
import pandas as pd

data = {
    "Team": ["A", "A", "B", "B"],
    "Points": [100, 150, 200, 250]
}

df = pd.DataFrame(data)

result = df.groupby("Team").sum()

print(result)

#Program 2: Multiple Columns Grouping
import pandas as pd

data = {
    "Team": ["A", "A", "B", "B"],
    "Position": ["Guard", "Center", "Guard", "Center"],
    "Points": [100, 150, 200, 250]
}

df = pd.DataFrame(data)

result = df.groupby(["Team", "Position"]).sum()

print(result)

#Aggregation
import pandas as pd

data = {
    "Team": ["A", "A", "B", "B"],
    "Salary": [1000, 2000, 3000, 4000]
}

df = pd.DataFrame(data)

result = df.groupby("Team").agg(
    total_salary=("Salary", "sum"),
    avg_salary=("Salary", "mean"),
    count=("Salary", "count")
)

print(result)

