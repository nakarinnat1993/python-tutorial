import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 24, 35],
    'City': ['New York', 'London', 'Berlin']
}
df = pd.DataFrame(data)

print(df)
print("Select column: ", df['Name'])
print("Select row: ", df.loc[0])
print("Select row range: ", df.loc[0:1])

filtered_df = df[df['Age'] > 30]
print("Filter age > 30: ", filtered_df)

average_age = df['Age'].mean()
print(f"Average Age: {average_age}")

df['Salary'] = [10000, 30000, 50000]
print(f"Add column: {df}")

# Update column at index 0
df.at[0, 'City'] = 'London'
grouped = df.groupby('City')['Salary'].mean()
print(grouped)