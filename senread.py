from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import csv
import pandas as pd

path = "csv/Sub_Amaya/1.csv"
df = pd.read_csv(path)
df = df.filter(regex='(TimeStamp|F7)')
df = df.ix[:, ~df.columns.str.contains('CQ')]
df.set_index('TimeStamp')
axes = df.plot.line(subplots=True)

plt.show()

# AF3 F7 F3 FC5 T7 P7 O1 O2 P8 T8 FC6 F4 F8 AF4