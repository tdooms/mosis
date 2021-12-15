from pypdevs.DEVS import AtomicDEVS


class Rail(AtomicDEVS):
    def __init__(self, length):
        AtomicDEVS.__init__(self, "Rail")

        self.input = self.addInPort("input")
        self.output = self.addOutPort("output")
        self.length = length
        self.state = {"trollies": list(), "time": 0, "temp": 0}

    def intTransition(self):
        self.state["temp"] = self.timeAdvance()
        return self.state

    def extTransition(self, inputs):
        self.state["time"] += self.elapsed
        trolley = inputs[self.input]
        nowait = self.state["time"] + self.length / trolley.velocity

        # The arrival time of the trolley is
        arrival = max(self.state["trollies"][-1][1] + 10, nowait) if len(self.state["trollies"]) else nowait
        print(f"trolley with velocity {trolley.velocity}:\t{nowait=}, {arrival=}")
        self.state["trollies"].append((trolley, arrival))
        return self.state

    def timeAdvance(self):
        # To determine how long we wait we take the arrival time minus the current time
        # print("yo", self.state["trollies"][0] if len(self.state["trollies"]) else None, self.state["time"])
        return self.state["trollies"][0][1] - self.state["time"] - self.state["temp"] if len(self.state["trollies"]) else float("inf")

    def outputFnc(self):
        assert len(self.state["trollies"])
        return {self.output: self.state["trollies"].pop(0)[0]}
