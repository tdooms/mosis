"""
This file contains the standard library for CBD building blocks.
"""
from CBD.Core import BaseBlock, CBD, level
from CBD import naivelog
import math

__all__ = ['ConstantBlock', 'NegatorBlock', 'InverterBlock', 'AdderBlock', 'ProductBlock', 'ModuloBlock',
           'RootBlock', 'AbsBlock', 'IntBlock', 'ClampBlock', 'GenericBlock', 'MultiplexerBlock', 'LessThanBlock',
           'EqualsBlock', 'LessThanOrEqualsBlock', 'NotBlock', 'OrBlock', 'AndBlock', 'DelayBlock', 'LoggingBlock',
           'AddOneBlock', 'DerivatorBlock', 'IntegratorBlock', 'SplitBlock', 'Clock', 'TimeBlock', 'PowerBlock',
           'MaxBlock', 'MinBlock']

class ConstantBlock(BaseBlock):
	"""
	The constant block will always output its constant value
	"""
	def __init__(self, block_name, value=0.0):
		BaseBlock.__init__(self, block_name, [], ["OUT1"])
		self.__value = value

	def getValue(self):
		"""Get the current value."""
		return self.__value

	def setValue(self, value):
		"""Change the constant value."""
		self.__value = value

	def compute(self, curIteration):
		self.appendToSignal(self.getValue())

	def __repr__(self):
		return BaseBlock.__repr__(self) + "  Value = " + str(self.getValue()) + "\n"


class NegatorBlock(BaseBlock):
	"""
	The negator block will output the value of the input multiplied with -1
	"""
	def __init__(self, block_name):
		BaseBlock.__init__(self, block_name, ["IN1"], ["OUT1"])

	def compute(self, curIteration):
		signal = self.getInputSignal(curIteration)
		self.appendToSignal(-signal.value)


class InverterBlock(BaseBlock):
	"""
	The invertblock will output 1/IN
	"""
	def __init__(self, block_name, tolerance=1e-30):
		BaseBlock.__init__(self, block_name, ["IN1"], ["OUT1"])
		self._tolerance = tolerance

	def compute(self, curIteration):
		signal = self.getInputSignal(curIteration)
		self.appendToSignal(1.0 / signal.value)


class AdderBlock(BaseBlock):
	"""
	The adderblock will add all the inputs.

	Args:
		block_name (str):       The name of the block.
		numberOfInputs (int):   The amount of input ports to set.
	"""
	def __init__(self, block_name, numberOfInputs=2):
		BaseBlock.__init__(self, block_name, ["IN%d" % (x+1) for x in range(numberOfInputs)], ["OUT1"])
		self.__numberOfInputs = numberOfInputs

	def compute(self, curIteration):
		signal1 = self.getInputSignal(curIteration, input_port="IN1")
		signal2 = self.getInputSignal(curIteration, input_port="IN2")
		self.appendToSignal(signal1.value + signal2.value)

	def getNumberOfInputs(self):
		"""
		Gets the total number of input ports.
		"""
		return self.__numberOfInputs

class ProductBlock(BaseBlock):
	"""
	The product block will multiply all the inputs
	"""
	def __init__(self, block_name, numberOfInputs=2):
		BaseBlock.__init__(self, block_name, ["IN%d" % (x+1) for x in range(numberOfInputs)], ["OUT1"])
		self.__numberOfInputs = numberOfInputs

	def compute(self, curIteration):
		signal1 = self.getInputSignal(curIteration, input_port="IN1")
		signal2 = self.getInputSignal(curIteration, input_port="IN2")
		self.appendToSignal(signal1.value * signal2.value)

	def getNumberOfInputs(self):
		"""
		Gets the total number of input ports.
		"""
		return self.__numberOfInputs


class ModuloBlock(BaseBlock):
	"""
	A basic block that computes the IN1 modulo IN2
	"""
	def __init__(self, block_name):
		BaseBlock.__init__(self, block_name, ["IN1", "IN2"], ["OUT1"])

	def compute(self, curIteration):
		signal1 = self.getInputSignal(curIteration, input_port="IN1")
		signal2 = self.getInputSignal(curIteration, input_port="IN2")
		self.appendToSignal(math.fmod(signal1.value, signal2.value))


