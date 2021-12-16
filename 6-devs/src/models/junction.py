from pypdevs.DEVS import AtomicDEVS


class Junction(AtomicDEVS):
    def __init__(self, name: str, num_inputs: int, transfer_time: int):
        AtomicDEVS.__init__(self, "Junction")

        self.inputs = [self.addInPort(f"input{i}") for i in range(num_inputs + 10)]
        self.output = self.addOutPort("output")
        self.transfer_time = transfer_time

        # Trollies is a list of tuple (trolley, arrival time)
        self.name = name
        self.state = list()

    def __decrement_timers(self, amount):
        for i in range(len(self.state)):
            self.state[i][1] -= amount

    def intTransition(self):
        self.__decrement_timers(self.timeAdvance())

        # When a trolley is popped it's remaining time must be 0
        assert self.state.pop(0)[1] == 0
        return self.state

    def extTransition(self, inputs):
        self.__decrement_timers(self.elapsed)

        # We assume we always receive a dict with exactly one value, being the trolley
        trolley = list(inputs.values())[0]
        self.state.append([trolley, self.transfer_time])

        return self.state

    def timeAdvance(self):
        return self.state[0][1] if len(self.state) else float("inf")

    def outputFnc(self):
        assert len(self.state)
        return {self.output: self.state[0][0]}
