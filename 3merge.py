import pandas as pd
df1 = pd.DataFrame({
    'id': ['1', '2', '3'],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'id': ['1', '2', '3'],
    'Math': [85, 90, 95]
})

df3 = pd.DataFrame({
    'id': ['1', '2', '3'],
    'English': [88, 92, 96]
})

df = pd.merge(pd.merge(df1, df2, on='id'), df3, on='id')

print(df)