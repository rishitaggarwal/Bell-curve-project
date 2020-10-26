import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("bellcurve_project for today.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()],["average rating"],show_hist= False)
fig.show()