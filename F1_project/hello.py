import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils

from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

import numpy as np
import pandas as pd
import seaborn as sns

ff1.Cache.enable_cache('cache')

def telemetry():

    year, grand_prix, session = 2022, 'Belgium', 'Practice 1'
    driver_1, driver_2, driver_3, driver_4  = 'VER', 'LEC', 'VER', 'PER'

    quali = ff1.get_session(year, grand_prix, session)
    quali.load()

    # Laps can now be accessed through the .laps object coming from the session
    laps_driver_1 = quali.laps.pick_driver(driver_1)
    laps_driver_2 = quali.laps.pick_driver(driver_2)

    # Select the fastest lap
    fastest_driver_1 = laps_driver_1.pick_fastest()
    fastest_driver_2 = laps_driver_2.pick_fastest()

    # Retrieve the telemetry and add the distance column
    telemetry_driver_1 = fastest_driver_1.get_telemetry().add_distance()
    telemetry_driver_2 = fastest_driver_2.get_telemetry().add_distance()

    # Make sure whe know the team name for coloring
    team_driver_1 = fastest_driver_1['Team']
    team_driver_2 = fastest_driver_2['Team']

    delta_time, ref_tel, compare_tel = utils.delta_time(fastest_driver_1, fastest_driver_2)

    plot_size = [15, 15]
    csv_name = f"{quali.event.year}_{quali.event.EventName}_{quali.name}"
    plot_title = f"{quali.event.year} {quali.event.EventName} - {quali.name} - {driver_1} VS {driver_2}"
    plot_ratios = [1, 3, 2, 1, 1, 2, 1]
    plot_filename = plot_title.replace(" ", "") + ".png"

    # Make plot a bit bigger
    plt.rcParams['figure.figsize'] = plot_size

    # Create subplots with different sizes
    fig, ax = plt.subplots(7, gridspec_kw={'height_ratios': plot_ratios})

    # Set the plot title
    ax[0].title.set_text(plot_title)


    # Delta line
    ax[0].plot(ref_tel['Distance'], delta_time)
    ax[0].axhline(0)
    ax[0].set(ylabel=f"Gap to {driver_2} (s)")

    # Speed trace
    ax[1].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Speed'], label=driver_1, color=ff1.plotting.driver_color(driver_1))
    ax[1].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Speed'], label=driver_2, color=ff1.plotting.driver_color(driver_2))
    ax[1].set(ylabel='Speed')
    ax[1].legend(loc="lower right")

    # Throttle trace
    ax[2].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Throttle'], label=driver_1, color=ff1.plotting.driver_color(driver_1))
    ax[2].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Throttle'], label=driver_2, color=ff1.plotting.driver_color(driver_2))
    ax[2].set(ylabel='Throttle')

    # Brake trace
    ax[3].plot(telemetry_driver_1['Distance'], telemetry_driver_1['Brake'], label=driver_1, color=ff1.plotting.driver_color(driver_1))
    ax[3].plot(telemetry_driver_2['Distance'], telemetry_driver_2['Brake'], label=driver_2, color=ff1.plotting.driver_color(driver_2))
    ax[3].set(ylabel='Brake')

    # Gear trace
    ax[4].plot(telemetry_driver_1['Distance'], telemetry_driver_1['nGear'], label=driver_1, color=ff1.plotting.driver_color(driver_1))
    ax[4].plot(telemetry_driver_2['Distance'], telemetry_driver_2['nGear'], label=driver_2, color=ff1.plotting.driver_color(driver_2))
    ax[4].set(ylabel='Gear')

    # RPM trace
    ax[5].plot(telemetry_driver_1['Distance'], telemetry_driver_1['RPM'], label=driver_1, color=ff1.plotting.driver_color(driver_1))
    ax[5].plot(telemetry_driver_2['Distance'], telemetry_driver_2['RPM'], label=driver_2, color=ff1.plotting.driver_color(driver_2))
    ax[5].set(ylabel='RPM')

    # DRS trace
    ax[6].plot(telemetry_driver_1['Distance'], telemetry_driver_1['DRS'], label=driver_1, color=ff1.plotting.driver_color(driver_1))
    ax[6].plot(telemetry_driver_2['Distance'], telemetry_driver_2['DRS'], label=driver_2, color=ff1.plotting.driver_color(driver_2))
    ax[6].set(ylabel='DRS')
    ax[6].set(xlabel='Lap distance (meters)')


    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for a in ax.flat:
        a.label_outer()
        
    # Store figure
    # plt.savefig(plot_filename, dpi=300)
    plt.show()

    #pd.DataFrame.to_csv(path_or_buf='F1_project/' + driver_1 + '_' + csv_name + '_Lap_time.csv', self=laps_driver_1)
    #pd.DataFrame.to_csv(path_or_buf='F1_project/' + driver_2 + '_' + csv_name + '_Lap_time.csv', self=laps_driver_2)
    #writeData(lapData=laps_driver_1, header=laps_driver_1.head(0).columns)

def race1():

    year, grand_prix, session = 2022, 'Italy', 'Race'
    driver_1,driver_2 = 'LEC', 'RUS'

    race = ff1.get_session(year, grand_prix, session)
    race.load()

    laps = race.load_laps().pick_drivers([driver_1,driver_2])

    laps = laps.pick_track_status('1')

    # Convert laptimes to seconds
    laps['LapTimeSeconds'] = laps['LapTime'].dt.total_seconds()

    sns.lineplot(x='LapNumber', y='LapTimeSeconds', data=laps, hue='Driver', marker='.')

    """
    laps_1 = laps.loc[laps['Driver'] == driver_1]['LapTimeSeconds'].tolist()
    laps_2 = laps.loc[laps['Driver'] == driver_2]['LapTimeSeconds'].tolist()
    LapTime = laps['LapNumber'].tolist()
    plt.fill_between(LapTime, laps_1, laps_2, alpha="0.3")
    """
    
    plt.show()
race1()