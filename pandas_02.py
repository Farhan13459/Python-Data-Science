import pandas as pd
import numpy as np

ipl=pd.read_csv("ipl-matches.csv")

win=ipl["WinningTeam"].value_counts() 
win1=ipl["Team1"].value_counts() + ipl["Team2"].value_counts()

win.sort_values(ascending=False,inplace=True)

total=np.sum(win)
win_teams=(win*100)/win1
print(win_teams.sort_values(ascending=False))


