from dataclasses import dataclass


@dataclass
class Passenger:
    origin: str
    destination: str
    lines: dict[int, list[str]]
