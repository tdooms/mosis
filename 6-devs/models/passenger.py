from dataclasses import dataclass


@dataclass
class Passenger:
    origin: int
    destination: int
    lines: list[list[int]]
