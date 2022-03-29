# vediamo la preparazione dei dati divisa in tre parti principali 
# 1. vettorizzazione -> trasfm. dati non numerici in numerici
# 2. sostituzione dei valori mancanti 
# 3. scalatura delle feature

from sklearn.compose import ColumnTransformer #il trasformer permette di trasformare determinate colonne con anche scalatura o sostituzione valori mancanti
from sklearn.preprocessing import OneHotEncoder 

# creo un dataset da zero a tre feature
X = [# peso, altezza, sport
    [ 110, 1.70, 'rugby'],
    [ 100, 1.90, 'basket'],
    [ 120, 1.90, 'rugby'],
    [  70, 1.60, 'soccer']
]

transformers = [
    # nome del trasf, 'strategia' di trasf., colonna a cui applicarla 
    ['category_vectorizer', OneHotEncoder(), [2]]
]
ct = ColumnTransformer(transformers, remainder='passthrough')
ct.fit(X) # passiamo i dati da trasformare
X = ct.transform() # trasforma i dati passati
# si può scrivere anche così direttamente X = ct.fit_trasform(X) 