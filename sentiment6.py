import pandas as pd

# df = dataframe
df = pd.read_csv('movie_review.csv') # read_csv permette la lettura di un csv, funziona anche con una url dalla quale scarica il file e lo parsa

print(df.head())