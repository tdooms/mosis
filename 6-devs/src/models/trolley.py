from dataclasses import dataclass
from models.passenger import Passenger


@dataclass
class Trolley:
    velocity: int
    line: str
    passengers: [Passenger]
    capacity: int

    def is_full(self):
        return len(self.passengers) == self.capacity
