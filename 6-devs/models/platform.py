from dataclasses import dataclass, field
from typing import Optional

from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger


@dataclass
class PlatformState:
    queue: list[Passenger] = field(default_factory=list)
    requested: Optional[int] = None
    time: int = 0


class Platform(AtomicDEVS):
    def __init__(self, origin: int):
        AtomicDEVS.__init__(self, "Platform")

        self.passenger_entry = self.addInPort("passenger_entry")
        self.request_passenger = self.addInPort("request_passenger")
        self.board = self.addOutPort("board")

        self.state = PlatformState()
        self.origin = origin

    def __requested_psgr_idx(self, line):
        return [idx for idx, psgr in enumerate(self.state.queue) if self.origin in psgr.lines[line]]

    def intTransition(self):
        self.state.time += self.timeAdvance()
        return self.state

    def extTransition(self, inputs):
        if self.request_passenger in inputs:
            line = inputs[self.request_passenger]
            if len(self.__requested_psgr_idx(line)) > 0:
                self.state.requested = line

        elif self.passenger_entry in inputs:
            self.state.queue.append(inputs[self.passenger_entry])

        return self.state

    def timeAdvance(self):
        return 0 if self.state.requested else float("inf")

    def outputFnc(self):
        self.state.requested = None
        candidates = self.__requested_psgr_idx(self.state.requested)
        assert len(candidates), "candidates list must not be empty, this must be checked beforehand"

        return {self.board: self.state.queue.pop(candidates[0])}
