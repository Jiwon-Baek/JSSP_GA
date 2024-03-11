import pandas as pd
<<<<<<< HEAD
<<<<<<< HEAD

# region Monitor
class Monitor(object):
    def __init__(self, config):
        self.config = config  ## Event tracer 저장 경로
=======
=======
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
from config import *

# region Monitor
class Monitor(object):
    def __init__(self, filepath):
        self.filepath = filepath  ## Event tracer 저장 경로
<<<<<<< HEAD
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
        self.time = list()
        self.event = list()
        self.part = list()
        self.process_name = list()
        self.machine_name = list()

    def record(self, time, process, machine, part_name=None, event=None):
        self.time.append(time)
        self.event.append(event)
        self.part.append(part_name)  # string
        self.process_name.append(process)
        self.machine_name.append(machine)

    def save_event_tracer(self):
        event_tracer = pd.DataFrame(columns=['Time', 'Event', 'Part', 'Process', 'Machine'])
        event_tracer['Time'] = self.time
        event_tracer['Event'] = self.event
        event_tracer['Part'] = self.part
        event_tracer['Process'] = self.process_name
        event_tracer['Machine'] = self.machine_name
<<<<<<< HEAD
<<<<<<< HEAD
        if self.config.save_log:
            event_tracer.to_csv(self.config.filename['log'])
=======

        event_tracer.to_csv(self.filepath)
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======

        event_tracer.to_csv(self.filepath)
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282

        return event_tracer


# endregion

def monitor_by_console(console_mode, env, part, object='Single Part', command=''):
    if console_mode:
        operation = part.op[part.step]
        command = " " + command + " "
        if object == 'Single Part':
            if operation.process_type == 0:
<<<<<<< HEAD
<<<<<<< HEAD
                print(str(env.now) + '\t' + str(operation.name) + command + 'M' + str(operation.machine))
        elif object == 'Single Job':
            if operation.part_name == 'Part0_0':
                print(str(env.now) + '\t' + str(operation.name) + command + 'M' + str(operation.machine))
        elif object == 'Entire Process':
            print(str(env.now) + '\t' + str(operation.name) + command + 'M' + str(operation.machine))
=======
=======
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
                print(str(env.now) + '\t' + str(operation.name) + command + 'M' + str(operation.machine_list))
        elif object == 'Single Job':
            if operation.part_name == 'Part0_0':
                print(str(env.now) + '\t' + str(operation.name) + command + 'M' + str(operation.machine_list))
        elif object == 'Entire Process':
            print(str(env.now) + '\t' + str(operation.name) + command + 'M' + str(operation.machine_list))
<<<<<<< HEAD
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
        elif object == 'Machine':
            print_by_machine(env, part)


def print_by_machine(env, part):
<<<<<<< HEAD
<<<<<<< HEAD
    if part.op[part.step].machine == 0:
        print(str(env.now) + '\t\t\t\t' + str(part.op[part.step].name))
    elif part.op[part.step].machine == 1:
        print(str(env.now) + '\t\t\t\t\t\t\t' + str(part.op[part.step].name))
    elif part.op[part.step].machine == 2:
        print(str(env.now) + '\t\t\t\t\t\t\t\t\t\t' + str(part.op[part.step].name))
    elif part.op[part.step].machine == 3:
        print(str(env.now) + '\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(part.op[part.step].name))
    elif part.op[part.step].machine == 4:
=======
=======
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
    if part.op[part.step].machine_list == 0:
        print(str(env.now) + '\t\t\t\t' + str(part.op[part.step].name))
    elif part.op[part.step].machine_list == 1:
        print(str(env.now) + '\t\t\t\t\t\t\t' + str(part.op[part.step].name))
    elif part.op[part.step].machine_list == 2:
        print(str(env.now) + '\t\t\t\t\t\t\t\t\t\t' + str(part.op[part.step].name))
    elif part.op[part.step].machine_list == 3:
        print(str(env.now) + '\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(part.op[part.step].name))
    elif part.op[part.step].machine_list == 4:
<<<<<<< HEAD
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
        print(str(env.now) + '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(part.op[part.step].name))
    else:
        print()
