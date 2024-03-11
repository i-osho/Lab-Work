# import pandas as pd
# data = {
#     'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva',],
#     'roll': [11, 27, 33, 35, 40],
#     'marks': [45,67,95,86,23],
#     'branch': ['cyber', 'cse', 'cyber', 'ece', 'cyber']
# }

# df = pd.DataFrame(data)
# df.plot(x="roll", y='marks', kind='line')


import pandas as pd

data = {
    'Name':  ["Arun", "Bappu", "Chariya", "Deep", "Erada", "Farak", "Grace", "Hannah", "Ishant", "Jack"],
    'Roll': [1,2,3,4,5,6,7,8,9,10],
    'Math': [90, 85, 88, 92, 86, 89, 91, 87, 93, 90],
    'Science': [91, 85, 89, 92, 87, 90, 92, 88, 94, 91],
    'English': [92, 86, 90, 93, 88, 91, 93, 89, 95, 92],
    'History': [93, 87, 91, 94, 89, 92, 94, 90, 96, 93],
    'Art': [94, 88, 92, 95, 90, 93, 95, 91, 97, 94]
}
df = pd.DataFrame(data)

df.set_index('Roll', inplace=True)
df.plot(x='Name', y=['Science','Math'], kind='bar')
df[df['Science'] == df['Science'].max()]['Name']


df= pd.read_csv('ToyotaCorolla.csv')
df.head(50).plot(x='Age', y='Price', kind='bar')