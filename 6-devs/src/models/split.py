from dataclasses import dataclass, field

from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger


class Split(AtomicDEVS):
    def __init__(self, routing: dict[str, int], outputs: int):
        """
        @routing:   dictionary of line to output
                    e.g. line 2 -> output 0, line 1 -> output 0, line 2 -> output 1
        """
        AtomicDEVS.__init__(self, "Split")

        self.input = self.addInPort("input")

        # The amount of outputs is the max number in the list
        self.outputs = [self.addOutPort(f"output{i}") for i in range(outputs)]
        self.routing = routing

        self.state = None

    def intTransition(self):
        self.state = None
        return self.state

    def extTransition(self, inputs):
        assert self.state is None
        self.state = list(inputs.values())[0]
        print("SPLIT: a trolley arrived on split")
        return self.state

    def timeAdvance(self):
        return float("inf") if self.state is None else 0

    def outputFnc(self):
        assert self.state is not None
        return {self.outputs[self.routing[self.state.line]]: self.state}
