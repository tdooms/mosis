from pypdevs.DEVS import AtomicDEVS


class Light(AtomicDEVS):
    def __init__(self):
        AtomicDEVS.__init__(self, "Light")

        self.request_trolley = self.addInPort("request_trolley")
        self.dequeue_trolley = self.addOutPort("dequeue_trolley")
        self.input = self.addInPort("input")
        self.state = {"queue": list(), "requested": False}

    def intTransition(self):
        self.state["requested"] = False
        self.state["queue"].pop(0)
        return self.state

    def extTransition(self, inputs):
        # Set requested flag if well... requested
        self.state["requested"] = self.request_trolley in inputs and len(self.state["queue"]) > 0

        # Add a new trolley to the queue
        if self.input in inputs:
            self.state["queue"].append(inputs[self.input])

        return self.state

    def timeAdvance(self):
        return 0 if self.state["requested"] else float("inf")

    def outputFnc(self):
        assert len(self.state["queue"])
        return {self.dequeue_trolley: self.state["queue"][0]}
