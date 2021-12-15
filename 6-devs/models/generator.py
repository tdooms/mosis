import random

from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger


class Generator(AtomicDEVS):
    def __init__(self, origin: str, destinations: list[str], lines: dict[int, list[str]], mu=5, sigma=1):
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
        self.state = self.__distribution()

    def __distribution(self):
        return random.normalvariate(self.mu, self.sigma)

    def intTransition(self):
        self.state = self.__distribution()
        return self.state

    def timeAdvance(self):
        return self.state

    def outputFnc(self):
        passenger = Passenger(origin=self.origin, destination=random.choice(self.destinations), lines=self.lines)
        return {self.passenger_entry: passenger}
