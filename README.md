# pands-project

I Got the data set from:
https://datahub.io/machine-learning/iris#data
as it is a .csv file, I htought working with a .csv file woulf be preferable. 

Read me:

The Data set for this project is the Fisher's Iris data set. This data set is based around three different species of the Iris flower. The three species are the Iris setosa, Iris virginica and Iris versicolor. The data holds four attributes of the flowers. The four attributes are sepal length, sepal width, petal length and petal width all in cm. Each species has fifty recorded samples in their data set. The data set was popularised by its name’s sake Sir Ronal Aylmer Fisher, a largely celebrated statistician.
Although the data set was popularised and named after Fisher, the dataset was collected and compiled by a botanist, Dr Edgar Anderson.
Anderson hand measured most of the petals and sepals by hand. The iris flower itself has over 250 species. Although the most common colour is purple, iris flowers can be almost any colour of the rainbow. 
That is a bit of background on the data and the flower the data is of. 

Returning focus specifically to the species contained in the data set, of the three species when looking at the data on species is immediately distinguishable from the other two. The Iris setosa data stands out, where the data for  Iris virginica and Iris versicolor are a little more similar. 

The first graphic I generated was a simple pie chart to confirm even numbers of each species of the Iris plant. This was mainly done to practice diferent tyes of data representation. but it is a good way to compare a categories of data to ensure even numbers of each data set are present to allow fair comparrisions. 

The next graphic I created was a heat map, to compare differnet measurements to each other. 
I did not divide this in to each sepcies of the iris plant. So it is an over arching look at all values for all species. As it tests pair values it's not surprising that most values for the plants experience a resonably high correlation. One thing I found interesting though is the relatively low lack of correlation the sepal width had with the other values. 
Meaning for any given species of the iris the sepal width can vary quite a lot and is not as consistant as other measure meants. 

The next set of graphics I created, I used the scatter plot function, but I used the classes as the y axis, against the X axis of each measured attributed. 
This created a graph where each measured value is placed on a horizontal line. Essentially the lines show the sets of each class of iris next to each other for easy comparison. 

These are the Dot1 - Dot4 graphs. The interesting thing about these graphs is typically Iris-setosa is the smallest, usually bunch down furthest left. Then Iris-versicolor in the middle a bit futher along distinclty larger than the Iris-setosa. And finally Iris-virginica typically furtherest right, being the largest values, with some over lap with Iris-versicolor.

This statement is mostly true for Petal Lenght, Sepal Lenght, and petal width. Values typically ascend  Iris-setosa to Iris-versicolor to Iris-virginica, With notable over lap between  Iris-versicolor and Iris-virginica. The only category that this is not true for is sepal width, the sepal width values of the iris sub classes do not follow this same pattern, this is why in the previous heat map there is little correlation between the sepal width and other values. 

The petal values for the Iris-setosa has no overlap with the other two classes, making it very distinct and easy to dsitingush. The upper values for the Iris-versicolor and the lower values for Iris-virginica have some note worthy overlap. Meaning given a random set of measurements most likely you would know if it is a Iris-setosa, but depending on which end of the scale the measurements are for Iris-versicolor or Iris-virginica you might not clearly be able to say which class it is. 

For the sepals it gets more difficult to determine the type of iris with uncategorised data, as there is more over lap for all classes of the iris, even if the sepal length follows the increasing size as the petals do, the sepal width does not and this makes it hard to determine the class of an iris using just the sepal measurements. 

I then created four box graphs again, by class and attribute. This is a a similar why to analysis data as the dot graphs in the last section. You can see the same steps of the stairs type measurements from Iris-setosa to Iris-versicolor to Iris-virginica in all attributes except the sepal width. 

In the box method you can see where a more concentrated volume of values sit, almost minimising the overlap between classes Futher isolating the Iris-setosa from the other two. 

The next thing I created was sub data frames for each class of iris so I could use the .agg function to summarise each class, with 4 headings. ["min", "max", "median","mean"].

ids.info generates some basic informationon the dataframe, but it's type is a sys.stdout.
I wanted to write this to the summary.txt file so I used this webpage to put the information in to the .txt file  https://stackoverflow.com/questions/35436331/how-to-save-output-from-dataframe-info-to-file-a-excel-or-text-file

