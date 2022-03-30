# si utilizza un nuovo dataset per sfruttare i classificatori, ovvero Iris dataset

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

datasets = load_iris()

X = datasets['data']
y = datasets['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

p_train = model.predict(X_train)
p_test = model.predict(X_test)

acc_train = accuracy_score(y_train, p_train) # si misura l'accuratezza del modello non l'errore assoluto medio
acc_test = accuracy_score(y_test, p_test)
print(f'train {acc_train}, test {acc_test}') # l'accuratezza è in percentuale 1 -> 100%