class RootBlock(BaseBlock):
	"""
	A basic block that computes the IN2-th root from IN1
	"""
	def __init__(self, block_name):
		BaseBlock.__init__(self, block_name, ["IN1", "IN2"], ["OUT1"])

	def compute(self, curIteration):
		signal1 = self.getInputSignal(curIteration, input_port="IN1")
		signal2 = self.getInputSignal(curIteration, input_port="IN2")
		self.appendToSignal(signal1.value ** (1.0 / signal2.value))


class PowerBlock(BaseBlock):
	"""
	A basic block that computes IN1 to the IN2-th power
	"""
	def __init__(self, block_name):
		BaseBlock.__init__(self, block_name, ["IN1", "IN2"], ["OUT1"])

	def compute(self, curIteration):
		signal1 = self.getInputSignal(curIteration, input_port="IN1")
		signal2 = self.getInputSignal(curIteration, input_port="IN2")
		self.appendToSignal(signal1.value ** signal2.value)


class AbsBlock(BaseBlock):
	"""
	The abs block will output the absolute value of the input.
	"""
	def __init__(self, block_name):
		BaseBlock.__init__(self, block_name, ["IN1"], ["OUT1"])

	def compute(self, curIteration):
		signal = self.getInputSignal(curIteration, input_port="IN1")
		self.appendToSignal(abs(signal.value))


class IntBlock(BaseBlock):
	"""
	The int block will output the integer value (floored) of the input.
	"""
	def __init__(self, block_name):
		BaseBlock.__init__(self, block_name, ["IN1"], ["OUT1"])

	def compute(self, curIteration):
		self.appendToSignal(int(self.getInputSignal(curIteration).value))


class ClampBlock(BaseBlock):
	"""
	The clamp block will clamp the input between min and max.

	Args:
		block_name (str):   The name of the block.
		min (numeric):      The minimal value.
		max (numeric):      The maximal value.
		use_const (bool):   When :code:`True`, the :attr:`min` and :attr:`max`
							values will be used. Otherwise, the minimal and
							maximal values are expected as inputs 2 and 3,
							respectively.
	"""
	def __init__(self, block_name, min=-1, max=1, use_const=True):
		super().__init__(block_name, ["IN1"] if use_const else ["IN1", "IN2", "IN3"], ["OUT1"])
		self._use_const = use_const
		self.min = min
		self.max = max

	def compute(self, curIteration):
		if self._use_const:
			min_ = self.min
			max_ = self.max
		else:
			min_ = self.getInputSignal(curIteration, "IN2").value
			max_ = self.getInputSignal(curIteration, "IN3").value
		x = self.getInputSignal(curIteration, "IN1").value
		self.appendToSignal(min(max(x, min_), max_))


class GenericBlock(BaseBlock):
	"""
	The generic block will evaluate the operator on the input
	operator is the name (a string) of a Python function from the math library
	which will be called when the block is evaluated
	by default, initialized to None
	"""
	def __init__(self, block_name, block_operator=None):
		# operator is the name (a string) of a Python function from the math library
		BaseBlock.__init__(self, block_name, ["IN1"], ["OUT1"])
		self.__block_operator = block_operator

	def getBlockOperator(self):
		"""
		Gets the block operator.
		"""
		return self.__block_operator

	def compute(self, curIteration):
		"""
			Get the function pointer from the built-in math library,
			This way we don't have to do any if-statements
		"""
		operator = getattr(math, self.getBlockOperator())
		signal = self.getInputSignal(curIteration)
		self.appendToSignal(operator(signal.value))

	def __repr__(self):
		repr = BaseBlock.__repr__(self)
		if self.__block_operator is None:
			repr += "  No operator given\n"
		else:
			repr += "  Operator :: " + self.__block_operator + "\n"
		return repr


