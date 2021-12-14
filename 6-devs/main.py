from models.generator import Generator
from models.collector import Collector
from tests.generator_collector_test import GeneratorCollector
from pypdevs.simulator import Simulator

if __name__ == '__main__':
    # Create the model
    # model = Generator(origin=0, destinations=[0, 1, 2])
    # model = Collector(origin=0)
    model = GeneratorCollector()

    # Set up the Simulator
    sim = Simulator(model)
    sim.setClassicDEVS()         # IMPORTANT!! Ensures the usage of the Classic DEVS formalism
    sim.setTerminationTime(500)  # Simulate until time = 500
    sim.simulate()
