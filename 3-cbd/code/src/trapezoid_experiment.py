#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   /home/basil/gitProjects/mosis/3-cbd/convert/__main__.py -F CBD -e root -sSrgv trapezoid.drawio -E delta=0.1 -f

from BlockToLatex import block_to_latex
from trapezoid import *
from CBD.simulator import Simulator

DELTA_T = 0.1

cbd = root("root")

block_to_latex(cbd)

# Run the Simulation
sim = Simulator(cbd)
sim.setDeltaT(DELTA_T)
sim.run(10)
