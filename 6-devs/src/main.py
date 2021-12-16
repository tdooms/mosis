from models.network import Network
from pypdevs.simulator import Simulator

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

    network = Network(path="networks/city.json")
    network.visualise("img/main.svg")
