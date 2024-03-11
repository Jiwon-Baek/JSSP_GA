<<<<<<< HEAD
<<<<<<< HEAD

=======
from data import op_data
from config import *
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======
from data import op_data
from config import *
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282

# region Operation
class Operation(object):
    """
    This class does not act as a process.
    Instead, this is just a member variable of a job that contains process info.
    This class is only used when generating a job sequence.
    The Process class is to be generated further.
    """

<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, env, id, part_name, process_type, machine, process_time, requirements=None):
=======
    def __init__(self, env, id, part_name, process_type, machine_list, process_time, requirements=None):
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======
    def __init__(self, env, id, part_name, process_type, machine_list, process_time, requirements=None):
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282

        self.id = id
        self.process_type = process_type
        self.process_time = process_time
        self.part_name = part_name
        self.name = part_name + '_Op' + str(id)

        # In the simplest Job Shop problem, process type is often coincide with the machine type itself.
<<<<<<< HEAD
<<<<<<< HEAD
        self.machine = machine
=======
        self.machine_list = machine_list
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======
        self.machine_list = machine_list
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
        if requirements is None:
            self.requirements = env.event()  # preceding event
            if id == 0:
                self.requirements.succeed()
        else:
            # if there are more requirements, more env.event() can be added up
            # you can handle events using Simpy.AllOf() or Simpy.AnyOf()
            self.requirements = [env.event() for i in range(5)]  # This is an arbitrary value


# endregion

# region Job
class Job(object):
    """
    A job is to be repeatedly generated in a source.
    (Job1_1, Job1_2, Job1_3, ..., Job1_100,
    Job2_1, Job2_2, Job2_3, ..., Job2_100,
    ...                         Job10_100)

    Member Variable : part_type, id
    """

<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, env, part_type, id, op_data):
=======
    def __init__(self, env, part_type, id):
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======
    def __init__(self, env, part_type, id):
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
        self.part_type = part_type
        self.id = id
        self.name = 'Part' + str(part_type) + '_' + str(id)
        self.step = -1
        self.loc = None  # current location
        self.op = [Operation(env,
                             id=j, part_name=self.name,
                             process_type=op_data[part_type][j][0],
<<<<<<< HEAD
<<<<<<< HEAD
                             machine=op_data[part_type][j][0],
=======
                             machine_list=op_data[part_type][j][0],
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======
                             machine_list=op_data[part_type][j][0],
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
                             process_time=op_data[part_type][j][1],
                             requirements=None) for j in range(len(op_data[part_type]))]


# endregion Job

