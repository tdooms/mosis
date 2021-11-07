#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   /home/basil/gitProjects/mosis/3-cbd/convert/__main__.py -F CBD -e root -sSrgv simpson2.drawio -E delta=0.1 -f

from CBD.Core import *
from CBD.lib.std import *

DELTA_T = 0.1

class root(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=['IN1', 'delta_t', 'IC'], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(ModuloBlock("mod"))
        self.addBlock(ConstantBlock("two", value=(2)))
        self.addBlock(EqualsBlock("equal1"))
        self.addBlock(ConstantBlock("zero", value=(0)))
        self.addBlock(MultiplexerBlock("choice-integral1"))
        self.addBlock(TrapezoidBlock("trapezoid"))
        self.addBlock(SimpsonBlock("simpson"))
        self.addBlock(AdderBlock("sum"))
        self.addBlock(DelayBlock("delay2"))
        self.addBlock(MultiplexerBlock("sum_choice"))
        self.addBlock(ConstantBlock("xqcI94YeRySnhTKOGUdH-91", value=(0)))
        self.addBlock(EqualsBlock("equal2"))
        self.addBlock(MultiplexerBlock("choice-integral2"))
        self.addBlock(AddOneBlock("addone"))
        self.addBlock(DelayBlock("delay1"))

        # Create the Connections
        self.addConnection("IC", "simpson", input_port_name='IC')
        self.addConnection("IC", "trapezoid", input_port_name='IC')
        self.addConnection("IC", "choice-integral2", input_port_name='IN2')
        self.addConnection("IN1", "simpson", input_port_name='IN1')
        self.addConnection("IN1", "trapezoid", input_port_name='IN1')
        self.addConnection("delta_t", "simpson", input_port_name='delta_t')
        self.addConnection("delta_t", "trapezoid", input_port_name='delta_t')
        self.addConnection("mod", "equal1", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("zero", "equal1", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("zero", "equal2", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("zero", "delay1", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("equal1", "choice-integral1", output_port_name='OUT1', input_port_name='select')
        self.addConnection("equal1", "sum_choice", output_port_name='OUT1', input_port_name='select')
        self.addConnection("sum", "OUT1", output_port_name='OUT1')
        self.addConnection("sum", "sum_choice", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("sum_choice", "delay2", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("delay2", "sum_choice", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("delay2", "sum", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("xqcI94YeRySnhTKOGUdH-91", "delay2", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("trapezoid", "choice-integral1", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("simpson", "choice-integral1", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("choice-integral1", "choice-integral2", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("choice-integral2", "sum", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("equal2", "choice-integral2", output_port_name='OUT1', input_port_name='select')
        self.addConnection("two", "mod", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("addone", "delay1", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("delay1", "addone", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("delay1", "equal2", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("delay1", "mod", output_port_name='OUT1', input_port_name='IN1')


class SimpsonBlock(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=['IN1', 'delta_t', 'IC'], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(DelayBlock("delay2-s"))
        self.addBlock(DelayBlock("delay3-s"))
        self.addBlock(DelayBlock("delay1-s"))
        self.addBlock(AdderBlock("sum3-s"))
        self.addBlock(ProductBlock("div_by_6-s"))
        self.addBlock(ProductBlock("middle-s"))
        self.addBlock(InverterBlock("invert-s"))
        self.addBlock(ConstantBlock("six-s", value=(6)))
        self.addBlock(ConstantBlock("xqcI94YeRySnhTKOGUdH-169", value=(4)))
        self.addBlock(AdderBlock("sum2-s"))
        self.addBlock(AdderBlock("sum1-s"))
        self.addBlock(ProductBlock("final_product-s"))

        # Create the Connections
        self.addConnection("IC", "delay2-s", input_port_name='IC')
        self.addConnection("IC", "delay3-s", input_port_name='IC')
        self.addConnection("IN1", "delay2-s", input_port_name='IN1')
        self.addConnection("IN1", "sum2-s", input_port_name='IN1')
        self.addConnection("delta_t", "delay1-s", input_port_name='IN1')
        self.addConnection("delta_t", "delay1-s", input_port_name='IC')
        self.addConnection("delta_t", "sum3-s", input_port_name='IN2')
        self.addConnection("delay2-s", "delay3-s", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("delay2-s", "middle-s", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("delay1-s", "sum3-s", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("sum3-s", "div_by_6-s", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("six-s", "invert-s", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("invert-s", "div_by_6-s", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("xqcI94YeRySnhTKOGUdH-169", "middle-s", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("middle-s", "sum1-s", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("sum2-s", "sum1-s", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("delay3-s", "sum2-s", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("final_product-s", "OUT1", output_port_name='OUT1')
        self.addConnection("sum1-s", "final_product-s", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("div_by_6-s", "final_product-s", output_port_name='OUT1', input_port_name='IN2')


class TrapezoidBlock(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=['IN1', 'delta_t', 'IC'], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(DelayBlock("delay-t"))
        self.addBlock(ProductBlock("product1-t"))
        self.addBlock(ConstantBlock("half-t", value=(0.5)))
        self.addBlock(AdderBlock("accumulator-t"))
        self.addBlock(ProductBlock("product2-t"))

        # Create the Connections
        self.addConnection("IC", "delay-t", input_port_name='IC')
        self.addConnection("IN1", "delay-t", input_port_name='IN1')
        self.addConnection("IN1", "accumulator-t", input_port_name='IN1')
        self.addConnection("delta_t", "product1-t", input_port_name='IN1')
        self.addConnection("half-t", "product1-t", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("delay-t", "accumulator-t", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("accumulator-t", "product2-t", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("product1-t", "product2-t", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("product2-t", "OUT1", output_port_name='OUT1')


