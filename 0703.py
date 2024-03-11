from unicodedata import normalize
import pandas as pd
import numpy as np

data = {
    'Name':  ["Arun", "Bappu", "Chariya", "Deep",],
    'Roll': [1,2,3,4],
    'Math': [90, 85, 88, np.NaN],
    'Science': [91, 85, 89, 92],
    'English': [92, 86, np.NaN, 93],
}
df = pd.DataFrame(data)

df.Math = df.Math.fillna(value=df.Math.mean())
df.English = df.English.fillna(value=df.English.mean())

df.plot(x='Name', y='Math', kind='scatter')
df.plot(x='Name', y='English', kind='scatter')

df

x = [4,54,56,7,8,0]
y = [12,56,19,85,43]

df2 = pd.DataFrame(list(zip(x,y)), columns=['Age', 'Weight'])

df2

X = df2.Age.to_numpy()
Y = df2.Weight.to_numpy()
