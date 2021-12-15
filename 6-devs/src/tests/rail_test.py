from pypdevs.DEVS import CoupledDEVS

from models.rail import Rail
from models.trolley import Trolley
from tests.trolley_collector import TrolleyCollector
from tests.trolley_generator import TrolleyGenerator


class RailTest(CoupledDEVS):
    def __init__(self):
        super().__init__("RailTest")
        trollies = [Trolley(20, 0, []), Trolley(100, 0, [])]

        self.generator = self.addSubModel(TrolleyGenerator(mu=20, sigma=0, trollies=trollies))
        self.collector = self.addSubModel(TrolleyCollector())
        self.junction = self.addSubModel(Rail(3000))

        self.connectPorts(self.generator.output, self.junction.input)
        self.connectPorts(self.junction.output, self.collector.input)

