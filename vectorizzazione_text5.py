from sklearn.feature_extraction.text import CountVectorizer

# bag of words permette di vettorizzare i testi ma perdendo l'ordine delle parole (non efficiente)
X = [
    'ciao ciao miao',
    'miao',
    'miao bao' 
]

vectorize = CountVectorizer()
vectorize.fit(X)
X = vectorize.transform(X)

print(vectorize.get_feature_names())
print(X.todense())
# print(X) printa con una notazione proprio di sklearn