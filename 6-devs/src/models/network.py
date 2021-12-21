import math

import graphviz
from pypdevs.DEVS import CoupledDEVS

from models.junction import Junction
from models.rail import Rail
from models.station import Station
from models.trolley import Trolley
from parse import parse_network


class Network(CoupledDEVS):
    def __init__(self, path: str, sim_length: int, small_buckets: int, summary_buckets: int):
        super().__init__("Network")
        data = parse_network(path)

        destinations = [sdata.name for sdata in data.stations]
        lines = {l_data.name: l_data.stations for l_data in data.lines}

        reachables = {x: [] for x in destinations}
        if data.meta.only_reachable:
            # we iterate over the lines and for each station in the line we add the whole line as reachable
            for line in lines.values():
                for station in line:
                    reachables[station] = list(set(reachables[station]).union(line))
            # We remove the station itself from the destinations as stated in the assignment
            for name in destinations:
                reachables[name].sort()
                reachables[name].remove(name)
        else:
            for name in destinations:
                reachables[name] = destinations

        self.trollies = {t_data.location: Trolley(t_data.name, t_data.velocity, t_data.line, [], t_data.capacity)
                         for t_data in data.trollies}

        self.stations = {s_data.name:
                             self.addSubModel(Station(s_data, reachables[s_data.name],
                                                      lines, self.trollies.get(s_data.name)))
                         for s_data in data.stations}

        self.rails = [self.addSubModel(Rail(r_data.length, r_data.delay))
                      for r_data in data.rails]

        self.junctions = {j_data.name: self.addSubModel(Junction(j_data.name, j_data.inputs, j_data.transfer_time))
                          for j_data in data.junctions}

        self.data = data

        self.sim_length = sim_length
        self.small_buckets = small_buckets
        self.summary_buckets = summary_buckets

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
        all_stats = {name: station.statistics() for name, station in self.stations.items()}

        station_arrived = {name: stat.collector.amount_exited for name, stat in all_stats.items()}
        station_avg = {name: stat.collector.average_time for name, stat in all_stats.items()}
        station_weighted_avg = {n: s.collector.average_time * s.collector.amount_exited for n, s in all_stats.items()}
        station_desired = {name: stat.collector.amount_exited_at_desired for name, stat in all_stats.items()}
        station_eq = {name: stat.collector.dest_eq_origin for name, stat in all_stats.items()}

        all_arrived = sum(station_arrived.values())
        all_avg = sum(station_weighted_avg.values()) / all_arrived if all_arrived else 0
        all_desired = sum(station_desired.values())
        all_eq = sum(station_eq.values())

        all_generated = sum([s.generator for s in all_stats.values()])
        all_still_travelling = all_generated - all_arrived

        all_psgrs = [psgr for station in self.stations.values() for psgr in station.passengers()]
        all_trollies = {psgr.used_trolley for psgr in all_psgrs}

        small_hists = {trolley: [0] * self.small_buckets for trolley in all_trollies}
        summary_hists = {trolley: [0] * self.summary_buckets for trolley in all_trollies}

        small_bs = self.sim_length / self.small_buckets
        relative_bs = self.small_buckets / self.summary_buckets

        for psgr in all_psgrs:
            for i in range(int(psgr.departed_at // small_bs), int(psgr.arrived_at // small_bs)):
                small_hists[psgr.used_trolley][i] += 1

        for tr_id, hist in small_hists.items():
            for i in range(len(hist)):
                summary_hists[tr_id][math.floor(i / relative_bs)] += (hist[i] / relative_bs)

        trolley_avg = {name: sum(hist) / self.small_buckets for name, hist in small_hists.items()}

        return [all_avg, summary_hists, trolley_avg, station_arrived, station_desired, station_avg, all_arrived,
                all_desired, all_still_travelling, all_eq]

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
