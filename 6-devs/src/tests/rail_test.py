from pypdevs.DEVS import CoupledDEVS

from models.rail import Rail
from models.trolley import Trolley
from tests.trolley_collector import TrolleyCollector
from tests.trolley_generator import TrolleyGenerator


class RailTest(CoupledDEVS):
    def __init__(self):
        super().__init__("RailTest")
        trollies = [Trolley("one", 20, "main", [], 2), Trolley("one", 20, "main", [], 2), Trolley("two", 100, "main", [], 2)]

        self.generator = self.addSubModel(TrolleyGenerator(mu=1, sigma=0, trollies=trollies))
        self.collector = self.addSubModel(TrolleyCollector())
        self.rail = self.addSubModel(Rail(3000))

        self.connectPorts(self.generator.output, self.rail.input)
        self.connectPorts(self.rail.output, self.collector.input)