class MultiplexerBlock(BaseBlock):
	"""
	The multiplexer block will output the signal from IN1 if select == 0; otherwise
	the signal from IN2 is outputted.
	"""
	def __init__(self, block_name):
		BaseBlock.__init__(self, block_name, ["IN1", "IN2", "select"], ["OUT1"])

	def compute(self, curIteration):
		select = self.getInputSignal(curIteration, "select").value
		self.appendToSignal(self.getInputSignal(curIteration, "IN1" if select == 0 else "IN2").value)


class MaxBlock(BaseBlock):
	"""
	The max block will output the maximal value of all its inputs.
	"""
	def __init__(self, block_name, numberOfInputs=2):
		BaseBlock.__init__(self, block_name, ["IN%d" % (x+1) for x in range(numberOfInputs)], ["OUT1"])
		self.__numberOfInputs = numberOfInputs

	def compute(self, curIteration):
		signal1 = self.getInputSignal(curIteration, input_port="IN1")
		signal2 = self.getInputSignal(curIteration, input_port="IN2")
		self.appendToSignal(max(signal1.value, signal2.value))

	def getNumberOfInputs(self):
		"""
		Gets the total number of input ports.
		"""
		return self.__numberOfInputs


class MinBlock(BaseBlock):
	"""
	The min block will output the minimal value of all its inputs.
	"""
	def __init__(self, block_name, numberOfInputs=2):
		BaseBlock.__init__(self, block_name, ["IN%d" % (x+1) for x in range(numberOfInputs)], ["OUT1"])
		self.__numberOfInputs = numberOfInputs

	def compute(self, curIteration):
		signal1 = self.getInputSignal(curIteration, input_port="IN1")
		signal2 = self.getInputSignal(curIteration, input_port="IN2")
		self.appendToSignal(min(signal1.value, signal2.value))

	def getNumberOfInputs(self):
		"""
		Gets the total number of input ports.
		"""
		return self.__numberOfInputs


class SplitBlock(BaseBlock):
	"""
	The split block will split a signal over multiple paths.
	While this block can generally be omitted, it may still be
	used for clarity and clean-ness of the resulting models.

	Args:
		block_name (str):       The name of the block.
		numberOfOutputs (int):  The amount of paths to split into.
	"""
	def __init__(self, block_name, numberOfOutputs=2):
		BaseBlock.__init__(self, block_name, ["IN1"], ["OUT%d" % (i+1) for i in range(numberOfOutputs)])
		self.__numberOfOutputs = numberOfOutputs

	def compute(self, curIteration):
		value = self.getInputSignal(curIteration).value
		for i in range(self.__numberOfOutputs):
			self.appendToSignal(value, "OUT%d" % (i+1))

	def getNumberOfOutputs(self):
		"""
		Gets the total number of output ports.
		"""
		return self.__numberOfOutputs


class LessThanBlock(BaseBlock):
	"""
	A simple block that will test if the IN1 is smaller than IN2 (output == 1 if true else 0)
	"""
	def __init__(self, block_name):
		BaseBlock.__init__(self, block_name, ["IN1", "IN2"], ["OUT1"])

	def	compute(self, curIteration):
		gisv = lambda s: self.getInputSignal(curIteration, s).value
		self.appendToSignal(1 if gisv("IN1") < gisv("IN2") else 0)


class EqualsBlock(BaseBlock):
	"""
	A simple block that will test if the IN1 is equal to IN2 (output == 1 if true else 0)
	"""
	def __init__(self, block_name):
		BaseBlock.__init__(self, block_name, ["IN1", "IN2"], ["OUT1"])

	def	compute(self, curIteration):
		gisv = lambda s: self.getInputSignal(curIteration, s).value
		self.appendToSignal(1 if gisv("IN1") == gisv("IN2") else 0)


class LessThanOrEqualsBlock(BaseBlock):
	"""
	A simple block that will test if the IN1 is smaller than or equals to IN2 (output == 1 if true else 0)
	"""
	def __init__(self, block_name):
		BaseBlock.__init__(self, block_name, ["IN1", "IN2"], ["OUT1"])

	def	compute(self, curIteration):
		gisv = lambda s: self.getInputSignal(curIteration, s).value
		self.appendToSignal(1 if gisv("IN1") <= gisv("IN2") else 0)


