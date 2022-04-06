import pandas as pd
import pandas_profiling as pp

import seaborn as sb
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# reading csv files
ids =  pd.read_csv('iris_csv.csv')
#print(df)
ids.head()
#print(ids.shape)
report = pp.ProfileReport(ids)

report.to_file('profile_report.html') # To preview data had to create a .html file as vs code could not open it
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
