#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   /home/basil/gitProjects/mosis/3-cbd/convert/__main__.py -F CBD -e root -sSrgv forward.drawio -E delta=0.1 -f

from CBD.Core import *
from CBD.lib.std import *

DELTA_T = 0.1

class root(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=['delta_t', 'IC', 'IN1'], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(DelayBlock("delay"))
        self.addBlock(ProductBlock("multiply"))
        self.addBlock(AdderBlock("accum"))

        # Create the Connections
        self.addConnection("IN1", "multiply", input_port_name='IN2')
        self.addConnection("delay", "accum", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("multiply", "accum", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("accum", "delay", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("accum", "OUT1", output_port_name='OUT1')
        self.addConnection("IC", "delay", input_port_name='IC')
        self.addConnection("delta_t", "multiply", input_port_name='IN1')


