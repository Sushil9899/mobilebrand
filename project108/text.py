import plotly.figure_factory as ff
import pandas as pd
import csv


print("hi")
df = pd.read_csv("data.csv") 
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Rating"],show_hist=False)

fig.show()