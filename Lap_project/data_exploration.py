import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from math import modf

"""
def string_to_milliseconds(string):
    hours, minutes, seconds = (["0", "0"] + string.split(":"))[-3:]
    hours = int(hours)
    minutes = int(minutes)
    seconds = float(seconds.replace(',', '.'))
    miliseconds = int(3600000 * hours + 60000 * minutes + 1000 * seconds)
    return miliseconds
"""

def secondToLapTime(string):
    minutes = int(string // 60)
    fraz,seconds = modf(string - 60 * minutes)
    fraz = fraz * 100
    fraz1,milliseconds = modf(fraz)
    lapTime = str(minutes) + ':' + str(int(seconds)) + '.' + str(int(milliseconds))
    return lapTime

df = pd.read_csv('MLPython/Lap_project/Readable_lap_time.csv')

# sns.relplot(data=df, x='lap_time_milliseconds', y='Qualità_giro', kind='line')

result = []

for lapTime in df['lastLapTime']:
    result.append(secondToLapTime(lapTime))

df['LapTime'] = result
sns.relplot(data=df, x='currentLapNum', y='lastLapTime', col='sessionUID', hue='tyreCompound', kind='line').fig.suptitle('Laps Time')

sns.relplot(data=df, x='tyresAgeLaps', y='tyresWear', col='tyreCompound', kind='line').fig.suptitle('Tyres Wear')

plt.show()