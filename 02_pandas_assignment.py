import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'HR'],
    'Salary': [45000, 54000, 50000, 62000, 47000]
}
df = pd.DataFrame(data)
print(df.head())
print(df[['Age','Salary']].describe())
print("Avg HR Salary:", df[df['Department']=='HR']['Salary'].mean())

df['Bonus'] = df['Salary'] * 0.10

print(df[(df['Age'] >= 25) & (df['Age'] <= 30)])

print(df.groupby('Department')['Salary'].mean())

sorted_df = df.sort_values(by='Salary')
sorted_df.to_csv("sorted_salaries.csv", index=False)