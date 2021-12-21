import random

from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger


class Generator(AtomicDEVS):
    def __init__(self, origin: str, destinations: list[str], lines: dict[str, list[str]], mu, sigma):
        """
        @lines:         dictionary of line number to ordered list of stations on that line
                        e.g. line 2 -> [station 0, 4, 5], line 5 -> [station 2, 3, 0]
        @destinations:  list of all possible station numbers
                        e.g. [0, 1, 2, 3, ..., 42]
        """
        AtomicDEVS.__init__(self, "Generator")

        self.passenger_entry = self.addOutPort("passenger_entry")
        self.origin = origin
        self.destinations = destinations
        self.mu = mu
        self.sigma = sigma
        self.lines = lines
        self.state = {"remaining": self.__distribution(), "count": 0}

    def __distribution(self):
        return random.normalvariate(self.mu, self.sigma)

    def intTransition(self):
        self.state["count"] += 1
        self.state["remaining"] = self.__distribution()
        return self.state

    def timeAdvance(self):
        return self.state["remaining"]

    def outputFnc(self):
        passenger = Passenger(self.origin, random.choice(self.destinations), self.lines)
        return {self.passenger_entry: passenger}

    def statistics(self):
        return self.state["count"]

