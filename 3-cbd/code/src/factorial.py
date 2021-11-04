#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   C:/Users/thoma/PycharmProjects/mosis/3-cbd/convert/__main__.py -e root -F CBD C:\Users\thoma\PycharmProjects\mosis\3-cbd\convert\factorio.drawio

from CBD.Core import *
from CBD.lib.std import *


class root(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=['n!'])

        # Create the Blocks
        self.addBlock(ProductBlock("product"))
        self.addBlock(DelayBlock("delay"))
        self.addBlock(ConstantBlock("one", value=(1)))
        self.addBlock(AddOneBlock("plusone"))
        self.addBlock(DelayBlock("delayFac"))

        # Create the Connections
        self.addConnection("delay", "product", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("delay", "plusone", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("one", "delay", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("one", "delayFac", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("plusone", "delay", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("product", "delayFac", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("product", "n!", output_port_name='OUT1')
        self.addConnection("delayFac", "product", output_port_name='OUT1', input_port_name='IN2')


