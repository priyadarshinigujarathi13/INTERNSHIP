import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "Boby", "Mina"],
    "Degree": ["Masters", "Graduate", "Graduate"],
    "Age": [27, 23, 21]
})

print(df)

df.pivot(
    index="Name",
    columns="Degree",
    values="Age"
)
#Pivot is used to reshape data by converting rows into columns.