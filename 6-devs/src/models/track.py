from models.trolley import Trolley
from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger


class Track(AtomicDEVS):
    def __init__(self, origin: str, arriving_delay, unboarding_delay, boarding_delay, departing_delay):
        AtomicDEVS.__init__(self, "Track")

        # Set all the delays!
        self.waits = {
            "none": 1,  # Wait 1 second between each light poll
            "arriving": arriving_delay,
            "unboarding": unboarding_delay,
            "boarding": boarding_delay,
            "departing": departing_delay,
        }

        # connected to a Collector
        self.depart = self.addOutPort("depart")

        # connected to a Platform
        self.request_passenger = self.addOutPort("request_passenger")
        self.board = self.addInPort("board")

        # connected to a Light
        self.request_trolley = self.addOutPort("req")
        self.dequeue_trolley = self.addInPort("deq")

        # connected to an output Track/Split
        self.output = self.addOutPort("output")

        self.origin = origin

        # We try to mimic a Rust enum/variant, which is kind of a static dictionary
        # We will encode this as a simple, [String, value] list
        # "none": None,
        # "arriving": Trolley,
        # "unboarding": Trolley,
        # "boarding": Trolley,
        # "departing": Trolley
        self.state = ["none", None]

    def __passenger_indices(self):
        return [idx for idx, psgr in enumerate(self.state[1].passengers) if self.origin == psgr.destination]

    def intTransition(self):
        if self.state[0] == "arriving":
            print("TRACK: the trolley arrived, starting to unboard")
            self.state = ["unboarding", self.state[1]]
        elif self.state[0] == "unboarding" and len(self.__passenger_indices()) == 0:
            print(f"TRACK: unboarding is done: {len(self.state[1].passengers)} passengers left, starting boarding...")
            self.state = ["boarding", self.state[1]]
        elif self.state[0] == "unboarding":
            self.state[1].passengers.pop(self.__passenger_indices()[0])
        elif self.state[0] == "boarding" and self.state[1].is_full():
            print(f"TRACK: boarding is done: {len(self.state[1].passengers)} passengers are here, departing...")
            self.state = ["departing", self.state[1]]
        elif self.state[0] == "departing":  # also check if done instead of jumping though
            print("TRACK: trolley is gone")
            self.state = ["none", None]

        return self.state

    def extTransition(self, inputs):
        if self.board in inputs:
            print("TRACK: boarded passenger")
            assert self.state[0] == "boarding"
            assert len(self.state[1].passengers) <= self.state[1].capacity
            self.state[1].passengers.append(inputs[self.board])
        elif self.dequeue_trolley:
            print("TRACK: a trolley is arriving")
            assert self.state[0] == "none"
            self.state = ["arriving", inputs[self.dequeue_trolley]]

        return self.state

    def timeAdvance(self):
        return self.waits[self.state[0]]

    def outputFnc(self):
        if self.state[0] == "none":
            return {self.request_trolley: None}
        elif self.state[0] == "unboarding" and len(self.__passenger_indices()) > 0:
            print("TRACK: unboarding passenger, current passengers:", len(self.state[1].passengers))
            return {self.depart: self.__passenger_indices()[0]}
        elif self.state[0] == "boarding" and not self.state[1].is_full():
            print("TRACK: requesting passenger")
            return {self.request_passenger: self.state[1].line}
        return {}






