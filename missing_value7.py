# quando i dati a disposizione sono numerosi là dove è presente un dato mancante in una cella può convenire eliminare l'intera riga
# lo stesso non si può fare quando i dati sono meno numerosi le classi utilizzate per recuperare dati mancanti sono le IMPUTER
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

X = [ # età, sesso
    [20, np.nan],
    [np.nan, 'm'],
    [30, 'f'],
    [35, 'f'],
    [np.nan, np.nan]
]

# sfrutto il ct per 'imputare' i dati sconosciuti
trasformers = [
    ['age_imputer', SimpleImputer(strategy='median'), [0]], # la strategia di default del simpleImputer è la media dei valori che ha a disposizione
    ['sex_imputer', SimpleImputer(strategy='most_frequent'), [1]],
]

ct = ColumnTransformer(trasformers)
X = ct.fit_transform(X)
 
print(X)