import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('hour.csv')
stat = df.describe()

# print(stat)

# sns.barplot(data=df, x='hr', y='cnt')

# for c in ['season', 'yr', 'mnth', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit']:
    # sns.barplot(data=df, x=c, y='cnt')
    # plt.show()

# for c in ['temp', 'atemp', 'hum', 'windspeed']:
    # sns.scatterplot(data=df, x=c, y='cnt')
    # plt.show()

# sns.barplot(data=df, x='hr', y='cnt', hue='workingday')
# hue permette di visualizzare se il giorno in questione è lavorativo o meno

# sns.relplot(data=df, x='hr', y='cnt', hue='season', col='workingday', kind='line')

# plt.show()