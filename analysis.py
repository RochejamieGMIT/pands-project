import pandas as pd
import pandas_profiling as pp

import seaborn as sb
import matplotlib.pyplot as plt
color = sb.color_palette()
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px
import numpy as np
from flask import Markup


# reading csv files
ids =  pd.read_csv('iris_csv.csv')
dist = ids['class'].value_counts()
colors = ['mediumturquoise', 'darkorange','red']
trace = go.Pie(values=(np.array(dist)),labels=dist.index)
layout = go.Layout(title='Class')
data = [trace]
fig = go.Figure(trace,layout)
fig.update_traces(marker=dict(colors=colors, line=dict(color='#000000', width=2)))
fig.write_html("pie.html")
fig.write_image("fig1.png")

def df_to_plotly(ids):
    return {'z': ids.values.tolist(),
            'x': ids.columns.tolist(),
            'y': ids.index.tolist() }
import plotly.graph_objects as go
dfNew = ids.corr()
fig = go.Figure(data=go.Heatmap(df_to_plotly(dfNew)))
fig.write_image("fig2.png")

fig = px.scatter(ids, x='petallength', y='class')
fig.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='petallength and class')
fig.write_image("fig3.png")

fig = px.box(ids, x='class', y='sepallength')
fig.update_traces(marker_color="midnightblue",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='class and sepallength')
fig.write_image("fig4.png")




filename = "iris_csv.csv"


listofCols = ['sepallength', 'sepalwidth']
print(ids[listofCols].head(2))


IrisSetosaGroup = ids[ids["class"].isin(['Iris-setosa'])] # seperating each species to their own group
IrisVersicolorGroup = ids[ids["class"].isin(['Iris-versicolor'])]
IrisVirginicaGroup = ids[ids["class"].isin(['Iris-virginica'])]


print(IrisVirginicaGroup.agg(
    {
        "sepallength" : ["min", "max", "median","mean"],
        "sepalwidth" : ["min", "max", "median","mean"],
        "petallength" : ["min", "max", "median","mean"],
        "petalwidth" : ["min", "max", "median","mean"]
    }
))
#print(IrisSetosaGroup)
#print(IrisVersicolorGroup)
#print(IrisVirginicaGroup)
print(IrisVirginicaGroup[listofCols].head(2))

#ids.head()
#print(ids.shape)
#report = pp.ProfileReport(ids)

#report.to_file('profile_report.html') # To preview data had to create a .html file as vs code could not open it
#data.info()
#print(data.describe())
#data.isnull().sum()
#
#up_dt = {}
#
#  
#print(up_dt)
#sb.scatterplot(x='petallength', y='petalwidth',
#               hue='class', data=data, )
#
#
#plt.legend()
#plt.savefig('testMultiSave.png')
#
# 
#sb.scatterplot(x='sepalwidth', y='sepallength',
#                hue='class', data=data, )
#plt.legend()
#plt.savefig('testMultiSave2.png')
#
#
#plt.show()
#
