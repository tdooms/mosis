from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger


class TrolleyCollector(AtomicDEVS):
    def __init__(self):
        AtomicDEVS.__init__(self, "TrolleyCollector")

        self.input = self.addInPort("input")
        self.state = {"trollies": list(), "time": 0}

    def extTransition(self, inputs):
        self.state["time"] += self.elapsed
        self.state["trollies"].append((self.elapsed, inputs[self.input]))

        # print(self.elapsed, self.state["time"])
        logging.debug(f"COLLECTOR: {inputs[self.input]} arrived at {self.state['time']:.2f}")

        return self.state

    def timeAdvance(self):
        return float("inf")
