from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger


class Collector(AtomicDEVS):
    def __init__(self, origin: int):
        AtomicDEVS.__init__(self, "Collector")

        self.depart = self.addInPort("depart")
        self.origin = origin
        self.time = 0
        self.state = list()

    def extTransition(self, inputs):
        self.time += self.elapsed
        self.state.append((self.elapsed, inputs[self.depart]))

        print(f"{self.origin}: passenger {inputs[self.depart]} arrived at {self.time:.2f}")
        return self.state

    def timeAdvance(self):
        return float("inf")

    def statistics(self) -> tuple[int, int, int]:
        desired = len([p for _, p in self.state if self.origin == p.destination])
        equals = len([p for _, p in self.state if p.origin == p.destination])

        # print("For each station, the amount of people that have exited at that station.")
        # print(f"\tstation {self.origin}: people exited {len(self.state)}")

        # print("For each station, the amount of people that have exited at that station.")
        # print(f"\tstation {self.origin}: people exited at desired {desired}")

        # print("passengers arrived:", )
        # print("average arrival time:", sum([time for time, p in self.state]) / len(self.state))

        # print("Number of people with a destination that equals their origin station:")
        # print(f"\tstation {self.origin}: people exited at origin {equals}")

        return len(self.state), desired, equals
