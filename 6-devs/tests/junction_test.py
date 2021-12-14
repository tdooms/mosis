from pypdevs.DEVS import CoupledDEVS

from models.junction import Junction
from tests.trolley_collector import TrolleyCollector
from tests.trolley_generator import TrolleyGenerator


class JunctionTest(CoupledDEVS):
    def __init__(self):
        super().__init__("JunctionTest")
        self.generator = self.addSubModel(TrolleyGenerator())
        self.collector = self.addSubModel(TrolleyCollector())
        self.junction = self.addSubModel(Junction(1))

        self.connectPorts(self.generator.output, self.junction.inputs[0])
        self.connectPorts(self.junction.output, self.collector.input)

