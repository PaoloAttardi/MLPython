import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Covid_project/data_download_file_reference_2022.csv')
# stat = df.describe()

# il df permette tre diverse 'predizioni' una a bassa diffusione una a media e una ad alta diffusione del virus, si prende in esempio la media diffusione

var = ['mean']

colums_to_be_used = ['inf_' + var[0], 'seir_cumulative_' + var[0], 'inf_cuml_' + var[0],
'seir_daily_' + var[0], 'seir_daily_unscaled_' + var[0], 'seir_cumulative_unscaled_' + var[0], 'Cases_' + var[0], ]

filtered = df[df["location_name"] == 'Italy']

print(filtered.head())