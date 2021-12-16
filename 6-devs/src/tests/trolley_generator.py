import random

from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger
from models.trolley import Trolley


class TrolleyGenerator(AtomicDEVS):
    def __init__(self, mu=5, sigma=1, trollies=None):
        AtomicDEVS.__init__(self, "TrolleyGenerator")

        trollies = trollies if trollies else [Trolley(50, 0, [], 2)]

        self.output = self.addOutPort("output")
        self.mu = mu
        self.sigma = sigma
        self.trollies = trollies
        self.state = {"remaining": self.__distribution(), "time": 0, "cycle": 0}

    def __distribution(self):
        return random.normalvariate(self.mu, self.sigma)

    def intTransition(self):
        # print(f"GENERATOR: generated at {self.state['time']}")
        self.state["time"] += self.timeAdvance()
        self.state["remaining"] = self.__distribution()
        self.state["cycle"] = (self.state["cycle"] + 1) % len(self.trollies)
        return self.state

    def timeAdvance(self):
        return self.state["remaining"]

    def outputFnc(self):
        return {self.output: self.trollies[self.state["cycle"]]}
