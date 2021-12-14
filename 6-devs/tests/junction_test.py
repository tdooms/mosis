from pypdevs.DEVS import CoupledDEVS

from models.collector import Collector
from models.generator import Generator

class JunctionTest(CoupledDEVS):
    def __init__(self):
        super().__init__("JunctionTest")
        self.generator = self.addSubModel(Generator(origin=0, destinations=[0]))
        self.collector = self.addSubModel(Collector(origin=0))

        self.connectPorts(self.generator.passenger_entry, self.collector.depart)

