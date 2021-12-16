from dataclasses import dataclass
from typing import Optional


@dataclass
class StationData:
    name: str
    split: dict[str, int]
    arriving_delay: float = 30
    unboarding_delay: float = 10
    boarding_delay: float = 10
    departing_delay: float = 30
    generator_mu: float = 5
    generator_sigma: float = 1
    wrong_chance: float = 0.2


@dataclass
class JunctionData:
    name: str
    inputs: int
    transfer_time: float = 50


@dataclass
class RailData:
    start: str
    end: str

    length: float
    delay: float = 10

    start_port: Optional[int] = None
    end_port: Optional[int] = None


@dataclass
class LineData:
    name: str
    stations: list[str]


@dataclass
class TrolleyData:
    velocity: float
    line: str
    location: str
    capacity: int = 10


@dataclass
class NetworkData:
    stations: list[StationData]
    junctions: list[JunctionData]
    rails: list[RailData]
    lines: list[LineData]
    trollies: list[TrolleyData]

