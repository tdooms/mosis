# Our network file format is in JSON form to keep it simple, human-readable and easy to parse
#
# {
#   "stations": [
#       "name": str,
#       "split": {str: int},
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
#       "name": str,
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

    stations = [StationData(**s_data) for s_data in data["stations"]]
    junctions = [JunctionData(**j_data) for j_data in data["junctions"]]
    rails = [RailData(**r_data) for r_data in data["rails"]]
    lines = [LineData(**l_data) for l_data in data["lines"]]
    trollies = [TrolleyData(**t_data) for t_data in data["trollies"]]

    return NetworkData(stations=stations, junctions=junctions, rails=rails, lines=lines, trollies=trollies)








