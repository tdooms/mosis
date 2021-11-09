#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   /home/thomas/PycharmProjects/mosis/3-cbd/convert/__main__.py -F CBD -e root -sSrgv kuttatrolley.drawio

from kuttatrolley import *
from CBD.simulator import Simulator


cbd = root("root")

# Run the Simulation
sim = Simulator(cbd)
sim.run(10)

# TODO: Process Your Simulation Results