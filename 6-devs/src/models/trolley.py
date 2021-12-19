from dataclasses import dataclass, field
from models.passenger import Passenger


@dataclass
class Trolley:
    name: str
    velocity: int
    line: str
    passengers: [Passenger]
    capacity: int

    def is_full(self):
        return len(self.passengers) == self.capacity
