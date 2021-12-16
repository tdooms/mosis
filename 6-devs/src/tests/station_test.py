from pypdevs.DEVS import CoupledDEVS

from classes import StationData
from models.rail import Rail
from models.station import Station
from models.trolley import Trolley
from tests.trolley_collector import TrolleyCollector
from tests.trolley_generator import TrolleyGenerator


class StationTest(CoupledDEVS):
    def __init__(self):
        super().__init__("StationTest")
        trollies = [Trolley(20, "main", [], 2), Trolley(100, "main", [], 2)]

        data = StationData(name="start", split={"main": 0})
        station = Station(data, destinations=["end"], lines={"main": ["start", "end"]})

        self.generator = self.addSubModel(TrolleyGenerator(mu=20, sigma=0, trollies=trollies))
        self.collector = self.addSubModel(TrolleyCollector())
        self.station = self.addSubModel(station)

        self.connectPorts(self.generator.output, self.station.input)
        self.connectPorts(self.station.outputs[0], self.collector.input)

