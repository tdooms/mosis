from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger


class TrolleyCollector(AtomicDEVS):
    def __init__(self):
        AtomicDEVS.__init__(self, "TrolleyCollector")

        self.input = self.addInPort("input")
        self.time = 0
        self.state = list()

    def extTransition(self, inputs):
        self.time += self.elapsed
        self.state.append((self.elapsed, inputs[self.input]))

        print(f"trolley {inputs[self.input]} arrived at {self.time:.2f}")
        return self.state

    def timeAdvance(self):
        return float("inf")
