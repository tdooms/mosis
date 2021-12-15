from pypdevs.DEVS import AtomicDEVS


class Rail(AtomicDEVS):
    def __init__(self, length: int, delay: int = 10):
        AtomicDEVS.__init__(self, "Rail")

        self.input = self.addInPort("input")
        self.output = self.addOutPort("output")
        self.length = length
        self.delay = delay
        self.state = list()

    def __decrement_timers(self, amount):
        for i in range(len(self.state)):
            self.state[i][1] -= amount

    def intTransition(self):
        self.__decrement_timers(self.timeAdvance())

        assert self.state.pop(0)[1] == 0
        return self.state

    def extTransition(self, inputs):
        # It's important to decrement before inserting
        self.__decrement_timers(self.elapsed)

        trolley = inputs[self.input]
        nowait = self.length / trolley.velocity
        arrival = max(self.state[-1][1] + self.delay, nowait) if len(self.state) else nowait
        self.state.append([trolley, arrival])

        return self.state

    def timeAdvance(self):
        return self.state[0][1] if len(self.state) else float("inf")

    def outputFnc(self):
        assert len(self.state)
        return {self.output: self.state[0][0]}
