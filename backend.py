from matplotlib import pyplot as plt
import fastf1 as ff1
import os
import pandas as pd
from fastf1.core import Laps

def setup():
    ff1.Cache.enable_cache(os.getcwd())


def load_summary(year, circuit):
    fp1 = create_summary(ff1.get_session(year, circuit, 'FP1'))
    fp2 = create_summary(ff1.get_session(year, circuit, 'FP2'))
    fp3 = create_summary(ff1.get_session(year, circuit, 'FP3'))
    return fp1, fp2, fp3


def create_summary(session):
    print("creating summary")
    laps = session.load_laps()
    drivers = pd.unique(laps['Driver'])
    list_fastest_laps = list()
    for drv in drivers:
        drvs_fastest_lap = laps.pick_driver(drv).pick_fastest()
        list_fastest_laps.append(drvs_fastest_lap)
    o_laps = Laps(list_fastest_laps).sort_values(by='LapTime').reset_index(drop=True)
    o_laps = o_laps[['Driver', 'LapTime', 'Compound']]

    o_laps['LapTime'] = o_laps['LapTime'].apply(lambda x: strfdelta(x))
    return o_laps


def strfdelta(tdelta):
    cmp = tdelta.components
    time_string = str(cmp[2])+":"+str(cmp[3])+":"+str(cmp[4])
    return time_string


def load_laps(year, circuit, fp1, fp2, fp3):
    print("loading laps")
    fp1 = create_heat_map(ff1.get_session(year, circuit, 'FP1').load_laps(), fp1['Driver'])
    fp2 = create_heat_map(ff1.get_session(year, circuit, 'FP2').load_laps(), fp2['Driver'])
    fp3 = create_heat_map(ff1.get_session(year, circuit, 'FP3').load_laps(), fp3['Driver'])
    return fp1, fp2, fp3


def create_heat_map(laps, drivers):
    list_driver_laps = list()
    for drv in drivers:
        drvs_laps = laps.pick_driver(drv).reset_index()
        float_laptime = drvs_laps["LapTime"].apply(lambda x: float_tdelta(x))
        list_driver_laps.append(float_laptime)
    heatmap = pd.concat(list_driver_laps, axis=1)
    heatmap.columns = drivers
    return heatmap

def float_tdelta(tdelta):
    try:
        cmp = tdelta.components
        time = cmp[2]*60 + cmp[3] + cmp[4]/1000
    except:
        time = float("inf")
    return time



def rest():
    laps = monza_quali.load_laps(with_telemetry=True)
    fast_leclerc = laps.pick_driver('LEC').pick_fastest()
    lec_car_data = fast_leclerc.get_car_data()
    t = lec_car_data['Time']
    vCar = lec_car_data['Speed']

# The rest is just plotting
    fig, ax = plt.subplots()
    ax.plot(t, vCar, label='Fast')
    ax.set_xlabel('Time')
    ax.set_ylabel('Speed [Km/h]')
    ax.set_title('Leclerc is')
    ax.legend()
    plt.show()