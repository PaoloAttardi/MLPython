import pandas as pd
from sklearn.datasets import load_wine
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, QuantileTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from validation2 import X_train

dataset = load_wine()

# vediamo il confronto tra magnesio, con deviazione standard alta, rispetto ai fenoli con deviazione standard molto minore
X = dataset['data'][:, [4, 7]] # in X isoliamo le colonne di magnesio e fenoli i 2 punti specificano di selezionare l'intera colonna

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

df = pd.DataFrame(X, columns=['magnesium', 'phenols'])

# per graficare i dati si utilizza la libreria seaborn 
g = sns.scatterplot(data=df, x='magnesium', y='phenols')

# seaborn scala direttamente i dati, per vederli in maniera neutra così come glieli abbiamo dati
# andiamo ad impostare gli stessi limiti di scala tra gli assi
#g.set(xlim=(-10, 200), ylim=(-10, 200)) così per vedere i dati 'puliti'

#plt.show()

X = dataset['data']
y = dataset['target']

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = KNeighborsClassifier()
model.fit(X_train, y_train)

# p_train = model.predict(X_train)
p_test = model.predict(X_test)

acc_not_scaled = accuracy_score(y_test, p_test)

X = dataset['data']
y = dataset['target']

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

model2 = KNeighborsClassifier()
model2.fit(X, y)

p = model2.predict(X)

acc_scaled = accuracy_score(y, p)

print(f'acc not scaled {acc_not_scaled}, acc scaled {acc_scaled}')