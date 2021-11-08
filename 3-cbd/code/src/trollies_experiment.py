#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   /home/thomas/PycharmProjects/mosis/3-cbd/convert/__main__.py -F CBD -e root -sSrgv trollies.drawio

from trollies import *
from CBD.simulator import Simulator
import matplotlib.pyplot as plt

from CBD.preprocessing.butcher import ButcherTableau as BT
from CBD.preprocessing.rungekutta import RKPreprocessor

RUNGE_KUTTA = True
DELTA = 0.3


class Trollies(CBD):
    def __init__(self, name="Trollies"):
        CBD.__init__(self, name, input_ports=[], output_ports=[])

        # Create the blocks
        # Highest value that 'works' is 7.27825 after that it explodes
        # Range between [1; 5] is good
        # Smaller than 1 doesn't converges very slowly
        self.addBlock(ConstantBlock("delta_t", value=DELTA))
        self.addBlock(root("root"))

        # Connect the blocks
        self.addConnection("delta_t", "root", input_port_name="delta_t")


if RUNGE_KUTTA:
    tableau = BT.RKF45()
    RKP = RKPreprocessor(tableau, atol=2e-5, hmin=0.1, safety=.84)

    cbd = Trollies("Trollies")
    sim = RKP.preprocess(cbd)
    sim.run(300)
else:
    cbd = Trollies("Trollies")

    sim = Simulator(cbd)
    sim.setDeltaT(DELTA)
    sim.run(300)


root = cbd.getBlockByName("root")

lookup_signal = root.getBlockByName("lookup").getSignal('OUT1')
plant_signal = root.getBlockByName("plant").getSignal('OUT1')
controller_signal = root.getBlockByName("controller").getSignal('OUT1')

time = [x for x, _ in lookup_signal]

lookup_speed = [y for _, y in lookup_signal]
plant_speed = [y for _, y in plant_signal]
f_traction = [y for _, y in controller_signal]

plt.plot(time, lookup_speed)
plt.plot(time, plant_speed)

plt.xlabel('time (s)')
plt.ylabel('speed (m/s)')

plt.title('lookup vs plant speed')
plt.show()
