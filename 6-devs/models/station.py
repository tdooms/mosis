from pypdevs.DEVS import CoupledDEVS

from models.collector import Collector
from models.generator import Generator
from models.light import Light
from models.platform import Platform
from models.split import Split
from models.old_track import Track


class Station(CoupledDEVS):
    def __init__(self, name: str, split: dict[int, int],
                 destinations: list[str], lines: dict[int, list[str]]):
        """
        @routing:       dictionary of line to output
                        e.g. line 2 -> output 0, line 1 -> output 0, line 2 -> output 1
        @destinations:  list of all possible stations
                        e.g. ["central", "east", "west"]
        @lines:         dictionary of line number to ordered list of stations on that line
                        e.g. line 2 -> ["north", "west"], line 5 -> ["center", "east"]
        """
        super().__init__("Station")

        num_outputs = max(split.values()) + 1

        self.input = self.addInPort("input")
        self.outputs = [self.addOutPort(f"output{i}") for i in range(num_outputs)]

        self.generator = self.addSubModel(Generator(origin=name, destinations=destinations, lines=lines))
        self.collector = self.addSubModel(Collector(origin=name))
        self.light = self.addSubModel(Light())
        self.split = self.addSubModel(Split(routing=split, outputs=num_outputs))
        self.track = self.addSubModel(Track(origin=name))
        self.platform = self.addSubModel(Platform(origin=name))

        self.connectPorts(self.generator.passenger_entry, self.platform.passenger_entry)
        self.connectPorts(self.track.request_passenger, self.platform.request_passenger)
        self.connectPorts(self.platform.board, self.track.board)
        self.connectPorts(self.light.dequeue_trolley, self.track.dequeue_trolley)
        self.connectPorts(self.track.request_trolley, self.light.request_trolley)
        self.connectPorts(self.track.depart, self.collector.depart)
        self.connectPorts(self.track.output, self.split.input)
        self.connectPorts(self.input, self.light.input)

        for i in range(num_outputs):
            self.connectPorts(self.split.outputs[i], self.outputs[i])

