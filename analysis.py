# This is a project to Analyse the fisher's iris data set. 
# I have a lot of code references to include with this project, 
#But one I used a lot through out the project is this
#https://towardsdatascience.com/a-beginners-guide-to-data-analysis-in-python-188706df5447
# There's a lot of other references thta will also be included through out. 
#
#

import io
from contextlib import redirect_stdout

import pandas as pd
import pandas_profiling as pp
import matplotlib.pyplot as plt

import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px
import numpy as np
from flask import Markup


# reading csv files
ids =  pd.read_csv('iris_csv.csv')
dist = ids['class'].value_counts()
trace = go.Pie(values=(np.array(dist)),labels=dist.index)
layout = go.Layout(title='Class')
data = [trace]
fig = go.Figure(trace,layout)
fig.write_image("fig1.png")

def df_to_plotly(ids):
    return {'z': ids.values.tolist(),
            'x': ids.columns.tolist(),
            'y': ids.index.tolist() }
dfNew = ids.corr()
fig = go.Figure(data=go.Heatmap(df_to_plotly(dfNew)))
fig.write_image("fig2.png")

fig = px.scatter(ids, x='petallength', y='class')
fig.update_traces()
fig.update_layout(title_text='petallength and class')
fig.write_image("Dot1_PetalLenghtDotGraph.png")

fig = px.scatter(ids, x='sepallength', y='class')
fig.update_traces
fig.update_layout(title_text='sepallength and class')
fig.write_image("Dot2_sepallengthDotGraph.png")

fig = px.scatter(ids, x='sepalwidth', y='class')
fig.update_traces
fig.update_layout(title_text='sepalwidth and class')
fig.write_image("Dot3_sepalwidthDotGraph.png")

fig = px.scatter(ids, x='petalwidth', y='class')
fig.update_traces
fig.update_layout(title_text='petalwidth and class')
fig.write_image("Dot4_petalwidthDotGraph.png")




fig = px.box(ids, x='class', y='petallength')
fig.update_traces
fig.update_layout(title_text='class and petallength')
fig.write_image("Box1_petallength.png")

fig = px.box(ids, x='class', y='sepallength')
fig.update_traces
fig.update_layout(title_text='class and sepallength')
fig.write_image("Box2_sepallength.png")

fig = px.box(ids, x='class', y='sepalwidth')
fig.update_traces
fig.update_layout(title_text='class and sepalwidth')
fig.write_image("Box3_sepalwidth.png")

fig = px.box(ids, x='class', y='petalwidth')
fig.update_traces
fig.update_layout(title_text='class and petalwidth')
fig.write_image("Box4_petalwidth.png")





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
    f.write("\nThis is a summary of the information on the Fisher's Iris data set \n Overall data seet information:\n")
    ids.info(buf=f)#Writing the sys.stdout to file https://stackoverflow.com/questions/35436331/how-to-save-output-from-dataframe-info-to-file-a-excel-or-text-file
    f.write("\nThe summary for the Iris-setosa Species is as follows: \n")
    dfAsString = SumIS.to_string(header=True, index=True)
    f.write(dfAsString)
    f.write("\nThe summary for the Iris-versicolor Species is as follows: \n")
    dfAsString = SumIVC.to_string(header=True, index=True)
    f.write(dfAsString)
    f.write("\nThe summary for the Iris-virginica Species is as follows: \n")
    dfAsString = SumIV.to_string(header=True, index=True)
    f.write(dfAsString)

f.close()


#report = pp.ProfileReport(ids)
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
ids.plot.scatter(x='petallength', y='petalwidth',c=ids['class'].map(colours),label = colours )
plt.title('Petal Scatter: Lenght v Width')
plt.legend(loc="best", title="Classes")
plt.savefig('scatter Petal.png')
plt.close()

fig,
ids.plot.scatter(x='sepallength', y='sepalwidth',c=ids['class'].map(colours), label = colours )
plt.title('Sepal Scatter: Lenght v Width')
plt.legend( loc="best", title="Classes")
plt.savefig('scatter Sepal.png')


