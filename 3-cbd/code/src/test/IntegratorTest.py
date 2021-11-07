import unittest

from CBD.Core import *
from CBD.lib.std import *
from CBD.simulator import Simulator

NUM_DISCR_TIME_STEPS = 5


class IntegratorTestCase(unittest.TestCase):
    def setUp(self):
        self.CBD = CBD("CBD_for_block_under_test")
        self.sim = Simulator(self.CBD)

    def _run(self, num_steps=1, delta_t=1.0):
        self.sim.setDeltaT(delta_t)
        self.sim.setTerminationTime(num_steps * delta_t)
        self.sim.setVerbose()
        self.sim.run()

    def _getSignal(self, blockname, output_port=None):
        foundBlocks = [block for block in self.CBD.getBlocks() if
                       block.getBlockName() == blockname]
        numFoundBlocks = len(foundBlocks)
        if numFoundBlocks == 1:
            signal = foundBlocks[0].getSignal(name_output=output_port)
            return [x.value for x in signal]
        else:
            raise Exception(
                str(numFoundBlocks) + " blocks with name " + blockname + " found.\nExpected a single block.")

    def testIntegratorBlock(self):
        # Function: f(t) = 6 + f(t - dt), where f(0) = 6
        dt = 0.0001
        epsilon = 0.002
        self.CBD.addBlock(ConstantBlock(block_name="c1", value=6.0))
        self.CBD.addBlock(ConstantBlock(block_name="c2", value=0.0))
        self.CBD.addBlock(ConstantBlock(block_name="c3", value=dt))
        self.CBD.addBlock(AdderBlock(block_name="a"))
        self.CBD.addBlock(DelayBlock(block_name="d"))

        self.CBD.addBlock(IntegratorBlock(block_name="int"))
        self.CBD.addConnection("c3", "int", input_port_name="delta_t")
        self.CBD.addConnection("a", "int")
        self.CBD.addConnection("c2", "int", input_port_name="IC")

        self.CBD.addConnection("c1", "a")
        self.CBD.addConnection("d", "a")
        self.CBD.addConnection("a", "d")
        self.CBD.addConnection("c2", "d", input_port_name="IC")
        self._run(NUM_DISCR_TIME_STEPS, dt)
        actual = [x * dt for x in [0.0, 9.0, 24.0, 45.0, 72.0]]
        measured = self._getSignal("int")
        error = [abs(measured[i] - actual[i]) for i in
                 range(NUM_DISCR_TIME_STEPS)]
        self.assertFalse(any([x > epsilon for x in error]),
                         "Error too large.\n\tExpected: {}\n\tActual: {}"
                         "\n\tErrors: {}".format(actual, measured, error))
