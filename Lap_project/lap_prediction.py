import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
import pickle

def string_to_milliseconds(string):
    hours, minutes, seconds = (["0", "0"] + string.split(":"))[-3:]
    hours = int(hours)
    minutes = int(minutes)
    seconds = float(seconds.replace(',', '.'))
    miliseconds = int(3600000 * hours + 60000 * minutes + 1000 * seconds)
    return miliseconds

df = pd.read_csv('Lap_project/Laps_time.csv', sep=';', header=1)

lap_time_milliseconds = []

for string in df['lap_time']:
    lap_time_milliseconds.append(string_to_milliseconds(string))

df['lap_time_milliseconds'] = lap_time_milliseconds

y = df['Consumo_gomme']
column_to_be_droped = ['Consumo_gomme', 'lap_time']
df.drop(column_to_be_droped, axis=1, inplace=True)

trasformers = [
    ['trasf', OneHotEncoder(), ['Circuito', 'Macchina', 'Pilota', 'Meteo', 'Gomme',
     'Qualita_giro', 'Tipo_assetto']]
    # ['scaler', RobustScaler(), ['G2', 'G1', 'age', ]]
]
ct = ColumnTransformer(trasformers, remainder='passthrough')

X = ct.fit_transform(df)

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LinearRegression()

"""
model.fit(X_train, y_train)

# si usa pickle per salvare i modello su un file pickle, una volta salvato non servirà più l'addestramento o la sovracrittura del modello
# a meno di volerlo aggiornare ad ogni nhuova aggiunta di dati in un altro script

with open('lapmodel.pickle', 'wb') as f:
    pickle.dump(model, f)
"""
pickle_in = open('lapmodel.pickle', 'rb')
model = pickle.load(pickle_in)

p_train = model.predict(X_train)
p_test = model.predict(X_test)

mea_train = mean_absolute_error(y_train, p_train)
mea_test = mean_absolute_error(y_test, p_test)

print(f'mean grade = {y.mean()}')
print(f'Train = {mea_train}, Test = {mea_test}')