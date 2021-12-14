from pypdevs.DEVS import AtomicDEVS


class Junction(AtomicDEVS):
    def __init__(self, num_inputs: int, transfer_time: int = 50):
        AtomicDEVS.__init__(self, "Junction")

        self.inputs = [self.addInPort(f"input{i}" for i in range(num_inputs))]
        self.output = self.addOutPort("output")
        self.time = 0
        self.transfer_time = transfer_time

        # Trollies is a list of tuple (trolley, arrival time)
        self.trollies = []

    def intTransition(self):
        self.time += self.timeAdvance()
        return self.trollies

    def extTransition(self, inputs):
        self.time += self.elapsed

        # We assume we always receive a dict with exactly one value, being the trolley
        trolley = list(inputs.values())[0]

        # The arrival time of the trolley is
        self.trollies.append((trolley, self.time + 50))
        return self.trollies

    def timeAdvance(self):
        # To determine how long we wait we take the arrival time minus the current time
        return self.trollies[0][1] - self.time if len(self.trollies) else float("inf")

    def outputFnc(self):
        assert len(self.trollies)
        return {self.output: self.trollies.pop(0)[0]}