class NotBlock(BaseBlock):
	"""
	A simple Not block that will set a 0 to 1 and vice versa
	"""
	def __init__(self, block_name):
		BaseBlock.__init__(self, block_name, ["IN1"], ["OUT1"])

	def	compute(self, curIteration):
		result = 0 if self.getInputSignal(curIteration, "IN1").value else 1
		self.appendToSignal(result)


class OrBlock(BaseBlock):
	"""
	A simple Or block with possibly multiple inputlines
	"""
	def __init__(self, block_name, numberOfInputs=2):
		BaseBlock.__init__(self, block_name, ["IN{0}".format(i) for i in range(1,numberOfInputs+1)], ["OUT1"])
		self.__numberOfInputs = numberOfInputs

	def	compute(self, curIteration):
		result = 0
		for i in range(1, self.__numberOfInputs+1):
			result = result or self.getInputSignal(curIteration, "IN"+str(i)).value
		self.appendToSignal(result)

	def getNumberOfInputs(self):
		"""
		Gets the total number of input ports.
		"""
		return self.__numberOfInputs


class AndBlock(BaseBlock):
	"""
	A simple And block with possibly multiple inputlines
	"""
	def __init__(self, block_name, numberOfInputs=2):
		BaseBlock.__init__(self, block_name, ["IN{0}".format(i) for i in range(1,numberOfInputs+1)], ["OUT1"])
		self.__numberOfInputs = numberOfInputs

	def	compute(self, curIteration):
		result = 1
		for i in range(1, self.__numberOfInputs+1):
			result = result and self.getInputSignal(curIteration, "IN"+str(i)).value
		self.appendToSignal(result)

	def getNumberOfInputs(self):
		"""
		Gets the total number of input ports.
		"""
		return self.__numberOfInputs


class DelayBlock(BaseBlock):
	"""
	A delay block that takes the last value from the list
	IC: Initial Condition
	"""
	def __init__(self, block_name):
		BaseBlock.__init__(self, block_name, ["IN1", "IC"], ["OUT1"])

	def getDependencies(self, curIteration):
		return [self._linksIn["IC"].block] if curIteration == 0 else []

	def compute(self, curIteration):
		if curIteration == 0:
			self.appendToSignal(self.getInputSignal(curIteration, "IC").value)
		else:
			self.appendToSignal(self.getInputSignal(curIteration - 1).value)


class LoggingBlock(BaseBlock):
	"""
	A simple Logging block
	"""
	def __init__(self, block_name, string, lev=level.WARNING):
		BaseBlock.__init__(self, block_name, ["IN1"], [])
		self.__string = string
		self.__logger = naivelog.getLogger("WarningLog")
		self.__lev = lev

	def compute(self, curIteration):
		if self.getInputSignal(curIteration, "IN1").value == 1:
			if self.__lev == level.WARNING:
				self.__logger.warning("Time " + str(self.getClock().getTime(curIteration)) + ": " + self.__string)
			elif self.__lev == level.ERROR:
				self.__logger.error("Time " + str(self.getClock().getTime(curIteration)) + ": " + self.__string)
			elif self.__lev == level.FATAL:
				self.__logger.fatal("Time " + str(self.getClock().getTime(curIteration)) + ": " + self.__string)


class AddOneBlock(CBD):
	"""
	Block adds a one to the input (used a lot for mux)
	"""
	def __init__(self, block_name):
		CBD.__init__(self, block_name, ["IN1"], ["OUT1"])
		self.addBlock(ConstantBlock(block_name="OneConstant", value=1))
		self.addBlock(AdderBlock("PlusOne"))
		self.addConnection("IN1", "PlusOne")
		self.addConnection("OneConstant", "PlusOne")
		self.addConnection("PlusOne", "OUT1")


