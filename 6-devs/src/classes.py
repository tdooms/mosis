from dataclasses import dataclass


@dataclass
class StationData:
    name: str
    split: dict[int, int]
    arriving_delay: float = 30
    unboarding_delay: float = 10
    boarding_delay: float = 10
    departing_delay: float = 30


@dataclass
class JunctionData:
    name: str


@dataclass
class RailData:
    length: float
    start: str
    end: str


@dataclass
class LineData:
    id: int
    stations: list[str]


@dataclass
class TrolleyData:
    speed: float
    capacity: int


@dataclass
class SystemData:
    stations: list[StationData]
    junctions: list[JunctionData]
    rails: list[RailData]
    lines: list[LineData]
    trollies: list[TrolleyData]

