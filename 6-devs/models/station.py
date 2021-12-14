from pypdevs.DEVS import CoupledDEVS

from models.collector import Collector
from models.generator import Generator
from models.light import Light
from models.platform import Platform
from models.split import Split
from models.track import Track


class Station(CoupledDEVS):
    def __init__(self, station_id: int, destinations: list[int], routing: list[int], num_outputs: int):
        super().__init__("Station")

        self.generator = self.addSubModel(Generator(origin=station_id, destinations=destinations))
        self.collector = self.addSubModel(Collector(origin=station_id))
        self.light = self.addSubModel(Light())
        self.split = self.addSubModel(Split(routing=routing, num_outputs=num_outputs))
        self.track = self.addSubModel(Track(origin=station_id))
        self.platform = self.addSubModel(Platform(origin=station_id))

        self.connectPorts(self.generator.passenger_entry, self.platform.passenger_entry)
        self.connectPorts(self.track.request_passenger, self.platform.request_passenger)
        self.connectPorts(self.platform.board, self.track.board)
        self.connectPorts(self.light.dequeue_trolley, self.track.dequeue_trolley)
        self.connectPorts(self.track.request_trolley, self.light.request_trolley)
        self.connectPorts(self.track.depart, self.collector.depart)
        self.connectPorts(self.track.output, self.split.input)