I then used some formatting and headings and added in the summary of each indivdual class. 

The next thing I did was generate the profile_report, Using pp.ProfileReport(ids).
I found this to be one of the most interesting tools. It generates a report of the data. I used the: report.to_file('profile_report.html') line to create a .html version of the report as my version of vscode could not automatically display the report.

The report covers duplicate rows, samples, heatmaps, scatter plots of any combination of attributes. Histograms and in depth statistics. Personally I will not be using this report to make observations about the data, But this tool is a fantastic way to utilise python to analyse data. In depth analysis, easy to read and a lot of visual repersentaition of the data. 

The next set of graphs I created were the histograms. A set of histograms were created for each class for each attribute. A total for 12 hisotgrams, over 4 graphics. 
From the hisograms it is clear that most of the values and attributes are not distriuted evenly. I found the histograms to be less discriptive of the data than other graphics. 

The last two plots are scatter plots. These are 2 plots that are sepal lenght plotted verus sepal width, and petal lenght v petal width. 

These are two very informative graphs, These graphs has each class set by colour {'Iris-setosa':'red', 'Iris-versicolor':'yellow', 'Iris-virginica':'blue'} so you can see where each class is on the graph. 
There are a few notable points. 
One,  high corrolation across the board for petal lenght v petal width, this uniform line confirms what was suggested in the heat map.

Two, a slight over lap between Iris-versicolor and Iris-virginica at the respective, upper and lower ends as expected

Three, the clear seperation of the Iris-setosa is very visable. 

In the other scatter plot, for Sepallenght V sepal Width. 

The low correlation bewteen the width and leght as suggeted by the heat map is visable, not uniformity to the data displayed. 

Two, A Lot more over lap of the values of Iris-versicolor and Iris-virginica, These two are almost indistigushable based on the sepal values alone. 

Three, The Iris-setosa is again seperate from the other classes, for the sepal values this is more surprising, More over lap with the other two classes was expected here based off the dot and box graphs analysis. 

If given blind measurements, a Iris-setosa could be confidently distingushed from the other classes. Depending on the end of the scale the measurements are, I.E a slightly larger Iris-versicolor or a slightly smaller Iris-virginica the class of the Iris could not be easily determined. 

Overall, Using python to analyse the data was effective. The range, and possible custization using pandas and plotly is impressive. I had some seaborn graphs originally too, but I thought adding them for the sake of complexity was not necessary. Pandas and plotly covered every point necessary to adequately analysis this data. The funciton I was most impressed with was the pp.ProfileReport(ids), although I did not use it to come to conclusions on this data, it is a very powerful tool for very little effort to use. It covers most points required for a quick analysis of the data. The lack of customistaion with the function is the trade off. 
For more detailed and customised versions of the graphs more customised code has to be produced. 










Here is a comprehensive list of references I have used to come up with the solutions with in the project code.

Pands project references:
https://towardsdatascience.com/a-beginners-guide-to-data-analysis-in-python-188706df5447

https://stackoverflow.com/questions/52553062/pandas-profiling-doesnt-display-the-output

https://plotly.com/python/renderers/

https://plotly.com/python/static-image-export/

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg

https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/06_calculate_statistics.html

https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file

https://www.machinelearningplus.com/pandas/pandas-histogram/#:~:text=Default%20plot,column%20in%20the%20pandas%20dataframe.

https://stackoverflow.com/questions/31596084/save-dataframe-hist-to-a-file

https://stackoverflow.com/questions/19614400/add-title-to-collection-of-pandas-hist-plots

https://stackoverflow.com/questions/41174202/matplotlib-doesnt-forget-previous-data-when-saving-figures-with-savefig

https://kanoki.org/2020/08/30/matplotlib-scatter-plot-color-by-category-in-python/

https://matplotlib.org/3.5.0/gallery/lines_bars_and_markers/scatter_with_legend.html

https://stattrek.com/statistics/charts/compare-data-sets.aspx#:~:text=Common%20graphical%20displays%20(e.g.%2C%20dotplots,two%20or%20more%20data%20sets.

https://stackoverflow.com/questions/35436331/how-to-save-output-from-dataframe-info-to-file-a-excel-or-text-file