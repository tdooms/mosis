import random, logging
from typing import Optional

from models.trolley import Trolley
from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger


class Track(AtomicDEVS):
    def __init__(self, origin: str, trolley: Optional[Trolley], arriving_delay: float, unboarding_delay: float,
                 boarding_delay: float, departing_delay: float, random_unboard: float):
        AtomicDEVS.__init__(self, "Track")

        # Set all the delays!
        self.waits = {
            "none": 10,  # Wait 10 second between each light poll
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
        self.random_unboard = random_unboard

        # We try to mimic a Rust enum/variant, which is kind of a static dictionary
        # We will encode this as a simple, [String, value] list
        # "none": None,
        # "arriving": Trolley,
        # "unboarding": Trolley,
        # "boarding": Trolley,
        # "departing": Trolley
        self.state = ["none", None] if trolley is None else ["boarding", trolley]

    def __passenger_indices(self):
        return [idx for idx, psgr in enumerate(self.state[1].passengers)
                if self.origin == psgr.destination or random.random() < self.random_unboard]

    def intTransition(self):
        if self.state[0] == "arriving":
            logging.debug("TRACK: the trolley arrived, starting to unboard")
            self.state = ["unboarding", self.state[1], self.__passenger_indices(), 0]
        elif self.state[0] == "unboarding" and len(self.state[2]) == self.state[3]:
            logging.debug(f"TRACK: unboarding is done: {len(self.state[1].passengers)} passengers left, starting boarding...")
            self.state[1].passengers = [p for idx, p in enumerate(self.state[1].passengers) if idx in self.state[2]]
            self.state = ["boarding", self.state[1]]
        elif self.state[0] == "unboarding":
            self.state[3] += 1
        elif self.state[0] == "boarding" and self.state[1].is_full():
            logging.debug(f"TRACK: boarding is done: {len(self.state[1].passengers)} passengers are here, departing...")
            self.state = ["departing", self.state[1]]
        elif self.state[0] == "departing":  # also check if done instead of jumping though
            logging.debug("TRACK: trolley is gone")
            self.state = ["none", None]

        return self.state

    def extTransition(self, inputs):
        if self.board in inputs and inputs[self.board] is None:
            logging.debug("TRACK: departing due to a lack of waiting passengers")
            self.state[0] = "departing"

        elif self.board in inputs:
            logging.debug("TRACK: boarded passenger")
            assert self.state[0] == "boarding"
            assert len(self.state[1].passengers) <= self.state[1].capacity
            passenger = inputs[self.board]
            passenger.used_trolley = self.state[1].name
            self.state[1].passengers.append(passenger)

        elif self.dequeue_trolley:
            logging.debug("TRACK: a trolley is arriving")
            assert self.state[0] == "none"
            self.state = ["arriving", inputs[self.dequeue_trolley]]

        return self.state

    def timeAdvance(self):
        return self.waits[self.state[0]]

    def outputFnc(self):
        if self.state[0] == "none":
            return {self.request_trolley: None}
        elif self.state[0] == "unboarding" and len(self.state[2]) > self.state[3]:
            logging.debug("TRACK: unboarding passenger")
            return {self.depart: self.state[1].passengers[self.state[2][self.state[3]]]}
        elif self.state[0] == "boarding" and not self.state[1].is_full():
            logging.debug("TRACK: requesting passenger")
            return {self.request_passenger: self.state[1].line}
        elif self.state[0] == "departing":
            logging.debug("TRACK: trolley leaving track")
            return {self.output: self.state[1]}
        return {}
