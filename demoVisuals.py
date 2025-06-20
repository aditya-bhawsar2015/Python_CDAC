import pandas as pd
import matplotlib.pyplot as plt

ename = ["abc", "mno", 'xyz', 'pqr', 'sdf']
salary = [99000, 98000, 97000, 92000, 77000]

df = pd.read_csv("matches.csv")

# print(df.shape[0])
def calculate_points(type, value):
    if type == 'runs':
        return value
    return value*20

pointList =[]
for i in range(df.shape[0]):
    pointList.append(calculate_points(df.iloc[i, 12], df.iloc[i,14]))

# pointList = pd.Series(pointList)
df['points'] = pointList



df = df.dropna(subset=['winner'])
def get_initials(name):
    # print(name)
    name = name.split(" ")
    initials = []
    for i in name:
        initials.append(i[0])
    # print(initials)
    return ''.join(initials)


df['winner'] = df['winner'].apply(lambda x: get_initials(x))

# print(df)

# average_points = df.groupby('winner')['points'].mean()
# print(type(average_points))




all_umpires = pd.concat([df['umpire1'], df['umpire2']])



umpire_count = all_umpires.value_counts().sort_index()


print(umpire_count)


umpire_count.plot(kind='bar')
plt.xlabel('Umpires')
plt.ylabel('No. Of Mathches')
plt.show()

# print(umpire1_match_count)

# average_points.plot(kind='bar')
# plt.title('Average Points per Team')
# plt.xlabel('Team')
# plt.ylabel('Average Points')

# plt.hist(df['points'])
# plt.show()
# plt.plot(ename, salary)
# plt.scatter(ename, salary)
# plt.bar(ename, salary)

# How has the number of matches per season changed over the years?

matches_per_season = df['season'].value_counts()
# print(matches_per_season)

# matches_per_season.sort_values().plot(kind='line')
# plt.title(" Matches Every Season ")
# plt.xlabel("Years")
# plt.ylabel("Matches")
# plt.show()

