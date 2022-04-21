import pandas as pd
import pandas_profiling as pp
import csv
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

fieldnames = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth','class']
lines = ""
with open('iris_csv.csv') as f:
    csv_reader = csv.DictReader(f, fieldnames)
    next(csv_reader)
    for line in csv_reader:
         lines = lines + f"The lenght of the Sepal {line['sepallength']} and the Width of the sepal is {line['sepalwidth']} and is in the class {line['class']} \n"

with open('summary.txt', 'w') as f:
    f.writelines(lines)