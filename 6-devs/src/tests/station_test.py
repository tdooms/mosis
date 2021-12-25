from pypdevs.DEVS import CoupledDEVS

from classes import StationData
from models.station import Station
from models.trolley import Trolley
from models.passenger import Passenger
from tests.trolley_collector import TrolleyCollector
from tests.trolley_generator import TrolleyGenerator


class StationTest(CoupledDEVS):
    def __init__(self):
        super().__init__("StationTest")
        trollies = [Trolley("one", 20, "not-main", [], 3), Trolley("two", 100, "main", [], 3)]

        data = StationData(name="start", split={"main": 0, "not-main": 0}, generator_mu=5, generator_sigma=0)
        lines = {"main": ["start", "end"], "not-main": ["start", "_end"]}
        station = Station(data, destinations=["end"], lines=lines)
        station.platform.state["queue"] = [Passenger("start", "_end", lines) for _ in range(2)]

        self.generator = self.addSubModel(TrolleyGenerator(mu=20, sigma=0, trollies=trollies))
        self.collector = self.addSubModel(TrolleyCollector())
        self.station = self.addSubModel(station)

        self.connectPorts(self.generator.output, self.station.input)
        self.connectPorts(self.station.outputs[0], self.collector.input)

