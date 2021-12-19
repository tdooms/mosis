import logging
from pypdevs.DEVS import AtomicDEVS

from models.passenger import Passenger


class Platform(AtomicDEVS):
    def __init__(self, origin: str):
        AtomicDEVS.__init__(self, "Platform")

        self.passenger_entry = self.addInPort("passenger_entry")
        self.request_passenger = self.addInPort("request_passenger")
        self.board = self.addOutPort("board")

        self.state = {"queue": list(), "requested": None, "time": 0}
        self.origin = origin

    def __passenger_indices(self, line):
        return [idx for idx, psgr in enumerate(self.state["queue"]) if self.origin in psgr.lines[line]]

    def intTransition(self):
        self.state["time"] += self.timeAdvance()

        candidates = self.__passenger_indices(self.state["requested"])
        self.state["requested"] = None
        self.state["queue"].pop(candidates[0])

        return self.state

    def extTransition(self, inputs):
        self.state["time"] += self.elapsed

        # Set the request variable in the state
        line = inputs[self.request_passenger] if self.request_passenger in inputs else None
        if line is not None and self.__passenger_indices(line):
            logging.debug("PLATFORM: received request with waiting passengers")
            self.state["requested"] = line

        # Add passenger to the queue
        elif self.passenger_entry in inputs:
            self.state["queue"].append(inputs[self.passenger_entry])

        return self.state

    def timeAdvance(self):
        return float("inf") if self.state["requested"] is None else 0

    def outputFnc(self):
        assert self.state["requested"] is not None
        candidates = self.__passenger_indices(self.state["requested"])
        assert len(candidates), "candidates list must not be empty, this must be checked beforehand"
        candidate = self.state["queue"][candidates[0]]
        candidate.departed_at = self.state["time"]
        logging.debug("PLATFORM: boarding passengers")
        return {self.board: candidate}
