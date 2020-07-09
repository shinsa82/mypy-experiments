from pandas import DataFrame

df = DataFrame([[1, 2], [3, 4], [5, 6]])
# reveal_type(df)
print(df)
df.to_csv('data.csv')  # error
