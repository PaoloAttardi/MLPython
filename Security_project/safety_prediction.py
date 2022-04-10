from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd

df = pd.read_csv('Security_project/car.csv')

y = df['target']
column_to_be_droped = ['target']
df.drop(column_to_be_droped, axis=1, inplace=True)

transformers = [
    ['text_trasform', OneHotEncoder(), ['buying', 'maint', 'safety', 'lug_boot']]
]

ct = ColumnTransformer(transformers)
X = ct.fit_transform(df)

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = BernoulliNB()
model.fit(X_train, y_train)

p_train = model.predict(X_train)
p_test = model.predict(X_test)

cla_train = classification_report(y_train, p_train)
cla_test = classification_report(y_test, p_test)

acc_train = accuracy_score(y_train, p_train)
acc_test = accuracy_score(y_test, p_test)

print('\n')
print(f'Train = {acc_train}, Test = {acc_test}')
print('\n')