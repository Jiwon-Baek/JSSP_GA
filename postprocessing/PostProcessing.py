import pandas as pd
<<<<<<< HEAD
<<<<<<< HEAD
import os
from collections import OrderedDict, defaultdict


def machine_log(config):
    df = pd.read_csv(config.filepath['log'])
=======
=======
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
from collections import OrderedDict, defaultdict
from config import *


def machine_log(_filepath):
    df = pd.read_csv(_filepath)
<<<<<<< HEAD
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
    df = df.drop(df.columns[0], axis=1)
    # Filter 'Started' and 'Finished' events
    df_started = df[df['Event'] == 'Started'].drop(['Event', 'Process'], axis=1).reset_index(drop=True)
    df_finished = df[df['Event'] == 'Finished'].drop(['Event', 'Process'], axis=1).reset_index(drop=True)

    machine_start = []
    machine_finish = []
<<<<<<< HEAD
<<<<<<< HEAD
    for i in range(config.n_machine):
=======
    for i in range(NUM_MACHINE):
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======
    for i in range(NUM_MACHINE):
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
        machine_start.append(df_started[(df_started['Machine'] == 'M' + str(i))])
        machine_finish.append(df_finished[(df_finished['Machine'] == 'M' + str(i))])

        machine_start[i].reset_index(drop=True, inplace=True)
        machine_finish[i].reset_index(drop=True, inplace=True)
    data = []

<<<<<<< HEAD
<<<<<<< HEAD
    for i in range(config.n_machine):
=======
    for i in range(NUM_MACHINE):
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======
    for i in range(NUM_MACHINE):
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
        for j in range(len(machine_finish[i])):
            temp = {'Machine': i,
                    'Job': machine_start[i].loc[j, 'Part'],
                    'Start': int(machine_start[i].iloc[j, 0]),
                    'Finish': int(machine_finish[i].iloc[j, 0]),
                    'Delta': int(machine_finish[i].iloc[j, 0] - machine_start[i].iloc[j, 0])}
            data.append(temp)

    data = pd.DataFrame(data)
    data = data.sort_values(by=['Start'])
    data.reset_index(drop=True, inplace=True)
<<<<<<< HEAD
<<<<<<< HEAD
    if config.save_machinelog:
        data.to_csv(config.filepath['machine'])
=======
    data.to_csv('./result/' + filename + '_machine_log.csv')
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======
    data.to_csv('./result/' + filename + '_machine_log.csv')
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
    return data
