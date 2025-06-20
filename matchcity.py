import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../day12/matches.csv")

city = df['city'].value_counts()
venues = df.groupby('season')['city']
print(city.head(1))

print(venues)