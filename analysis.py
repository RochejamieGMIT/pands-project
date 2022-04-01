import pandas as pd

import seaborn as sb
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# reading csv files
data =  pd.read_csv('iris_csv.csv')
#print(df)
data.head()
data.shape
data.info()
print(data.describe())
data.isnull().sum()

up_dt = {}

  
print(up_dt)
sb.scatterplot(x='petallength', y='petalwidth',
               hue='class', data=data, )


plt.legend()
plt.savefig('testMultiSave.png')

 
sb.scatterplot(x='sepalwidth', y='sepallength',
                hue='class', data=data, )
plt.legend()
plt.savefig('testMultiSave2.png')


plt.show()

