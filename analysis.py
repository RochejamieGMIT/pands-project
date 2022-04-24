import pandas as pd
import pandas_profiling as pp

import seaborn as sb
import matplotlib.pyplot as plt
color = sb.color_palette()
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
fig.write_image("fig1.png")

def df_to_plotly(ids):
    return {'z': ids.values.tolist(),
            'x': ids.columns.tolist(),
            'y': ids.index.tolist() }
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


SumIS = IrisSetosaGroup.agg(
    {
        "sepallength" : ["min", "max", "median","mean"],
        "sepalwidth" : ["min", "max", "median","mean"],
        "petallength" : ["min", "max", "median","mean"],
        "petalwidth" : ["min", "max", "median","mean"]
    }
)


SumIVC= IrisVersicolorGroup.agg(
    {
        "sepallength" : ["min", "max", "median","mean"],
        "sepalwidth" : ["min", "max", "median","mean"],
        "petallength" : ["min", "max", "median","mean"],
        "petalwidth" : ["min", "max", "median","mean"]
    }
)
SumIV = IrisVirginicaGroup.agg(
    {
        "sepallength" : ["min", "max", "median","mean"],
        "sepalwidth" : ["min", "max", "median","mean"],
        "petallength" : ["min", "max", "median","mean"],
        "petalwidth" : ["min", "max", "median","mean"]
    }
)

with open('summary.txt', 'a') as f:
    f.write("The summary for the Iris-setosa Species is as follows: \n")
    dfAsString = SumIS.to_string(header=True, index=True)
    f.write(dfAsString)
    f.write("\nThe summary for the Iris-versicolor Species is as follows: \n")
    dfAsString = SumIVC.to_string(header=True, index=True)
    f.write(dfAsString)
    f.write("\nThe summary for the Iris-virginica Species is as follows: \n")
    dfAsString = SumIV.to_string(header=True, index=True)
    f.write(dfAsString)

f.close()

dist = IrisSetosaGroup['sepallength'].value_counts()
trace = go.Pie(values=(np.array(dist)),labels=dist.index)
#layout = go.Layout(title='Each class')
#data = [trace]
#fig = go.Figure(trace,layout)
#fig.update_traces(marker=dict(line=dict(width=2)))
#fig.show()

#report = pp.ProfileReport(df)
#report.to_file('profile_report.html') # To preview data had to create a .html file as vs code could not open it

fig, ax = plt.subplots()
ids.hist(column='sepallength',ax=ax,bins = 5,by = 'class');
plt.suptitle("Histogram of Sepal lenght by class")
fig.savefig('sepallengthHist.png')
plt.close()

fig, ax = plt.subplots()
ids.hist(column='sepalwidth',ax=ax,by = 'class', bins = 5,);
plt.suptitle("Histogram of sepal width by class")
fig.savefig('sepalwidthHist.png')
plt.close()

fig, ax = plt.subplots()
ids.hist(column='petallength',ax=ax, bins = 5,by = 'class');
plt.suptitle("Histogram of petal length by class")
fig.savefig('petallengthHist.png')
plt.close()


fig, ax = plt.subplots()
ids.hist(column='petalwidth',ax=ax,bins = 5,by = 'class');
plt.suptitle("Histogram of petal width by class")
fig.savefig('petalwidthHist.png')
plt.close()


colours = {'Iris-setosa':'red', 'Iris-versicolor':'yellow', 'Iris-virginica':'blue'}
fig,
ids.plot.scatter(x='petallength', y='petalwidth',c=df['class'].map(colours),label = colours )
plt.title('Petal Scatter: Lenght v Width')
plt.legend(loc="lower left", title="Classes")
plt.savefig('scatter Petal.png')
plt.close()

fig,
ids.plot.scatter(x='sepallength', y='sepalwidth',c=df['class'].map(colours), label = colours )
plt.title('Sepal Scatter: Lenght v Width')
plt.legend(loc="lower left", title="Classes")
plt.savefig('scatter Sepal.png')
