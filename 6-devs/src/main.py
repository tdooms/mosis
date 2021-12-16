from models.network import Network
from parse import parse_network
from tests.generator_collector_test import GeneratorCollectorTest
from pypdevs.simulator import Simulator
from tests.junction_test import JunctionTest
from tests.rail_test import RailTest
from tests.station_test import StationTest

if __name__ == '__main__':
    # # Create the model
    # # model = Generator(origin=0, destinations=[0, 1, 2])
    # # model = Collector(origin=0)
    # model = StationTest()
    #
    # # Set up the Simulator
    # sim = Simulator(model)
    # # sim.setVerbose(None)
    # sim.setClassicDEVS()         # IMPORTANT!! Ensures the usage of the Classic DEVS formalism
    # sim.setTerminationTime(300)  # Simulate until time = 500
    # sim.simulate()

    network = Network(path="networks/simple.json")
    network.visualise("img/main.png")
