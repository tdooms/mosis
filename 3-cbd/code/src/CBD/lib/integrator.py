from CBD.Core import CBD
from std import *


class IntegratorBlock(CBD):
    def forward_euler(self):
        # Create the Blocks
        self.addBlock(DelayBlock("delay"))
        self.addBlock(ProductBlock("multiply"))
        self.addBlock(AdderBlock("accum"))

        # Create the Connections
        self.addConnection("IN1", "multiply", input_port_name='IN2')
        self.addConnection("delay", "accum", output_port_name='OUT1',
                           input_port_name='IN2')
        self.addConnection("multiply", "accum", output_port_name='OUT1',
                           input_port_name='IN1')
        self.addConnection("accum", "delay", output_port_name='OUT1',
                           input_port_name='IN1')
        self.addConnection("accum", "OUT1", output_port_name='OUT1')
        self.addConnection("IC", "delay", input_port_name='IC')
        self.addConnection("delta_t", "multiply", input_port_name='IN1')

    def trapezoid(self):
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
        self.addConnection("accumulator", "delay_state",
                           output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("y0", "delay_input", output_port_name='OUT1',
                           input_port_name='IC')
        self.addConnection("delay_input", "mid_adder", output_port_name='OUT1',
                           input_port_name='IN1')
        self.addConnection("mid_adder", "mult", output_port_name='OUT1',
                           input_port_name='IN1')
        self.addConnection("delay_state", "accumulator",
                           output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("mult", "accumulator", output_port_name='OUT1',
                           input_port_name='IN2')
        self.addConnection("IC", "delay_state", input_port_name='IC')
        self.addConnection("delta_t", "delta_halver", input_port_name='IN1')
        self.addConnection("delta_halver", "mult", output_port_name='OUT1',
                           input_port_name='IN2')
        self.addConnection("halver", "delta_halver", output_port_name='OUT1',
                           input_port_name='IN2')

    def simpson(self):
        class SimpsonBlock(CBD):
            def __init__(self, block_name):
                super().__init__(block_name,
                                 input_ports=['IC', 'delta_t', 'IN1'],
                                 output_ports=['OUT1'])

                # Create the Blocks
                self.addBlock(DelayBlock("xqcI94YeRySnhTKOGUdH-113"))
                self.addBlock(DelayBlock("xqcI94YeRySnhTKOGUdH-117"))
                self.addBlock(DelayBlock("xqcI94YeRySnhTKOGUdH-133"))
                self.addBlock(AdderBlock("xqcI94YeRySnhTKOGUdH-142"))
                self.addBlock(ProductBlock("div_by_6"))
                self.addBlock(ProductBlock("middle"))
                self.addBlock(InverterBlock("xqcI94YeRySnhTKOGUdH-162"))
                self.addBlock(
                    ConstantBlock("xqcI94YeRySnhTKOGUdH-165", value=(6)))
                self.addBlock(
                    ConstantBlock("xqcI94YeRySnhTKOGUdH-169", value=(4)))
                self.addBlock(AdderBlock("sum2"))
                self.addBlock(AdderBlock("sum1"))
                self.addBlock(ProductBlock("final_product"))

                # Create the Connections
                self.addConnection("IC", "xqcI94YeRySnhTKOGUdH-113",
                                   input_port_name='IC')
                self.addConnection("IC", "xqcI94YeRySnhTKOGUdH-117",
                                   input_port_name='IC')
                self.addConnection("IN1", "xqcI94YeRySnhTKOGUdH-113",
                                   input_port_name='IN1')
                self.addConnection("IN1", "sum2", input_port_name='IN1')
                self.addConnection("delta_t", "xqcI94YeRySnhTKOGUdH-133",
                                   input_port_name='IN1')
                self.addConnection("delta_t", "xqcI94YeRySnhTKOGUdH-133",
                                   input_port_name='IC')
                self.addConnection("delta_t", "xqcI94YeRySnhTKOGUdH-142",
                                   input_port_name='IN2')
                self.addConnection("xqcI94YeRySnhTKOGUdH-113",
                                   "xqcI94YeRySnhTKOGUdH-117",
                                   output_port_name='OUT1',
                                   input_port_name='IN1')
                self.addConnection("xqcI94YeRySnhTKOGUdH-113", "middle",
                                   output_port_name='OUT1',
                                   input_port_name='IN2')
                self.addConnection("xqcI94YeRySnhTKOGUdH-133",
                                   "xqcI94YeRySnhTKOGUdH-142",
                                   output_port_name='OUT1',
                                   input_port_name='IN1')
                self.addConnection("xqcI94YeRySnhTKOGUdH-142", "div_by_6",
                                   output_port_name='OUT1',
                                   input_port_name='IN1')
                self.addConnection("xqcI94YeRySnhTKOGUdH-165",
                                   "xqcI94YeRySnhTKOGUdH-162",
                                   output_port_name='OUT1',
                                   input_port_name='IN1')
                self.addConnection("xqcI94YeRySnhTKOGUdH-162", "div_by_6",
                                   output_port_name='OUT1',
                                   input_port_name='IN2')
                self.addConnection("xqcI94YeRySnhTKOGUdH-169", "middle",
                                   output_port_name='OUT1',
                                   input_port_name='IN1')
                self.addConnection("middle", "sum1", output_port_name='OUT1',
                                   input_port_name='IN2')
                self.addConnection("sum2", "sum1", output_port_name='OUT1',
                                   input_port_name='IN1')
                self.addConnection("xqcI94YeRySnhTKOGUdH-117", "sum2",
                                   output_port_name='OUT1',
                                   input_port_name='IN2')
                self.addConnection("final_product", "OUT1",
                                   output_port_name='OUT1')
                self.addConnection("sum1", "final_product",
                                   output_port_name='OUT1',
                                   input_port_name='IN1')
                self.addConnection("div_by_6", "final_product",
                                   output_port_name='OUT1',
                                   input_port_name='IN2')

        class TrapezoidBlock(CBD):
            def __init__(self, block_name):
                super().__init__(block_name,
                                 input_ports=['IC', 'delta_t', 'IN1'],
                                 output_ports=['OUT1'])

                # Create the Blocks
                self.addBlock(DelayBlock("xqcI94YeRySnhTKOGUdH-193"))
                self.addBlock(ProductBlock("xqcI94YeRySnhTKOGUdH-199"))
                self.addBlock(
                    ConstantBlock("xqcI94YeRySnhTKOGUdH-204", value=(0.5)))
                self.addBlock(AdderBlock("xqcI94YeRySnhTKOGUdH-207"))
                self.addBlock(ProductBlock("xqcI94YeRySnhTKOGUdH-213"))

                # Create the Connections
                self.addConnection("IC", "xqcI94YeRySnhTKOGUdH-193",
                                   input_port_name='IC')
                self.addConnection("IN1", "xqcI94YeRySnhTKOGUdH-193",
                                   input_port_name='IN1')
                self.addConnection("IN1", "xqcI94YeRySnhTKOGUdH-207",
                                   input_port_name='IN1')
                self.addConnection("delta_t", "xqcI94YeRySnhTKOGUdH-199",
                                   input_port_name='IN1')
                self.addConnection("xqcI94YeRySnhTKOGUdH-204",
                                   "xqcI94YeRySnhTKOGUdH-199",
                                   output_port_name='OUT1',
                                   input_port_name='IN2')
                self.addConnection("xqcI94YeRySnhTKOGUdH-193",
                                   "xqcI94YeRySnhTKOGUdH-207",
                                   output_port_name='OUT1',
                                   input_port_name='IN2')
                self.addConnection("xqcI94YeRySnhTKOGUdH-207",
                                   "xqcI94YeRySnhTKOGUdH-213",
                                   output_port_name='OUT1',
                                   input_port_name='IN1')
                self.addConnection("xqcI94YeRySnhTKOGUdH-199",
                                   "xqcI94YeRySnhTKOGUdH-213",
                                   output_port_name='OUT1',
                                   input_port_name='IN2')
                self.addConnection("xqcI94YeRySnhTKOGUdH-213", "OUT1",
                                   output_port_name='OUT1')

        # Create the Blocks
        self.addBlock(ModuloBlock("xqcI94YeRySnhTKOGUdH-17"))
        self.addBlock(ConstantBlock("xqcI94YeRySnhTKOGUdH-21", value=(2)))
        self.addBlock(EqualsBlock("xqcI94YeRySnhTKOGUdH-25"))
        self.addBlock(ConstantBlock("xqcI94YeRySnhTKOGUdH-29", value=(0)))
        self.addBlock(MultiplexerBlock("xqcI94YeRySnhTKOGUdH-33"))
        self.addBlock(TrapezoidBlock("trapezoid"))
        self.addBlock(SimpsonBlock("simpson"))
        self.addBlock(AdderBlock("xqcI94YeRySnhTKOGUdH-65"))
        self.addBlock(DelayBlock("xqcI94YeRySnhTKOGUdH-71"))
        self.addBlock(MultiplexerBlock("xqcI94YeRySnhTKOGUdH-83"))
        self.addBlock(ConstantBlock("xqcI94YeRySnhTKOGUdH-91", value=(0)))
        self.addBlock(EqualsBlock("xqcI94YeRySnhTKOGUdH-225"))
        self.addBlock(MultiplexerBlock("xqcI94YeRySnhTKOGUdH-231"))
        self.addBlock(AddOneBlock("LFYGzvRloyAe_HxOVc6M-1"))
        self.addBlock(DelayBlock("LFYGzvRloyAe_HxOVc6M-5"))

        # Create the Connections
        self.addConnection("IC", "simpson", input_port_name='IC')
        self.addConnection("IC", "trapezoid", input_port_name='IC')
        self.addConnection("IC", "xqcI94YeRySnhTKOGUdH-231",
                           input_port_name='IN2')
        self.addConnection("IN1", "simpson", input_port_name='IN1')
        self.addConnection("IN1", "trapezoid", input_port_name='IN1')
        self.addConnection("delta_t", "simpson", input_port_name='delta_t')
        self.addConnection("delta_t", "trapezoid", input_port_name='delta_t')
        self.addConnection("xqcI94YeRySnhTKOGUdH-17", "xqcI94YeRySnhTKOGUdH-25",
                           output_port_name='OUT1',
                           input_port_name='IN1')
        self.addConnection("xqcI94YeRySnhTKOGUdH-29", "xqcI94YeRySnhTKOGUdH-25",
                           output_port_name='OUT1',
                           input_port_name='IN2')
        self.addConnection("xqcI94YeRySnhTKOGUdH-29",
                           "xqcI94YeRySnhTKOGUdH-225", output_port_name='OUT1',
                           input_port_name='IN1')
        self.addConnection("xqcI94YeRySnhTKOGUdH-29", "LFYGzvRloyAe_HxOVc6M-5",
                           output_port_name='OUT1',
                           input_port_name='IC')
        self.addConnection("xqcI94YeRySnhTKOGUdH-25", "xqcI94YeRySnhTKOGUdH-33",
                           output_port_name='OUT1',
                           input_port_name='select')
        self.addConnection("xqcI94YeRySnhTKOGUdH-25", "xqcI94YeRySnhTKOGUdH-83",
                           output_port_name='OUT1',
                           input_port_name='select')
        self.addConnection("xqcI94YeRySnhTKOGUdH-65", "OUT1",
                           output_port_name='OUT1')
        self.addConnection("xqcI94YeRySnhTKOGUdH-65", "xqcI94YeRySnhTKOGUdH-83",
                           output_port_name='OUT1',
                           input_port_name='IN2')
        self.addConnection("xqcI94YeRySnhTKOGUdH-83", "xqcI94YeRySnhTKOGUdH-71",
                           output_port_name='OUT1',
                           input_port_name='IN1')
        self.addConnection("xqcI94YeRySnhTKOGUdH-71", "xqcI94YeRySnhTKOGUdH-83",
                           output_port_name='OUT1',
                           input_port_name='IN1')
        self.addConnection("xqcI94YeRySnhTKOGUdH-71", "xqcI94YeRySnhTKOGUdH-65",
                           output_port_name='OUT1',
                           input_port_name='IN1')
        self.addConnection("xqcI94YeRySnhTKOGUdH-91", "xqcI94YeRySnhTKOGUdH-71",
                           output_port_name='OUT1',
                           input_port_name='IC')
        self.addConnection("trapezoid", "xqcI94YeRySnhTKOGUdH-33",
                           output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("simpson", "xqcI94YeRySnhTKOGUdH-33",
                           output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("xqcI94YeRySnhTKOGUdH-33",
                           "xqcI94YeRySnhTKOGUdH-231", output_port_name='OUT1',
                           input_port_name='IN1')
        self.addConnection("xqcI94YeRySnhTKOGUdH-231",
                           "xqcI94YeRySnhTKOGUdH-65", output_port_name='OUT1',
                           input_port_name='IN2')
        self.addConnection("xqcI94YeRySnhTKOGUdH-225",
                           "xqcI94YeRySnhTKOGUdH-231", output_port_name='OUT1',
                           input_port_name='select')
        self.addConnection("xqcI94YeRySnhTKOGUdH-21", "xqcI94YeRySnhTKOGUdH-17",
                           output_port_name='OUT1',
                           input_port_name='IN2')
        self.addConnection("LFYGzvRloyAe_HxOVc6M-1", "LFYGzvRloyAe_HxOVc6M-5",
                           output_port_name='OUT1',
                           input_port_name='IN1')
        self.addConnection("LFYGzvRloyAe_HxOVc6M-5", "LFYGzvRloyAe_HxOVc6M-1",
                           output_port_name='OUT1',
                           input_port_name='IN1')
        self.addConnection("LFYGzvRloyAe_HxOVc6M-5", "xqcI94YeRySnhTKOGUdH-225",
                           output_port_name='OUT1',
                           input_port_name='IN2')
        self.addConnection("LFYGzvRloyAe_HxOVc6M-5", "xqcI94YeRySnhTKOGUdH-17",
                           output_port_name='OUT1',
                           input_port_name='IN1')