class DerivatorBlock(CBD):
	"""
	The derivator block is a CBD that calculates the derivative.
	"""
	def __init__(self, block_name):
		CBD.__init__(self, block_name, ["IN1", "delta_t", "IC"], ["OUT1"])
		# TODO understand
		# Create the blocks
		self.addBlock(ProductBlock(block_name="multiply_ic"))
		self.addBlock(ProductBlock(block_name="multiply"))

		self.addBlock(InverterBlock(block_name="inverter"))

		self.addBlock(NegatorBlock(block_name="negator1"))
		self.addBlock(NegatorBlock(block_name="negator2"))

		self.addBlock(AdderBlock(block_name="sum1"))
		self.addBlock(AdderBlock(block_name="sum2"))

		self.addBlock(DelayBlock(block_name="delay"))

		# Connect the blocks
		self.addConnection("IC", "multiply_ic")
		self.addConnection("delta_t", "multiply_ic")

		self.addConnection("multiply_ic", "negator1")
		self.addConnection("negator1", "sum1")
		self.addConnection("IN1", "sum1")

		self.addConnection("sum1", "delay", input_port_name="IC")
		self.addConnection("IN1", "delay", input_port_name="IN1")

		self.addConnection("delay", "negator2")
		self.addConnection("negator2", "sum2")
		self.addConnection("IN1", "sum2")

		self.addConnection("delta_t", "inverter")
		self.addConnection("inverter", "multiply")
		self.addConnection("sum2", "multiply")

		self.addConnection("multiply", "OUT1")


