from dataclasses import dataclass, field
from models.passenger import Passenger



@dataclass
class Trolley:
    velocity: int
    line: str
    passengers: [Passenger]
    capacity: int
    history: list[int] = field(default_factory=list)

    def is_full(self):
        return len(self.passengers) == self.capacity
