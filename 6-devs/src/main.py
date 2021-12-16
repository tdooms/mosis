from models.network import Network
from pypdevs.simulator import Simulator

from tests.station_test import StationTest

if __name__ == '__main__':
    # Create the model
    model = Network("networks/simple.json")
    # model = StationTest()

    # Set up the Simulator
    sim = Simulator(model)
    # sim.setVerbose(None)
    sim.setClassicDEVS()         # IMPORTANT!! Ensures the usage of the Classic DEVS formalism
    sim.setTerminationTime(500)  # Simulate until time = K
    sim.simulate()

    model.statistics()

    # network = Network(path="networks/city.json")
    # network.visualise("img/main.svg")