class IntegratorBlock(CBD):
	"""
	The integrator block is a CBD that calculates the integration.
	The block is implemented according to the backwards Euler rule.
	"""

	def forward_euler(self):
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

	def backward_euler(self):
		# Create the Blocks
		self.addBlock(ConstantBlock(block_name="y0", value=0))
		self.addBlock(AdderBlock(block_name="sum"))
		self.addBlock(ProductBlock(block_name="multiply"))
		self.addBlock(DelayBlock(block_name="delay"))
		self.addBlock(DelayBlock(block_name="delayState"))

		# Create the Connections
		self.addConnection("IC", "delayState", input_port_name="IC")
		self.addConnection("y0", "delay", input_port_name="IC")
		self.addConnection("IN1", "delay", input_port_name="IN1")
		self.addConnection("delay", "multiply")
		self.addConnection("delta_t", "multiply")
		self.addConnection("delayState", "sum")
		self.addConnection("multiply", "sum")
		self.addConnection("sum", "delayState", input_port_name="IN1")
		self.addConnection("sum", "OUT1")

	def simpson(self):
		class SimpsonBlock(CBD):
			def __init__(self, block_name):
				super().__init__(block_name, input_ports=['IC', 'delta_t', 'IN1'], output_ports=['OUT1'])

				# Create the Blocks
				self.addBlock(DelayBlock("xqcI94YeRySnhTKOGUdH-113"))
				self.addBlock(DelayBlock("xqcI94YeRySnhTKOGUdH-117"))
				self.addBlock(DelayBlock("xqcI94YeRySnhTKOGUdH-133"))
				self.addBlock(AdderBlock("xqcI94YeRySnhTKOGUdH-142"))
				self.addBlock(ProductBlock("div_by_6"))
				self.addBlock(ProductBlock("middle"))
				self.addBlock(InverterBlock("xqcI94YeRySnhTKOGUdH-162"))
				self.addBlock(ConstantBlock("xqcI94YeRySnhTKOGUdH-165", value=(6)))
				self.addBlock(ConstantBlock("xqcI94YeRySnhTKOGUdH-169", value=(4)))
				self.addBlock(AdderBlock("sum2"))
				self.addBlock(AdderBlock("sum1"))
				self.addBlock(ProductBlock("final_product"))

				# Create the Connections
				self.addConnection("IC", "xqcI94YeRySnhTKOGUdH-113", input_port_name='IC')
				self.addConnection("IC", "xqcI94YeRySnhTKOGUdH-117", input_port_name='IC')
				self.addConnection("IN1", "xqcI94YeRySnhTKOGUdH-113", input_port_name='IN1')
				self.addConnection("IN1", "sum2", input_port_name='IN1')
				self.addConnection("delta_t", "xqcI94YeRySnhTKOGUdH-133", input_port_name='IN1')
				self.addConnection("delta_t", "xqcI94YeRySnhTKOGUdH-133", input_port_name='IC')
				self.addConnection("delta_t", "xqcI94YeRySnhTKOGUdH-142", input_port_name='IN2')
				self.addConnection("xqcI94YeRySnhTKOGUdH-113", "xqcI94YeRySnhTKOGUdH-117", output_port_name='OUT1',
								   input_port_name='IN1')
				self.addConnection("xqcI94YeRySnhTKOGUdH-113", "middle", output_port_name='OUT1', input_port_name='IN2')
				self.addConnection("xqcI94YeRySnhTKOGUdH-133", "xqcI94YeRySnhTKOGUdH-142", output_port_name='OUT1',
								   input_port_name='IN1')
				self.addConnection("xqcI94YeRySnhTKOGUdH-142", "div_by_6", output_port_name='OUT1',
								   input_port_name='IN1')
				self.addConnection("xqcI94YeRySnhTKOGUdH-165", "xqcI94YeRySnhTKOGUdH-162", output_port_name='OUT1',
								   input_port_name='IN1')
				self.addConnection("xqcI94YeRySnhTKOGUdH-162", "div_by_6", output_port_name='OUT1',
								   input_port_name='IN2')
				self.addConnection("xqcI94YeRySnhTKOGUdH-169", "middle", output_port_name='OUT1', input_port_name='IN1')
				self.addConnection("middle", "sum1", output_port_name='OUT1', input_port_name='IN2')
				self.addConnection("sum2", "sum1", output_port_name='OUT1', input_port_name='IN1')
				self.addConnection("xqcI94YeRySnhTKOGUdH-117", "sum2", output_port_name='OUT1', input_port_name='IN2')
				self.addConnection("final_product", "OUT1", output_port_name='OUT1')
				self.addConnection("sum1", "final_product", output_port_name='OUT1', input_port_name='IN1')
				self.addConnection("div_by_6", "final_product", output_port_name='OUT1', input_port_name='IN2')

		class TrapezoidBlock(CBD):
			def __init__(self, block_name):
				super().__init__(block_name, input_ports=['IC', 'delta_t', 'IN1'], output_ports=['OUT1'])

				# Create the Blocks
				self.addBlock(DelayBlock("xqcI94YeRySnhTKOGUdH-193"))
				self.addBlock(ProductBlock("xqcI94YeRySnhTKOGUdH-199"))
				self.addBlock(ConstantBlock("xqcI94YeRySnhTKOGUdH-204", value=(0.5)))
				self.addBlock(AdderBlock("xqcI94YeRySnhTKOGUdH-207"))
				self.addBlock(ProductBlock("xqcI94YeRySnhTKOGUdH-213"))

				# Create the Connections
				self.addConnection("IC", "xqcI94YeRySnhTKOGUdH-193", input_port_name='IC')
				self.addConnection("IN1", "xqcI94YeRySnhTKOGUdH-193", input_port_name='IN1')
				self.addConnection("IN1", "xqcI94YeRySnhTKOGUdH-207", input_port_name='IN1')
				self.addConnection("delta_t", "xqcI94YeRySnhTKOGUdH-199", input_port_name='IN1')
				self.addConnection("xqcI94YeRySnhTKOGUdH-204", "xqcI94YeRySnhTKOGUdH-199", output_port_name='OUT1',
								   input_port_name='IN2')
				self.addConnection("xqcI94YeRySnhTKOGUdH-193", "xqcI94YeRySnhTKOGUdH-207", output_port_name='OUT1',
								   input_port_name='IN2')
				self.addConnection("xqcI94YeRySnhTKOGUdH-207", "xqcI94YeRySnhTKOGUdH-213", output_port_name='OUT1',
								   input_port_name='IN1')
				self.addConnection("xqcI94YeRySnhTKOGUdH-199", "xqcI94YeRySnhTKOGUdH-213", output_port_name='OUT1',
								   input_port_name='IN2')
				self.addConnection("xqcI94YeRySnhTKOGUdH-213", "OUT1", output_port_name='OUT1')

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
		self.addConnection("IC", "xqcI94YeRySnhTKOGUdH-231", input_port_name='IN2')
		self.addConnection("IN1", "simpson", input_port_name='IN1')
		self.addConnection("IN1", "trapezoid", input_port_name='IN1')
		self.addConnection("delta_t", "simpson", input_port_name='delta_t')
		self.addConnection("delta_t", "trapezoid", input_port_name='delta_t')
		self.addConnection("xqcI94YeRySnhTKOGUdH-17", "xqcI94YeRySnhTKOGUdH-25", output_port_name='OUT1',
						   input_port_name='IN1')
		self.addConnection("xqcI94YeRySnhTKOGUdH-29", "xqcI94YeRySnhTKOGUdH-25", output_port_name='OUT1',
						   input_port_name='IN2')
		self.addConnection("xqcI94YeRySnhTKOGUdH-29", "xqcI94YeRySnhTKOGUdH-225", output_port_name='OUT1',
						   input_port_name='IN1')
		self.addConnection("xqcI94YeRySnhTKOGUdH-29", "LFYGzvRloyAe_HxOVc6M-5", output_port_name='OUT1',
						   input_port_name='IC')
		self.addConnection("xqcI94YeRySnhTKOGUdH-25", "xqcI94YeRySnhTKOGUdH-33", output_port_name='OUT1',
						   input_port_name='select')
		self.addConnection("xqcI94YeRySnhTKOGUdH-25", "xqcI94YeRySnhTKOGUdH-83", output_port_name='OUT1',
						   input_port_name='select')
		self.addConnection("xqcI94YeRySnhTKOGUdH-65", "OUT1", output_port_name='OUT1')
		self.addConnection("xqcI94YeRySnhTKOGUdH-65", "xqcI94YeRySnhTKOGUdH-83", output_port_name='OUT1',
						   input_port_name='IN2')
		self.addConnection("xqcI94YeRySnhTKOGUdH-83", "xqcI94YeRySnhTKOGUdH-71", output_port_name='OUT1',
						   input_port_name='IN1')
		self.addConnection("xqcI94YeRySnhTKOGUdH-71", "xqcI94YeRySnhTKOGUdH-83", output_port_name='OUT1',
						   input_port_name='IN1')
		self.addConnection("xqcI94YeRySnhTKOGUdH-71", "xqcI94YeRySnhTKOGUdH-65", output_port_name='OUT1',
						   input_port_name='IN1')
		self.addConnection("xqcI94YeRySnhTKOGUdH-91", "xqcI94YeRySnhTKOGUdH-71", output_port_name='OUT1',
						   input_port_name='IC')
		self.addConnection("trapezoid", "xqcI94YeRySnhTKOGUdH-33", output_port_name='OUT1', input_port_name='IN1')
		self.addConnection("simpson", "xqcI94YeRySnhTKOGUdH-33", output_port_name='OUT1', input_port_name='IN2')
		self.addConnection("xqcI94YeRySnhTKOGUdH-33", "xqcI94YeRySnhTKOGUdH-231", output_port_name='OUT1',
						   input_port_name='IN1')
		self.addConnection("xqcI94YeRySnhTKOGUdH-231", "xqcI94YeRySnhTKOGUdH-65", output_port_name='OUT1',
						   input_port_name='IN2')
		self.addConnection("xqcI94YeRySnhTKOGUdH-225", "xqcI94YeRySnhTKOGUdH-231", output_port_name='OUT1',
						   input_port_name='select')
		self.addConnection("xqcI94YeRySnhTKOGUdH-21", "xqcI94YeRySnhTKOGUdH-17", output_port_name='OUT1',
						   input_port_name='IN2')
		self.addConnection("LFYGzvRloyAe_HxOVc6M-1", "LFYGzvRloyAe_HxOVc6M-5", output_port_name='OUT1',
						   input_port_name='IN1')
		self.addConnection("LFYGzvRloyAe_HxOVc6M-5", "LFYGzvRloyAe_HxOVc6M-1", output_port_name='OUT1',
						   input_port_name='IN1')
		self.addConnection("LFYGzvRloyAe_HxOVc6M-5", "xqcI94YeRySnhTKOGUdH-225", output_port_name='OUT1',
						   input_port_name='IN2')
		self.addConnection("LFYGzvRloyAe_HxOVc6M-5", "xqcI94YeRySnhTKOGUdH-17", output_port_name='OUT1',
						   input_port_name='IN1')



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

	def __init__(self, block_name, method="forward_euler"):
		CBD.__init__(self, block_name, ["IN1", "delta_t", "IC"], ["OUT1"])
		getattr(self, method)()


