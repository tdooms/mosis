from pypdevs.DEVS import CoupledDEVS

from models.junction import Junction
from models.trolley import Trolley
from tests.trolley_collector import TrolleyCollector
from tests.trolley_generator import TrolleyGenerator


class JunctionTest(CoupledDEVS):
    def __init__(self):
        super().__init__("JunctionTest")
        trollies = [Trolley(1, 0, []), Trolley(2, 0, []), Trolley(3, 0, []), Trolley(4, 0, [])]
        self.generator = self.addSubModel(TrolleyGenerator(sigma=0, mu=10, trollies=trollies))
        self.collector = self.addSubModel(TrolleyCollector())
        self.junction = self.addSubModel(Junction(1))

        self.connectPorts(self.generator.output, self.junction.inputs[0])
        self.connectPorts(self.junction.output, self.collector.input)

