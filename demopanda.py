import pandas as pd
import matplotlib.pyplot as plt
emp = pd.read_csv("emp.csv")
dept = pd.read_csv("dept.csv")
d = pd.read_csv("cricket_data_2025.csv")

# print(d["Player_Name"])
df_no_duplicates = d.drop_duplicates(keep="first")
print(df_no_duplicates['Player_Name'].tail())
# print(df_no_duplicates)
# df_replaced = d.replace("No stats", 0)
# print(df_replaced["Fours"])
# df_replaced.to_csv("cricket_data_2025.csv", index = False)

result = pd.merge(emp,dept, how="left")
result_group = result.groupby(['dnmae', 'city'])


plt.scatter(d['Player_Name'], d['Matches_Batted'])
plt.show()
