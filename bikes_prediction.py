import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import RobustScaler # oltre che a scalare si occupa anche dei valori estremi
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('hour.csv')

y = df['cnt']
colums_to_be_deleted = ['cnt', 'casual', 'registered', 'dteday', 'instant'] # instant è un id NON va considerato
df.drop(colums_to_be_deleted, axis=1, inplace=True)

transformers = [
    ['oneHot', OneHotEncoder(), ['season', 'yr', 'mnth', 'hr', 'weekday', 'weathersit']], # ciò migliora molto le prestazioni
    ['scaler', RobustScaler(), ['temp', 'atemp', 'hum', 'windspeed']] # non migliora in quanto le feature sono tutte comprese tra 0 e 1
]
# trasformo tutte le variabili a categoria cercando di migliorare le prestazioni

ct = ColumnTransformer(transformers, remainder='passthrough')

X = ct.fit_transform(df)

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LinearRegression()
model.fit(X_train, y_train)

p_train = model.predict(X_train)
p_test = model.predict(X_test)

mae_train = mean_absolute_error(y_train, p_train)
mae_test = mean_absolute_error(y_test, p_test)

print(f'Median cnt {np.median(y)}')
print(f'Train {mae_train}, test {mae_test}')