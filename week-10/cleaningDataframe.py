import pandas as pd
data = {
    'Name': ['514', '515', '516', None],
    'Marks': [120, None, 28, 92]
}
df = pd.DataFrame(data)
df['Marks'] = df['Marks'].fillna(0)
df['Total'] = df['Marks'] + 5
df = df.dropna()
print(df)