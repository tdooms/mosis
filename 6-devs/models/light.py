from pypdevs.DEVS import AtomicDEVS



class Light(AtomicDEVS):
    def __init__(self):
        AtomicDEVS.__init__(self, "Light")

        self.request_trolley = self.addInPort("request_trolley")
        self.dequeue_trolley = self.addOutPort("dequeue_trolley")
        self.requested = False

    def intTransition(self):
        self.state.time += self.timeAdvance()
        return self.state

    def extTransition(self, inputs):
        if self.request_trolley in inputs and len(self.state.queue) > 0:
            self.requested = True
        return self.state

    def timeAdvance(self):
        return 0 if self.requested else float("inf")

    def outputFnc(self):
        assert len(self.state.queue)
        self.requested = False

        return {self.dequeue_trolley: self.state.queue.pop(0)}
