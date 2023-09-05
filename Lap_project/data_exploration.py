import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def meanLapTime(session):
    lapTime = []
    for currentsession in df['sessionUID']:
        if currentsession == session:
            lapTime.append(df['lastLapTime'])
    return np.mean(lapTime)

df = pd.read_csv('../MLPython/Lap_project/Readable_lap_time.csv')

session = df['sessionUID'][0]

timeLimit = meanLapTime(session) + 4

df = df[df['lastLapTime'] < timeLimit]

sns.relplot(data=df, x='currentLapNum', y='lastLapTime', col='sessionUID', hue='tyreCompound', kind='line')
plt.show()

sns.boxplot(data=df, x='tyreCompound', y='lastLapTime', showmeans=True)
plt.show()

sns.relplot(data=df, x='tyresAgeLaps', y='tyresWear', hue='tyreCompound', kind='line')
plt.title('Tyres Wear')
plt.show()

sns.relplot(data=df, x='fuelInTank', y='lastLapTime', col='setUpName', kind='line', markers='.')
plt.gca().invert_xaxis()
plt.show()