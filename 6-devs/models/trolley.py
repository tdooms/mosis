from dataclasses import dataclass
from models.passenger import Passenger


@dataclass
class Trolley:
    velocity: int
    line: int
    passengers: [Passenger]
    capacity: int = 10
