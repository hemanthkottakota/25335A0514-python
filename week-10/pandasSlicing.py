import pandas as pd
data = {
    'Name': ['514', '515', '516', '517'],
    'Marks': [100, 90, 68, 20]
}
df = pd.DataFrame(data)
sorted_df = df.sort_values(by='Marks')

print("Sorted Data:")
print(sorted_df)

print("\nSliced Data : ")
print(df[:2])