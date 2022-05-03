# This is a project to Analyse the fisher's iris data set. 
# I have a lot of code references to include with this project, 
#But one I used a lot through out the project is this
# https://towardsdatascience.com/a-beginners-guide-to-data-analysis-in-python-188706df5447
# There's a lot of other references thta will also be included through out.
# And A comprehensive list will be added to the read me file. 
# I used this reference to come up with interensting ways to try to analyse the data
# https://stattrek.com/statistics/charts/compare-data-sets.aspx#:~:text=Common%20graphical%20displays%20(e.g.%2C%20dotplots,two%20or%20more%20data%20sets.
#

#Import necessary libraries
import pandas as pd
import pandas_profiling as pp
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px
import numpy as np



# reading csv files
ids =  pd.read_csv('iris_csv.csv')

# Reference for the Pi chart 
# https://towardsdatascience.com/a-beginners-guide-to-data-analysis-in-python-188706df5447
# 
dist = ids['class'].value_counts()
trace = go.Pie(values=(np.array(dist)),labels=dist.index)
layout = go.Layout(title='Class')
data = [trace]
fig = go.Figure(trace,layout)
fig.write_image("Pie_ValueCountCheck.png") # Generating a pie chart to confirm an equal amount of values for each class

def df_to_plotly(ids):
    return {'z': ids.values.tolist(),
            'x': ids.columns.tolist(),
            'y': ids.index.tolist() }
dfNew = ids.corr() # Compute pairwise correlation with another DataFrame or Series.
fig = go.Figure(data=go.Heatmap(df_to_plotly(dfNew))) #Creates a heatmap of the data to check for correlations 
fig.write_image("Heatmap.png") # not very useful in this instance as it does not differentiate between classes


# https://plotly.com/python/renderers/
# https://plotly.com/python/static-image-export/
#
fig = px.scatter(ids, x='petallength', y='class') # create a scatter plot of each petal lenght in their class
fig.update_traces()
fig.update_layout(title_text='petallength and class') # Add title
fig.write_image("Dot1_PetalLenghtDotGraph.png") # Save to PNG
# I found this interesting as putting each class side by side you can see where they over lap

fig = px.scatter(ids, x='sepallength', y='class') # create a scatter plot of each sepallength in their class
fig.update_traces
fig.update_layout(title_text='sepallength and class')
fig.write_image("Dot2_sepallengthDotGraph.png")

fig = px.scatter(ids, x='sepalwidth', y='class') # create a scatter plot of each sepalwidth in their class
fig.update_traces
fig.update_layout(title_text='sepalwidth and class')
fig.write_image("Dot3_sepalwidthDotGraph.png")

fig = px.scatter(ids, x='petalwidth', y='class') # create a scatter plot of each petalwidth in their class
fig.update_traces
fig.update_layout(title_text='petalwidth and class')
fig.write_image("Dot4_petalwidthDotGraph.png")




fig = px.box(ids, x='class', y='petallength') #Creates a box graph of petal length for each class
fig.update_traces
fig.update_layout(title_text='class and petallength') # title
fig.write_image("Box1_petallength.png") # save to png

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

# seperating each species to their own group using isin function
# https://www.geeksforgeeks.org/python-pandas-dataframe-isin/
IrisSetosaGroup = ids[ids["class"].isin(['Iris-setosa'])]
IrisVersicolorGroup = ids[ids["class"].isin(['Iris-versicolor'])]
IrisVirginicaGroup = ids[ids["class"].isin(['Iris-virginica'])]

# https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/06_calculate_statistics.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg
#
#Summarise the data in each class 
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
    dfAsString = SumIS.to_string(header=True, index=True) # https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file
    f.write(dfAsString)
    f.write("\nThe summary for the Iris-versicolor Species is as follows: \n")
    dfAsString = SumIVC.to_string(header=True, index=True)
    f.write(dfAsString)
    f.write("\nThe summary for the Iris-virginica Species is as follows: \n")
    dfAsString = SumIV.to_string(header=True, index=True)
    f.write(dfAsString)

f.close()


#https://stackoverflow.com/questions/52553062/pandas-profiling-doesnt-display-the-output
report = pp.ProfileReport(ids)
report.to_file('profile_report.html') # To preview data had to create a .html file as vs code could not open it

# https://www.machinelearningplus.com/pandas/pandas-histogram/#:~:text=Default%20plot,column%20in%20the%20pandas%20dataframe.
# https://stackoverflow.com/questions/31596084/save-dataframe-hist-to-a-file
# https://stackoverflow.com/questions/19614400/add-title-to-collection-of-pandas-hist-plots
# https://stackoverflow.com/questions/41174202/matplotlib-doesnt-forget-previous-data-when-saving-figures-with-savefig

fig, ax = plt.subplots()
ids.hist(column='sepallength',ax=ax,bins = 10,by = 'class');
plt.suptitle("Histogram of Sepal lenght by class")
fig.savefig('Hist1_sepallengthHist.png')
plt.close()

fig, ax = plt.subplots()
ids.hist(column='sepalwidth',ax=ax,bins = 10 ,by = 'class');
plt.suptitle("Histogram of sepal width by class")
fig.savefig('Hist2_sepalwidthHist.png')
plt.close()

fig, ax = plt.subplots()
ids.hist(column='petallength',ax=ax, bins = 10,by = 'class');
plt.suptitle("Histogram of petal length by class")
fig.savefig('Hist3_petallengthHist.png')
plt.close()


fig, ax = plt.subplots()
ids.hist(column='petalwidth',ax=ax,bins = 10,by = 'class');
plt.suptitle("Histogram of petal width by class")
fig.savefig('Hist4_petalwidthHist.png')
plt.close()


# https://kanoki.org/2020/08/30/matplotlib-scatter-plot-color-by-category-in-python/
# https://matplotlib.org/3.5.0/gallery/lines_bars_and_markers/scatter_with_legend.html

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


