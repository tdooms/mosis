import copy
import random
from dataclasses import dataclass
from typing import Optional


def create_passenger(origin: str, lines: dict[str, list[str]], destinations: list[str], wrong_chance: float):
    assert 1 >= wrong_chance >= 0, "change must be between 0 and 1 inclusive"

    # It's important to notice that the destination is never the same as the origin
    available = copy.deepcopy(destinations)
    available.remove(origin)

    # Also notice that the 'real' destination cannot be the original one
    original = random.choice(available)
    available.remove(original)

    destination = original if len(available) == 0 or random.random() > wrong_chance else random.choice(available)
    return Passenger(origin=origin, destination=destination, original_dest=original, lines=lines)


@dataclass
class Passenger:
    origin: str
    destination: str
    original_dest: str
    lines: dict[str, list[str]]

    departed_at: Optional[float] = None
    arrived_at: Optional[float] = None


