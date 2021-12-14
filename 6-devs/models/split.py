from dataclasses import dataclass, field

from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger


class Split(AtomicDEVS):
    def __init__(self, num_outputs: int, routing: list[int]):
        AtomicDEVS.__init__(self, "Split")

        self.input = self.addInPort("input")
        self.outputs = [self.addOutPort(f"output{i}") for i in range(num_outputs)]
        self.routing = routing

        self.trolley = None

    def extTransition(self, inputs):
        if self.input in inputs and self.trolley:
            self.trolley = inputs[self.input]
        return self.state

    def timeAdvance(self):
        return 0 if self.trolley else float("inf")

    def outputFnc(self):
        assert self.trolley
        result = {self.outputs[self.trolley.line]: self.trolley}

        self.trolley = None
        return result
