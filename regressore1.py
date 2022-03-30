from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_absolute_error

dataset = load_boston()

# in dataset carichiamo tutti i dati presi dalla libreria sklearn.dataset 
# questi sono divisibili in una matrice X di 13 colonne e 506 righe che descrivono
# criminalità, inquinamento, età media... di un lotto abitativo della città di boston
# per visualizzarlo basta utilizzare print(dataset['data'])
# inoltre, dentro la chiave target print(dataset['target'])
# abbiamo il prezzo risultante del lotto che sarà un array di 506 numeri corrispondenti
# ai lotti abitativi di cui sopra, quindi:

X = dataset['data'] # matrice feature lotti
y = dataset['target'] # array prezzi lotti

# addestriamo direttamente un algoritmo per ricavare il modello del dataset 
# utiliziamo un algoritmo di addetsramento proprio di sklearn ovvero regressione lineare

# in M.L. si differenziano regressori e classificatori
# i regressori sono modelli usati per algoritmi che devono dare in output un numero
# nel nostro caso la stima di un prezzo di una casa
# il classificatore tira fouri output a categoria (giallo, rosso, blu) o (maschio, femmina) ecc...

model = LinearRegression() # costruisco il modello NON addestrato
model.fit(X, y) # addestramento del modello SENZA validazione

p = model.predict(X) # predizione rispetto ai dati di X

# la situazione è la seguente X = f(y) con .fit noti X e y troviamo f
# con .predict nota ora f passiamo dei dati (X stesso in questo caso) e otteniamo una predizione di y

mae = mean_absolute_error(y, p) # calcoliamo l'errore medio della predizione
print('MAE', mae)