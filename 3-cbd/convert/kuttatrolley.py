#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   /home/thomas/PycharmProjects/mosis/3-cbd/convert/__main__.py -F CBD -e root -sSrgv kuttatrolley.drawio

from CBD.Core import *
from CBD.lib.std import *


class LookupBlock(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(ConstantBlock("8vYfKD7r18sQojz9sVD8-4", value=(200)))
        self.addBlock(ConstantBlock("8vYfKD7r18sQojz9sVD8-6", value=(170)))
        self.addBlock(ConstantBlock("8vYfKD7r18sQojz9sVD8-8", value=(10)))
        self.addBlock(TimeBlock("8vYfKD7r18sQojz9sVD8-10"))
        self.addBlock(ConstantBlock("8vYfKD7r18sQojz9sVD8-12", value=(260)))
        self.addBlock(LessThanBlock("8vYfKD7r18sQojz9sVD8-14"))
        self.addBlock(LessThanBlock("8vYfKD7r18sQojz9sVD8-18"))
        self.addBlock(LessThanBlock("8vYfKD7r18sQojz9sVD8-22"))
        self.addBlock(LessThanBlock("8vYfKD7r18sQojz9sVD8-26"))
        self.addBlock(MultiplexerBlock("8vYfKD7r18sQojz9sVD8-34"))
        self.addBlock(MultiplexerBlock("8vYfKD7r18sQojz9sVD8-39"))
        self.addBlock(MultiplexerBlock("8vYfKD7r18sQojz9sVD8-44"))
        self.addBlock(MultiplexerBlock("8vYfKD7r18sQojz9sVD8-49"))
        self.addBlock(ConstantBlock("8vYfKD7r18sQojz9sVD8-58", value=(0)))
        self.addBlock(ConstantBlock("8vYfKD7r18sQojz9sVD8-60", value=(10)))
        self.addBlock(ConstantBlock("8vYfKD7r18sQojz9sVD8-64", value=(8)))
        self.addBlock(ConstantBlock("8vYfKD7r18sQojz9sVD8-67", value=(18)))
        self.addBlock(ConstantBlock("8vYfKD7r18sQojz9sVD8-70", value=(12)))

        # Create the Connections
        self.addConnection("8vYfKD7r18sQojz9sVD8-8", "8vYfKD7r18sQojz9sVD8-14", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-6", "8vYfKD7r18sQojz9sVD8-18", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-4", "8vYfKD7r18sQojz9sVD8-22", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-12", "8vYfKD7r18sQojz9sVD8-26", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-14", "8vYfKD7r18sQojz9sVD8-34", output_port_name='OUT1', input_port_name='select')
        self.addConnection("8vYfKD7r18sQojz9sVD8-18", "8vYfKD7r18sQojz9sVD8-39", output_port_name='OUT1', input_port_name='select')
        self.addConnection("8vYfKD7r18sQojz9sVD8-22", "8vYfKD7r18sQojz9sVD8-44", output_port_name='OUT1', input_port_name='select')
        self.addConnection("8vYfKD7r18sQojz9sVD8-26", "8vYfKD7r18sQojz9sVD8-49", output_port_name='OUT1', input_port_name='select')
        self.addConnection("8vYfKD7r18sQojz9sVD8-58", "8vYfKD7r18sQojz9sVD8-34", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-60", "8vYfKD7r18sQojz9sVD8-34", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-64", "8vYfKD7r18sQojz9sVD8-39", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-67", "8vYfKD7r18sQojz9sVD8-44", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-70", "8vYfKD7r18sQojz9sVD8-49", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-34", "8vYfKD7r18sQojz9sVD8-39", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-39", "8vYfKD7r18sQojz9sVD8-44", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-44", "8vYfKD7r18sQojz9sVD8-49", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-10", "8vYfKD7r18sQojz9sVD8-14", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-10", "8vYfKD7r18sQojz9sVD8-18", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-10", "8vYfKD7r18sQojz9sVD8-22", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-10", "8vYfKD7r18sQojz9sVD8-26", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-49", "OUT1", output_port_name='OUT1')


class PIDBlock(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=['IN2', 'IN1'], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(AdderBlock("8vYfKD7r18sQojz9sVD8-89"))
        self.addBlock(IntegratorBlock("8vYfKD7r18sQojz9sVD8-99"))
        self.addBlock(ProductBlock("8vYfKD7r18sQojz9sVD8-115"))
        self.addBlock(ProductBlock("8vYfKD7r18sQojz9sVD8-119"))
        self.addBlock(ConstantBlock("k", value=(329.38)))
        self.addBlock(ConstantBlock("ti", value=(66.35)))
        self.addBlock(ConstantBlock("8vYfKD7r18sQojz9sVD8-136", value=(0)))

        # Create the Connections
        self.addConnection("IN1", "8vYfKD7r18sQojz9sVD8-115", input_port_name='IN1')
        self.addConnection("IN1", "8vYfKD7r18sQojz9sVD8-99", input_port_name='IN1')
        self.addConnection("k", "8vYfKD7r18sQojz9sVD8-115", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-99", "8vYfKD7r18sQojz9sVD8-119", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("ti", "8vYfKD7r18sQojz9sVD8-119", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-119", "8vYfKD7r18sQojz9sVD8-89", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-89", "OUT1", output_port_name='OUT1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-136", "8vYfKD7r18sQojz9sVD8-99", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("IN2", "8vYfKD7r18sQojz9sVD8-99", input_port_name='delta_t')
        self.addConnection("8vYfKD7r18sQojz9sVD8-115", "8vYfKD7r18sQojz9sVD8-89", output_port_name='OUT1', input_port_name='IN1')


class PlantBlock(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=['IN2', 'IN1'], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(ConstantBlock("half", value=(0.5)))
        self.addBlock(ConstantBlock("p", value=(1.2)))
        self.addBlock(ConstantBlock("Cd", value=(0.6)))
        self.addBlock(ConstantBlock("A", value=(9.12)))
        self.addBlock(ProductBlock("8vYfKD7r18sQojz9sVD8-156"))
        self.addBlock(ProductBlock("8vYfKD7r18sQojz9sVD8-160"))
        self.addBlock(ProductBlock("8vYfKD7r18sQojz9sVD8-168"))
        self.addBlock(ProductBlock("8vYfKD7r18sQojz9sVD8-174"))
        self.addBlock(ProductBlock("8vYfKD7r18sQojz9sVD8-178"))
        self.addBlock(AdderBlock("8vYfKD7r18sQojz9sVD8-184"))
        self.addBlock(InverterBlock("8vYfKD7r18sQojz9sVD8-188"))
        self.addBlock(ConstantBlock("m_psgr", value=(77)))
        self.addBlock(ConstantBlock("m_trolley", value=(2376)))
        self.addBlock(AdderBlock("8vYfKD7r18sQojz9sVD8-195"))
        self.addBlock(ProductBlock("8vYfKD7r18sQojz9sVD8-202"))
        self.addBlock(IntegratorBlock("8vYfKD7r18sQojz9sVD8-208"))
        self.addBlock(ConstantBlock("8vYfKD7r18sQojz9sVD8-215", value=(0)))
        self.addBlock(NegatorBlock("8vYfKD7r18sQojz9sVD8-228"))

        # Create the Connections
        self.addConnection("IN1", "8vYfKD7r18sQojz9sVD8-184", input_port_name='IN2')
        self.addConnection("half", "8vYfKD7r18sQojz9sVD8-156", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("p", "8vYfKD7r18sQojz9sVD8-156", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("Cd", "8vYfKD7r18sQojz9sVD8-160", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("A", "8vYfKD7r18sQojz9sVD8-160", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-156", "8vYfKD7r18sQojz9sVD8-168", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-160", "8vYfKD7r18sQojz9sVD8-168", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-168", "8vYfKD7r18sQojz9sVD8-178", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-174", "8vYfKD7r18sQojz9sVD8-178", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("m_psgr", "8vYfKD7r18sQojz9sVD8-195", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("m_trolley", "8vYfKD7r18sQojz9sVD8-195", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-195", "8vYfKD7r18sQojz9sVD8-188", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-184", "8vYfKD7r18sQojz9sVD8-202", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-188", "8vYfKD7r18sQojz9sVD8-202", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-208", "OUT1", output_port_name='OUT1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-208", "8vYfKD7r18sQojz9sVD8-174", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-208", "8vYfKD7r18sQojz9sVD8-174", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("8vYfKD7r18sQojz9sVD8-215", "8vYfKD7r18sQojz9sVD8-208", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("IN2", "8vYfKD7r18sQojz9sVD8-208", input_port_name='delta_t')
        self.addConnection("8vYfKD7r18sQojz9sVD8-178", "8vYfKD7r18sQojz9sVD8-228", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-228", "8vYfKD7r18sQojz9sVD8-184", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("8vYfKD7r18sQojz9sVD8-202", "8vYfKD7r18sQojz9sVD8-208", output_port_name='OUT1', input_port_name='IN1')


class root(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=['delta_t'], output_ports=[])

        # Create the Blocks
        self.addBlock(LookupBlock("lookup"))
        self.addBlock(AdderBlock("sum"))
        self.addBlock(NegatorBlock("neg"))
        self.addBlock(PlantBlock("plant"))
        self.addBlock(PIDBlock("controller"))

        # Create the Connections
        self.addConnection("lookup", "sum", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("plant", "neg", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("controller", "plant", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("sum", "controller", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("delta_t", "controller", input_port_name='IN2')
        self.addConnection("delta_t", "plant", input_port_name='IN2')
        self.addConnection("neg", "sum", output_port_name='OUT1', input_port_name='IN1')


