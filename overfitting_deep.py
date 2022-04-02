from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score

n = 100 
# creiamo un dataset senza correlazione tra input e output, in questo modo verifichiamo come il modello vada a 'imparare a memoria'
# soffrendo dunque di overfitting

X = np.random.random(size=(n, 5)) # ho 100 record con 5 feature ciascuna
y = np.random.choice(['si', 'no'], size=n)

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = MLPClassifier(hidden_layer_sizes=[1000, 500], verbose=2) # per verificare l'underfitting basta modificare hidden_layer_sizes=[1]
model.fit(X_train, y_train)

p_train = model.predict(X_train)
p_test = model.predict(X_test)

acc_train = accuracy_score(y_train, p_train)
acc_test = accuracy_score(y_test, p_test)

print(f'Train {acc_train}, Test{acc_test}') 
# dal risultato delle accuratezze evinco un 100% sul train imparato a memoria,
# e un 50% circa sul test che equivale a tirare a caso avendo solo due output possibili