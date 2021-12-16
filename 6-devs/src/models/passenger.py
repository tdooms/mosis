from dataclasses import dataclass


@dataclass
class Passenger:
    origin: str
    destination: str
    lines: dict[str, list[str]]
