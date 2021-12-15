# Our network file format is in JSON form to keep it simple, human-readable and easy to parse
#
# {
#   "stations": [
#       "name": str,
#       "split": {int (line): int (output)},
#       "arriving_delay": Optional[float]
#       "unboarding_delay": Optional[float]
#       "boarding_delay": Optional[float]
#       "departing_delay": Optional[float]
#   ],
#   "junctions": [
#       "name": str
#   ],
#   "rails": [
#       "length": float,
#       "start": str,
#       "end": str
#   ],
#   "lines": [
#       "id": int,
#       "stations": [str]
#   ],
#   "trollies": [
#       "speed": float,
#       "capacity": int,
#   ]
# }


import json
from classes import *


def parse_network(path):
    data = json.load(open(path))

    stations = [StationData(**sdata) for sdata in data["stations"]]
    junctions = [JunctionData(**sdata) for sdata in data["junctions"]]
    rails = [RailData(**sdata) for sdata in data["rails"]]
    lines = [LineData(**sdata) for sdata in data["lines"]]
    trollies = [TrolleyData(**sdata) for sdata in data["trollies"]]

    return SystemData(stations=stations, junctions=junctions, rails=rails, lines=lines, trollies=trollies)








