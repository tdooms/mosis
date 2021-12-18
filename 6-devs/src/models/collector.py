from dataclasses import dataclass

from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger


@dataclass
class CollectorStatistics:
    average_time: float
    amount_exited: float
    amount_exited_at_desired: float
    dest_eq_origin: float
    trolley_histories: dict[int, list[int]]


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

        # for p in self.state["passengers"]:
        #     if
        # tr_hist =

        return CollectorStatistics(avg_time, amt_exited, amt_desired, dest_eq, {})

        # print("For each station, the amount of people that have exited at that station.")
        # print(f"\tstation {self.origin}: people exited {len(self.state)}")

        # print("For each station, the amount of people that have exited at that station.")
        # print(f"\tstation {self.origin}: people exited at desired {desired}")

        # print("passengers arrived:", )
        # print("average arrival time:", sum([time for time, p in self.state]) / len(self.state))

        # print("Number of people with a destination that equals their origin station:")
        # print(f"\tstation {self.origin}: people exited at origin {equals}")
        #
        # return len(self.state), desired, equals
