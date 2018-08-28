from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import csv
import pandas as pd

filename = 'Exp01_2018.07.10_15.07.03.bp' 
path = "csv/Sub_Amaya/%s.csv" % filename
dfall = pd.read_csv(path)


bands = ['AF3', 'F7', 'FC5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F8', 'AF4']
for band in bands:
    df = dfall.filter(regex="(TimeStamp|%s)" % band)
    df = df.ix[:, ~df.columns.str.contains('CQ')]
    df.set_index('TimeStamp')
    axes = df.plot.line(subplots=True)
    fig = plt.gcf()
    fig.savefig('Amaya/%s-%s.png' % (filename, band))


# F3
df = dfall.filter(regex="(TimeStamp|F3)")
df = df.ix[:, ~df.columns.str.contains('CQ')]
df = df.ix[:, ~df.columns.str.contains('AF3')]
df.set_index('TimeStamp')
axes = df.plot.line(subplots=True)
fig = plt.gcf()
fig.savefig('Amaya/%s-F3.png' % filename)

# F4
df = dfall.filter(regex="(TimeStamp|F4)")
df = df.ix[:, ~df.columns.str.contains('CQ')]
df = df.ix[:, ~df.columns.str.contains('AF4')]
df.set_index('TimeStamp')
axes = df.plot.line(subplots=True)
fig = plt.gcf()
fig.savefig('Amaya/%s-f4.png' % filename)