from pypdevs.DEVS import CoupledDEVS

from models.split import Split
from models.trolley import Trolley
from tests.trolley_collector import TrolleyCollector
from tests.trolley_generator import TrolleyGenerator


class SplitTest(CoupledDEVS):
    def __init__(self):
        super().__init__("JunctionTest")
        trollies = [Trolley("one", 20, "line-one", [], 10), Trolley("two", 20, "line-two", [], 10)]
        self.generator = self.addSubModel(
            TrolleyGenerator(sigma=0, mu=10, trollies=trollies))
        self.collector_one = self.addSubModel(TrolleyCollector())
        self.collector_two = self.addSubModel(TrolleyCollector())
        self.split = self.addSubModel(Split({"line-one": 0, "line-two": 1}, 2))

        self.connectPorts(self.generator.output, self.split.input)
        self.connectPorts(self.split.outputs[0], self.collector_one.input)
        self.connectPorts(self.split.outputs[1], self.collector_two.input)
