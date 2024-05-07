import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Covid_project/data_download_file_reference_2022.csv')
# stat = df.describe()

# il df permette tre diverse 'predizioni' una a bassa diffusione una a media e una ad alta diffusione del virus, si prende in esempio la media diffusione

var = ['mean']

filtered = df[df["location_name"] == 'Italy']
df = filtered.get([
    'date','inf_' + var[0], 'seir_cumulative_' + var[0], 'inf_cuml_' + var[0],
    'seir_daily_' + var[0], 'seir_daily_unscaled_' + var[0], 'seir_cumulative_unscaled_' + var[0], 'cases_' + var[0], 'reff_' + var[0],
    'cumulative_deaths', 'daily_deaths','cumulative_cases','cumulative_hospitalizations',
    'daily_cases','population','mobility_' + var[0],'testing_'+ var[0],'pneumonia_'+ var[0],'mask_use_'+ var[0],'cumulative_all_vaccinated',
    'cumulative_all_fully_vaccinated','hospital_beds_'+ var[0],'icu_beds_'+ var[0],'admis_'+ var[0],'all_bed_capacity','icu_bed_capacity',
    'infection_fatality','infection_detection','infection_hospitalization'
])

# sns.relplot(data=df, x='cumulative_all_fully_vaccinated', y='daily_cases', kind='line')
# sns.relplot(data=df, x='daily_cases', y='daily_deaths', hue='cumulative_all_fully_vaccinated')
print(df['cumulative_all_fully_vaccinated'][10918])

plt.show()