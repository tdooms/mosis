from pypdevs.DEVS import AtomicDEVS


class Junction(AtomicDEVS):
    def __init__(self, num_inputs: int, transfer_time: int = 50):
        AtomicDEVS.__init__(self, "Junction")

        self.inputs = [self.addInPort(f"input{i}" for i in range(num_inputs))]
        self.output = self.addOutPort("output")
        self.transfer_time = transfer_time

        # Trollies is a list of tuple (trolley, arrival time)
        self.state = {"trollies": list(), "time": 0}

    def intTransition(self):
        if self.timeAdvance() != float("inf"):
            self.elapsed = self.timeAdvance()
        return self.state

    def extTransition(self, inputs):
        self.state["time"] += self.elapsed
        print(self.elapsed, self.state["time"])

        # We assume we always receive a dict with exactly one value, being the trolley
        trolley = list(inputs.values())[0]
        self.state["trollies"].append((trolley, self.state["time"] + 50))
        return self.state

    def timeAdvance(self):
        return self.state["trollies"][0][1] - self.state["time"] if len(self.state["trollies"]) else float("inf")

    def outputFnc(self):
        assert len(self.state["trollies"])
        return {self.output: self.state["trollies"].pop(0)[0]}
