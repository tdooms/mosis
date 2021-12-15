from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from models.trolley import Trolley
from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger


class TrackAction(Enum):
    NONE = 0,
    ARRIVING = 1,
    UNLOADING = 2,
    BOARDING = 3,
    DEPARTING = 4


@dataclass
class TrackState:
    action: TrackAction
    time: float = 0

    trolley: Optional[Trolley] = None


class Track(AtomicDEVS):
    def __init__(self, origin: str):
        AtomicDEVS.__init__(self, "Platform")

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

        self.state = TrackState(action=TrackAction.NONE)
        self.origin = origin

    def intTransition(self):
        self.state.time += self.timeAdvance()

        # If there is no trolley we do nothing, this is handled in ext transition
        if self.state.action == TrackAction.NONE:
            pass
        # After 30 sec we
        elif self.state.action == TrackAction.ARRIVING:
            self.state.action = TrackAction.UNLOADING

        elif self.state.action == TrackAction.DEPARTING:
            self.state.action = TrackAction.NONE

        elif self.state.action == TrackAction.UNLOADING:
            # If unboarders is empty we go to boarding
            # unboarders = [idx for idx, p in enumerate(self.state.trolley.passengers) if p.destination == self.origin]
            pass
        elif self.state.action == TrackAction.BOARDING:
            if len(self.state.trolley.passengers) == self.state.trolley.capacity:
                self.state.action = TrackAction.DEPARTING

        return self.state

    def extTransition(self, inputs):
        return self.state

    def timeAdvance(self):
        # TODO: no more hardcode please
        waits = {
            TrackAction.NONE: 1,       # Wait 1  second  between polling the light
            TrackAction.ARRIVING: 30,  # wait 30 seconds on arrival and departure
            TrackAction.BOARDING: 10,  # Wait 10 seconds between board and un-board action
            TrackAction.UNLOADING: 10,
            TrackAction.DEPARTING: 30,
        }
        return waits[self.state.action]

    def outputFnc(self):
        if self.state.action == TrackAction.NONE:
            return {self.request_trolley: None}

        elif self.state.action == TrackAction.UNLOADING:
            if len(self.state.trolley.passengers) > 0:
                return {self.depart: self.state.trolley.passengers.pop(0)}

        elif self.state.action == TrackAction.BOARDING:
            if len(self.state.trolley.passengers) < self.state.trolley.capacity:
                return {self.request_passenger: self.state.trolley.line}




