from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import numpy as np

np.random.seed(2) 

# grazie al codice sopra tutte le operazioni randomiche come il train_test_split
# avranno i valori numerici generati casualmente ma sempre allo stesso modo (forzando la loro estrazione)

dataset = fetch_california_housing()

X = dataset['data'] # matrice feature lotti
y = dataset['target'] # array prezzi lotti

# per garantire il funzionamento del modello invece che dare in pasto al.fit tutti i dati a mia disposizione
# ne dò soltanto una parte (70/75% dei dati) da questi ricavo il modello, mentre la seconda sarà utilizzata per fare test/validazione

X_train, X_test, y_train, y_test = train_test_split(X, y) # la funzione restituisce una tupla da 4 variabili
model = LinearRegression() # costruisco il modello NON addestrato
model.fit(X_train, y_train) # addestramento del modello CON validazione

p_train = model.predict(X_train) # predizione rispetto ai dati di X_train
p_test = model.predict(X_test) # predizione rispetto ai dati di X_test

mae_test = mean_absolute_error(y_test, p_test) # calcoliamo l'errore medio della predizione rispetto ai dati di test
mae_train = mean_absolute_error(y_train, p_train) # calcoliamo l'errore medio della predizione rispetto ai dati di train
print('MAE train', mae_train)
print('MAE test', mae_test)