from pypdevs.DEVS import CoupledDEVS

from models.junction import Junction
from models.trolley import Trolley
from tests.trolley_collector import TrolleyCollector
from tests.trolley_generator import TrolleyGenerator


class JunctionTest(CoupledDEVS):
    def __init__(self):
        super().__init__("JunctionTest")
        trollies_one = [Trolley("one", 20, "line-one", [], 10)]
        trollies_two = [Trolley("two", 20, "line-two", [], 10)]
        self.generator_one = self.addSubModel(
            TrolleyGenerator(sigma=0, mu=10, trollies=trollies_one))
        self.generator_two = self.addSubModel(
            TrolleyGenerator(sigma=0, mu=9, trollies=trollies_two))
        self.collector = self.addSubModel(TrolleyCollector())
        self.junction = self.addSubModel(Junction("main_junction", 2, 20))

        self.connectPorts(self.generator_one.output, self.junction.inputs[0])
        self.connectPorts(self.generator_two.output, self.junction.inputs[1])
        self.connectPorts(self.junction.output, self.collector.input)
