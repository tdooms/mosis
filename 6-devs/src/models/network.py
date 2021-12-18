from pypdevs.DEVS import CoupledDEVS

from classes import NetworkData
from models.junction import Junction
from models.rail import Rail
from models.station import Station
from models.trolley import Trolley
from parse import parse_network
import graphviz


class Network(CoupledDEVS):
    def __init__(self, path: str):
        super().__init__("Network")
        data = parse_network(path)

        dests = [sdata.name for sdata in data.stations]
        lines = {l_data.name: l_data.stations for l_data in data.lines}

        self.trollies = {t_data.location: Trolley(t_data.velocity, t_data.line, [], t_data.capacity)
                         for t_data in data.trollies}

        self.stations = {s_data.name: self.addSubModel(Station(s_data, dests, lines, self.trollies.get(s_data.name)))
                         for s_data in data.stations}

        self.rails = [self.addSubModel(Rail(r_data.length, r_data.delay))
                      for r_data in data.rails]

        self.junctions = {j_data.name: self.addSubModel(Junction(j_data.name, j_data.inputs, j_data.transfer_time))
                          for j_data in data.junctions}

        self.data = data

        def __find_connection(name):
            if name in self.stations:
                return self.stations[name]
            elif name in self.junctions:
                return self.junctions[name]
            else:
                raise "error, no junction or station with given name"

        for i in range(len(self.rails)):
            start = __find_connection(data.rails[i].start)
            end = __find_connection(data.rails[i].end)

            s_port = start.output if data.rails[i].start_port is None else start.outputs[data.rails[i].start_port]
            e_port = end.input if data.rails[i].end_port is None else end.inputs[data.rails[i].end_port]

            self.connectPorts(s_port, self.rails[i].input)
            self.connectPorts(self.rails[i].output, e_port)

    def statistics(self) -> list:
        for name, station in self.stations.items():
            stats = station.statistics()
            print(stats)
        return []

    def visualise(self, path: str):
        dot = graphviz.Digraph(comment='Mosis City')
        for name, station in self.stations.items():
            dot.node(name)
        for name, junction in self.junctions.items():
            dot.node(name)
        for i in range(len(self.rails)):
            dot.edge(self.rails[i].IPorts[0].inline[0].host_DEVS.name,
                     self.rails[i].OPorts[0].outline[0].host_DEVS.name,
                     f"{self.data.rails[i].length}m")
        dot.render(format='svg', outfile=path)
