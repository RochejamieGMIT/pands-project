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

for r in data:
    if r["class"] == "Iris-setosa":
        row = {'sepallength': r['sepallength'],
            'sepalwidth': r['sepalwidth'],
            'petallength': r['petallength'],
            'petalwidth': r['petalwidth'],
            'class': '1'}
    up_dt.append(row)
  
print(up_dt)
sb.scatterplot(x='petallength', y='petalwidth',
               hue='class', data=data, )


plt.legend()
plt.savefig('testMultiSave.png')

 
sb.scatterplot(x='sepalwidth', y='sepallength',
                hue='class', data=data, )
plt.legend()
plt.savefig('testMultiSave2.png')
  



fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x = data['sepallength']
y = data['sepalwidth']
z = data['class']

ax.set_xlabel("sepallength")
ax.set_ylabel("sepalwidth")
ax.set_zlabel("class")

ax.scatter(x, y, z)

plt.show()

