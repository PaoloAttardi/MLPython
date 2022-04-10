import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Student_project/student-mat.csv', sep=';')

# print(df.head())

table_to_be_droped = ['G3', 'reason']
y = df['G3']
# X = df.drop(table_to_be_droped, axis=1, inplace=True)

# sns.barplot(data=df, x='studytime', y='G3')

sns.relplot(data=df, x='G1', y='G3', kind='line')

plt.show()