from traffictools.car import *
from traffictools.airplane import *

class FlyingCar(Airplane, Car):
    def __init__(self):
        super().__init__()
