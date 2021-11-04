#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   C:/Users/thoma/PycharmProjects/mosis/3-cbd/convert/__main__.py -e lookup -F CBD C:\Users\thoma\PycharmProjects\mosis\3-cbd\convert\trollieeeees.drawio

from CBD.Core import *
from CBD.lib.std import *


class lookup(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=['output'])

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
        self.addConnection("pTehlZL50KRKIpqK_xpU-172", "output", output_port_name='OUT1')


