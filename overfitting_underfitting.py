import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

np.random.seed(0)

X = np.arange(0, 10, 0.2) # permette di generare numeri in un certo intervallo  e con uno step di 0.2
n = len(X)

y = np.cos(X) + (2*np.random.random(n)) #il secondo elemento aggiunge un po' di 'rumore' prova a commentarlo e rieseguire il codice
X = np.expand_dims(X, axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y)
model = MLPRegressor(hidden_layer_sizes=[50], max_iter=10000, tol=-1, verbose=2)

model.fit(X_train, y_train)

p_train = model.predict(X_train)
p_test = model.predict(X_test)
p = model.predict(X)

mae_train = mean_absolute_error(y_train, p_train)
mae_test = mean_absolute_error(y_test, p_test)
print(f'Train {mae_train}, test {mae_test}')

sns.scatterplot(x=X_train[:, 0], y=y_train)
sns.scatterplot(x=X_test[:, 0], y=y_test)
sns.lineplot(x=X[:,0], y=p)

plt.show()