from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
# from sklearn.preprocessing import RobustScaler
import numpy as np

np.random.seed(2)

df = pd.read_csv('Student_project/student-mat.csv', sep=';')

column_to_be_droped = ['G3', 'reason', 'famsize', 'guardian']
y = df['G3']
df.drop(column_to_be_droped, axis=1, inplace=True)

trasformers = [
    ['school_trasf', OneHotEncoder(), ['school', 'sex', 'address', 'Pstatus', 'Mjob',
     'Fjob', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']]
    # ['scaler', RobustScaler(), ['G2', 'G1', 'age', ]]
]
ct = ColumnTransformer(trasformers, remainder='passthrough')

X = ct.fit_transform(df)

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LinearRegression()
model.fit(X_train, y_train)

p_train = model.predict(X_train)
p_test = model.predict(X_test)

mea_train = mean_absolute_error(y_train, p_train)
mea_test = mean_absolute_error(y_test, p_test)

print(f'mean grade = {y.mean()}')
print(f'Train = {mea_train}, Test = {mea_test}')