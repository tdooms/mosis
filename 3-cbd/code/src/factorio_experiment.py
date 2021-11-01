#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   C:/Users/thoma/PycharmProjects/mosis/3-cbd/convert/__main__.py -e root -F CBD C:\Users\thoma\PycharmProjects\mosis\3-cbd\convert\factorio.drawio

from factorio import *
from CBD.simulator import Simulator


cbd = root("root")

# Run the Simulation
sim = Simulator(cbd)
print(sim.setVerbose())
sim.run(10)


# TODO: Process Your Simulation Results