class Clock(CBD):
	"""
	System clock. **Must be present in a simulation model.**

	Args:
		block_name (str):   The name of the block.
		start_time (float): Time at which the simulation starts. Defaults to 0.

	:Input Ports:
		- :code:`h`: The delta in-between timesteps. For fixed-rate simulations,
		  this must be linked up to a constant value (e.g. a :class:`ConstantBlock`).

	:Output Ports:
		- :code:`time`: The current simulation time.
		- :code:`rel_time`: The relative simulation time, ignoring the start time.
	"""
	def __init__(self, block_name, start_time=0.0):
		CBD.__init__(self, block_name, ["h"], ["time", "rel_time", "delta"])
		self.__start_time = start_time

		self.addBlock(ConstantBlock("IC", start_time))
		self.addBlock(DelayBlock("delay"))
		self.addBlock(AdderBlock("TSum"))
		self.addBlock(AdderBlock("STSum"))
		self.addBlock(NegatorBlock("STNeg"))
		self.addBlock(ConstantBlock("Past", 0.0))
		self.addBlock(AdderBlock("PastSum"))

		self.addConnection("h", "TSum")
		self.addConnection("delay", "TSum")
		self.addConnection("TSum", "delay", input_port_name='IN1')
		self.addConnection("delay", "PastSum")
		self.addConnection("Past", "PastSum")
		self.addConnection("PastSum", "time")

		self.addConnection("IC", "delay", input_port_name='IC')

		self.addConnection("IC", "STNeg")
		self.addConnection("PastSum", "STSum")
		self.addConnection("STNeg", "STSum")
		self.addConnection("STSum", "rel_time")

		self.addConnection("h", "delta")

	def getTime(self, curIt):
		"""
		Gets the current time of the clock.
		"""
		sig = self.getBlockByName("TSum").getSignal("OUT1")
		if curIt == 0 or len(sig) == 0:
			return self.__start_time
		return sig[curIt - 1].value

	def getRelativeTime(self, curIt):
		"""
		Gets the relative simulation time (ignoring the start time).
		"""
		return self.getTime(curIt) - self.__start_time

	def setStartTime(self, start_time=0.0):
		self.__start_time = start_time
		self.getBlockByName("IC").setValue(start_time)

	def _rewind(self):
		CBD._rewind(self)
		time = self.getInputSignal(-1, "h").value
		c = self.getBlockByName("Past")
		c.setValue(c.getValue() - time)


class TimeBlock(BaseBlock):
	"""
	Obtains the current time of the simulation.

	Args:
		block_name (str):   The name of the block.

	Note:
		When manipulating and reading time values, it may be better to use the
		:class:`Clock` instead.
	"""
	def __init__(self, block_name):
		BaseBlock.__init__(self, block_name, [], ["OUT1", "relative"])

	def compute(self, curIteration):
		time = self.getClock().getTime(curIteration)
		rel_time = self.getClock().getRelativeTime(curIteration)
		self.appendToSignal(time)
		self.appendToSignal(rel_time, "relative")
