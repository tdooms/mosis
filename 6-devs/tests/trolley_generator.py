import random

from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger
from models.trolley import Trolley


class TrolleyGenerator(AtomicDEVS):
    def __init__(self, origin: int, destinations: list[int], mu=5, sigma=1):
        AtomicDEVS.__init__(self, "TrolleyGenerator")

        self.passenger_entry = self.addOutPort("output")
        self.origin = origin
        self.destinations = destinations
        self.mu = mu
        self.sigma = sigma
        self.state = self.__distribution()
        self.time = 0

    def __distribution(self):
        return random.normalvariate(self.mu, self.sigma)

    def intTransition(self):
        self.time += self.timeAdvance()
        self.state = self.__distribution()
        # print(f"{self.origin}: current time: {self.time:.2f} new passenger in: {self.state:.2f}")

        return self.state

    def timeAdvance(self):
        return self.state

    def outputFnc(self):
        return {self.passenger_entry: Trolley(50, 0, [])}
