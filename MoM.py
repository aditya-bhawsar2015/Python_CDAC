import time

start_time = time.time()
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../day12/matches.csv")

batsmen  = pd.read_csv("All-Time-Best-Batsman.csv")
bowler = pd.read_csv("All-Time-Best-Bowlers.csv")

groupby_team = df.groupby('')

end_time=time.time()

print(f"Execution time : {end_time-start_time}")
