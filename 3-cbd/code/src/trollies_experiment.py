#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   /home/thomas/PycharmProjects/mosis/3-cbd/convert/__main__.py -F CBD -e root -sSrgv trollies.drawio

from trollies import *
from CBD.simulator import Simulator
import matplotlib.pyplot as plt


cbd = root("root")

sim = Simulator(cbd)
sim.run(300)

lookup_signal = cbd.getBlockByName("lookup").getSignal('OUT1')
plant_signal = cbd.getBlockByName("plant").getSignal('OUT1')
controller_signal = cbd.getBlockByName("controller").getSignal('OUT1')

time = [x for x, _ in lookup_signal]

lookup_speed = [y for _, y in lookup_signal]
plant_speed = [y for _, y in plant_signal]
f_traction = [y for _, y in controller_signal]

print(f_traction)

plt.plot(time, lookup_speed)
plt.plot(time, plant_speed)

plt.xlabel('time (s)')
plt.ylabel('speed (m/s)')


plt.title('lookup vs plant speed')
plt.show()
