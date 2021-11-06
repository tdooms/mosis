#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   /home/basil/gitProjects/mosis/3-cbd/convert/__main__.py -F CBD -e root -sSrgv trapezoid.drawio -E delta=0.1 -f

from CBD.Core import *
from CBD.lib.std import *

DELTA_T = 0.1

class root(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=['IN1', 'delta_t', 'IC'], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(ConstantBlock("y0", value=(0)))
        self.addBlock(AdderBlock("accumulator"))
        self.addBlock(DelayBlock("delay_state"))
        self.addBlock(DelayBlock("delay_input"))
        self.addBlock(AdderBlock("mid_adder"))
        self.addBlock(ProductBlock("mult"))
        self.addBlock(ConstantBlock("halver", value=(0.5)))
        self.addBlock(ProductBlock("delta_halver"))

        # Create the Connections
        self.addConnection("IN1", "delay_input", input_port_name='IN1')
        self.addConnection("IN1", "mid_adder", input_port_name='IN2')
        self.addConnection("accumulator", "OUT1", output_port_name='OUT1')
        self.addConnection("accumulator", "delay_state", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("y0", "delay_input", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("delay_input", "mid_adder", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("mid_adder", "mult", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("delay_state", "accumulator", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("mult", "accumulator", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("IC", "delay_state", input_port_name='IC')
        self.addConnection("delta_t", "delta_halver", input_port_name='IN1')
        self.addConnection("delta_halver", "mult", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("halver", "delta_halver", output_port_name='OUT1', input_port_name='IN2')


