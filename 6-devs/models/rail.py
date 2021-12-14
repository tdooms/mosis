from pypdevs.DEVS import AtomicDEVS


class Rail(AtomicDEVS):
    def __init__(self, length):
        AtomicDEVS.__init__(self, "Rail")

        self.input = self.addInPort("input")
        self.output = self.addOutPort("output")
        self.length = length
        self.time = 0

        # Trollies is a list of tuple (trolley, arrival time)
        self.trollies = []

    def intTransition(self):
        self.state.time += self.timeAdvance()
        return self.state

    def extTransition(self, inputs):
        self.time += self.elapsed
        trolley = inputs[self.input]
        nowait = self.time + self.length / trolley.velocity

        # The arrival time of the trolley is
        arrival = max(self.trollies[-1][1] + 10, nowait) if len(self.trollies) else nowait
        self.trollies.append((trolley, arrival))
        return self.state

    def timeAdvance(self):
        # To determine how long we wait we take the arrival time minus the current time
        return self.trollies[0][1] - self.time if len(self.trollies) else float("inf")

    def outputFnc(self):
        assert len(self.state.queue)
        return {self.output: self.state.queue.pop(0)[0]}
