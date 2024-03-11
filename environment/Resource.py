import simpy
<<<<<<< HEAD
<<<<<<< HEAD
=======

from config import *

>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======

from config import *

>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
class Machine(object):
    def __init__(self, env, id):
        self.env = env
        self.id = id
        self.capacity = 1
        self.availability = simpy.Store(env, capacity=self.capacity)
        self.workingtime_log = []
        self.util_time = 0.0
<<<<<<< HEAD
<<<<<<< HEAD
        self.op_where = []

    def add_reference(self, op):
        self.op_where.append(op.id) # 처리한 op가 몇 번째였는지를 기록
=======
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282
=======
>>>>>>> 322e220bf514fcc8e59f3f4bb456154fb0501282


class Worker(object):
    def __init__(self, env, id):
        self.env = env
        self.id = id
        self.capacity = 1
        self.availability = simpy.Store(env, capacity=self.capacity)
        self.workingtime_log = []
        self.util_time = 0.0


class Jig(object):
    def __init__(self, env, id):
        self.env = env
        self.id = id
        self.capacity = 1
        self.availability = simpy.Store(env, capacity=self.capacity)
        self.workingtime_log = []
        self.util_time = 0.0
