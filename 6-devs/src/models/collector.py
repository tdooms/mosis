from dataclasses import dataclass

from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger


@dataclass
class CollectorStatistics:
    average_time: float
    amount_exited: float
    amount_exited_at_desired: float
    dest_eq_origin: float


class Collector(AtomicDEVS):
    def __init__(self, origin: str):
        AtomicDEVS.__init__(self, "Collector")

        self.depart = self.addInPort("depart")
        self.origin = origin
        self.state = {"passengers": list(), "time": 0}

    def extTransition(self, inputs):
        self.state["time"] += self.elapsed
        passenger = inputs[self.depart]
        passenger.arrived_at = self.state["time"]
        self.state["passengers"].append(passenger)

        print(f"COLLECTOR: {inputs[self.depart]} arrived")
        return self.state

    def timeAdvance(self):
        return float("inf")

    def statistics(self) -> CollectorStatistics:
        avg_time = sum([p.arrived_at - p.departed_at for p in self.state["passengers"]]) / len(self.state["passengers"])
        amt_exited = len(self.state["passengers"])
        amt_desired = len([p for p in self.state["passengers"] if self.origin == p.destination])
        dest_eq = len([p for p in self.state["passengers"] if self.origin == p.origin])

        return CollectorStatistics(avg_time, amt_exited, amt_desired, dest_eq, {})

    def passengers(self):
        return self.state["passengers"]
