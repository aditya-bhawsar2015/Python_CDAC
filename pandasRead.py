import pandas as pd

d = pd.read_csv("Student.csv")

# print(d)

print(d[d['std']>5])


f = pd.read_csv("tested.csv")
print(f.shape)
e=f.dropna()
print(e)


print(f.describe())     #describes data min max average etc