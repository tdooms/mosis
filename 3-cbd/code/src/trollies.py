#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   /home/thomas/PycharmProjects/mosis/3-cbd/convert/__main__.py -F CBD -e root -sSrgv trollies.drawio

from CBD.Core import *
from CBD.lib.std import *


class LookupBlock(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(ConstantBlock("pTehlZL50KRKIpqK_xpU-127", value=(200)))
        self.addBlock(ConstantBlock("pTehlZL50KRKIpqK_xpU-129", value=(170)))
        self.addBlock(ConstantBlock("pTehlZL50KRKIpqK_xpU-131", value=(10)))
        self.addBlock(TimeBlock("pTehlZL50KRKIpqK_xpU-133"))
        self.addBlock(ConstantBlock("pTehlZL50KRKIpqK_xpU-135", value=(260)))
        self.addBlock(LessThanBlock("pTehlZL50KRKIpqK_xpU-137"))
        self.addBlock(LessThanBlock("pTehlZL50KRKIpqK_xpU-141"))
        self.addBlock(LessThanBlock("pTehlZL50KRKIpqK_xpU-145"))
        self.addBlock(LessThanBlock("pTehlZL50KRKIpqK_xpU-149"))
        self.addBlock(MultiplexerBlock("pTehlZL50KRKIpqK_xpU-157"))
        self.addBlock(MultiplexerBlock("pTehlZL50KRKIpqK_xpU-162"))
        self.addBlock(MultiplexerBlock("pTehlZL50KRKIpqK_xpU-167"))
        self.addBlock(MultiplexerBlock("pTehlZL50KRKIpqK_xpU-172"))
        self.addBlock(ConstantBlock("pTehlZL50KRKIpqK_xpU-181", value=(0)))
        self.addBlock(ConstantBlock("pTehlZL50KRKIpqK_xpU-183", value=(10)))
        self.addBlock(ConstantBlock("pTehlZL50KRKIpqK_xpU-187", value=(8)))
        self.addBlock(ConstantBlock("pTehlZL50KRKIpqK_xpU-190", value=(18)))
        self.addBlock(ConstantBlock("pTehlZL50KRKIpqK_xpU-193", value=(12)))

        # Create the Connections
        self.addConnection("pTehlZL50KRKIpqK_xpU-131", "pTehlZL50KRKIpqK_xpU-137", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("pTehlZL50KRKIpqK_xpU-129", "pTehlZL50KRKIpqK_xpU-141", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("pTehlZL50KRKIpqK_xpU-127", "pTehlZL50KRKIpqK_xpU-145", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("pTehlZL50KRKIpqK_xpU-135", "pTehlZL50KRKIpqK_xpU-149", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("pTehlZL50KRKIpqK_xpU-137", "pTehlZL50KRKIpqK_xpU-157", output_port_name='OUT1', input_port_name='select')
        self.addConnection("pTehlZL50KRKIpqK_xpU-141", "pTehlZL50KRKIpqK_xpU-162", output_port_name='OUT1', input_port_name='select')
        self.addConnection("pTehlZL50KRKIpqK_xpU-145", "pTehlZL50KRKIpqK_xpU-167", output_port_name='OUT1', input_port_name='select')
        self.addConnection("pTehlZL50KRKIpqK_xpU-149", "pTehlZL50KRKIpqK_xpU-172", output_port_name='OUT1', input_port_name='select')
        self.addConnection("pTehlZL50KRKIpqK_xpU-181", "pTehlZL50KRKIpqK_xpU-157", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("pTehlZL50KRKIpqK_xpU-183", "pTehlZL50KRKIpqK_xpU-157", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("pTehlZL50KRKIpqK_xpU-187", "pTehlZL50KRKIpqK_xpU-162", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("pTehlZL50KRKIpqK_xpU-190", "pTehlZL50KRKIpqK_xpU-167", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("pTehlZL50KRKIpqK_xpU-193", "pTehlZL50KRKIpqK_xpU-172", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("pTehlZL50KRKIpqK_xpU-157", "pTehlZL50KRKIpqK_xpU-162", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("pTehlZL50KRKIpqK_xpU-162", "pTehlZL50KRKIpqK_xpU-167", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("pTehlZL50KRKIpqK_xpU-167", "pTehlZL50KRKIpqK_xpU-172", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("pTehlZL50KRKIpqK_xpU-133", "pTehlZL50KRKIpqK_xpU-137", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("pTehlZL50KRKIpqK_xpU-133", "pTehlZL50KRKIpqK_xpU-141", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("pTehlZL50KRKIpqK_xpU-133", "pTehlZL50KRKIpqK_xpU-145", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("pTehlZL50KRKIpqK_xpU-133", "pTehlZL50KRKIpqK_xpU-149", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("pTehlZL50KRKIpqK_xpU-172", "OUT1", output_port_name='OUT1')


class PIDBlock(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=['IN2', 'IN1'], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(AdderBlock("pTehlZL50KRKIpqK_xpU-209"))
        self.addBlock(AdderBlock("pTehlZL50KRKIpqK_xpU-213"))
        self.addBlock(DerivatorBlock("pTehlZL50KRKIpqK_xpU-218"))
        self.addBlock(IntegratorBlock("pTehlZL50KRKIpqK_xpU-223"))
        self.addBlock(ProductBlock("pTehlZL50KRKIpqK_xpU-233"))
        self.addBlock(ConstantBlock("td", value=(0.075)))
        self.addBlock(ProductBlock("pTehlZL50KRKIpqK_xpU-241"))
        self.addBlock(ProductBlock("pTehlZL50KRKIpqK_xpU-245"))
        self.addBlock(ConstantBlock("k", value=(329.38)))
        self.addBlock(ConstantBlock("ti", value=(66.35)))
        self.addBlock(ConstantBlock("dl0SNWZN4P_1slR8nIbx-131", value=(0)))

        # Create the Connections
        self.addConnection("pTehlZL50KRKIpqK_xpU-209", "pTehlZL50KRKIpqK_xpU-213", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("IN1", "pTehlZL50KRKIpqK_xpU-241", input_port_name='IN1')
        self.addConnection("IN1", "pTehlZL50KRKIpqK_xpU-218", input_port_name='IN1')
        self.addConnection("IN1", "pTehlZL50KRKIpqK_xpU-223", input_port_name='IN1')
        self.addConnection("td", "pTehlZL50KRKIpqK_xpU-233", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("k", "pTehlZL50KRKIpqK_xpU-241", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("pTehlZL50KRKIpqK_xpU-223", "pTehlZL50KRKIpqK_xpU-245", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("ti", "pTehlZL50KRKIpqK_xpU-245", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("pTehlZL50KRKIpqK_xpU-233", "pTehlZL50KRKIpqK_xpU-209", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("pTehlZL50KRKIpqK_xpU-241", "pTehlZL50KRKIpqK_xpU-209", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("pTehlZL50KRKIpqK_xpU-245", "pTehlZL50KRKIpqK_xpU-213", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("pTehlZL50KRKIpqK_xpU-213", "OUT1", output_port_name='OUT1')
        self.addConnection("pTehlZL50KRKIpqK_xpU-218", "pTehlZL50KRKIpqK_xpU-233", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-131", "pTehlZL50KRKIpqK_xpU-218", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-131", "pTehlZL50KRKIpqK_xpU-223", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("IN2", "pTehlZL50KRKIpqK_xpU-223", input_port_name='delta_t')
        self.addConnection("IN2", "pTehlZL50KRKIpqK_xpU-218", input_port_name='delta_t')


class PlantBlock(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=['IN2', 'IN1'], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(ConstantBlock("half", value=(0.5)))
        self.addBlock(ConstantBlock("p", value=(1.2)))
        self.addBlock(ConstantBlock("Cd", value=(0.6)))
        self.addBlock(ConstantBlock("A", value=(9.12)))
        self.addBlock(ProductBlock("dl0SNWZN4P_1slR8nIbx-14"))
        self.addBlock(ProductBlock("dl0SNWZN4P_1slR8nIbx-18"))
        self.addBlock(ProductBlock("dl0SNWZN4P_1slR8nIbx-26"))
        self.addBlock(ProductBlock("dl0SNWZN4P_1slR8nIbx-32"))
        self.addBlock(ProductBlock("dl0SNWZN4P_1slR8nIbx-36"))
        self.addBlock(AdderBlock("dl0SNWZN4P_1slR8nIbx-47"))
        self.addBlock(NegatorBlock("dl0SNWZN4P_1slR8nIbx-55"))
        self.addBlock(InverterBlock("dl0SNWZN4P_1slR8nIbx-62"))
        self.addBlock(ConstantBlock("m_psgr", value=(77)))
        self.addBlock(ConstantBlock("m_trolley", value=(2376)))
        self.addBlock(AdderBlock("dl0SNWZN4P_1slR8nIbx-69"))
        self.addBlock(ProductBlock("dl0SNWZN4P_1slR8nIbx-76"))
        self.addBlock(IntegratorBlock("dl0SNWZN4P_1slR8nIbx-83"))
        self.addBlock(ConstantBlock("dl0SNWZN4P_1slR8nIbx-92", value=(0)))

        # Create the Connections
        self.addConnection("IN1", "dl0SNWZN4P_1slR8nIbx-55", input_port_name='IN1')
        self.addConnection("half", "dl0SNWZN4P_1slR8nIbx-14", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("p", "dl0SNWZN4P_1slR8nIbx-14", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("Cd", "dl0SNWZN4P_1slR8nIbx-18", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("A", "dl0SNWZN4P_1slR8nIbx-18", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-14", "dl0SNWZN4P_1slR8nIbx-26", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-18", "dl0SNWZN4P_1slR8nIbx-26", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-26", "dl0SNWZN4P_1slR8nIbx-36", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-32", "dl0SNWZN4P_1slR8nIbx-36", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-36", "dl0SNWZN4P_1slR8nIbx-47", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-55", "dl0SNWZN4P_1slR8nIbx-47", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("m_psgr", "dl0SNWZN4P_1slR8nIbx-69", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("m_trolley", "dl0SNWZN4P_1slR8nIbx-69", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-69", "dl0SNWZN4P_1slR8nIbx-62", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-47", "dl0SNWZN4P_1slR8nIbx-76", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-62", "dl0SNWZN4P_1slR8nIbx-76", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-83", "dl0SNWZN4P_1slR8nIbx-32", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-83", "dl0SNWZN4P_1slR8nIbx-32", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-83", "OUT1", output_port_name='OUT1')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-76", "dl0SNWZN4P_1slR8nIbx-83", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("dl0SNWZN4P_1slR8nIbx-92", "dl0SNWZN4P_1slR8nIbx-83", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("IN2", "dl0SNWZN4P_1slR8nIbx-83", input_port_name='delta_t')


class root(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=[])

        # Create the Blocks
        self.addBlock(LookupBlock("lookup"))
        self.addBlock(AdderBlock("sum"))
        self.addBlock(NegatorBlock("neg"))
        self.addBlock(PlantBlock("plant"))
        self.addBlock(PIDBlock("controller"))
        self.addBlock(ConstantBlock("delta_t", value=(1)))

        # Create the Connections
        self.addConnection("lookup", "sum", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("plant", "neg", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("neg", "sum", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("controller", "plant", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("sum", "controller", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("delta_t", "controller", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("delta_t", "plant", output_port_name='OUT1', input_port_name='IN2')


