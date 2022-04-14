import pandas as pd
from pyparsing import line
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def string_to_milliseconds(string):
    hours, minutes, seconds = (["0", "0"] + string.split(":"))[-3:]
    hours = int(hours)
    minutes = int(minutes)
    seconds = float(seconds.replace(',', '.'))
    miliseconds = int(3600000 * hours + 60000 * minutes + 1000 * seconds)
    return miliseconds

df = pd.read_csv('MLPython/Lap_project/Laps_time.csv', sep=';', header=1)

lap_time_milliseconds = []

for string in df['lap_time']:
    lap_time_milliseconds.append(string_to_milliseconds(string))

df['lap_time_milliseconds'] = lap_time_milliseconds

# sns.relplot(data=df, x='lap_time_milliseconds', y='Qualità_giro', kind='line')

sns.relplot(data=df, x='Consumo_gomme', y='lap_time_milliseconds', hue='Stint', col='Gomme', kind='line')

plt.gca().invert_xaxis()
plt.show()