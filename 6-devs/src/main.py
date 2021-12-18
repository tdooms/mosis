from models.network import Network
from pypdevs.simulator import Simulator

from tests.station_test import StationTest


def print_stats(stats):
    print("1. Average travel time of a passenger: ", stats[0])
    print("2. For each trolley, a summarized overview of trolley capacity over time: ", stats[1])
    print("3. For each trolley, the time-average trolley capacity: ", stats[2])
    print("4. For each station, the amount of people that have exited at that station: ", stats[3])
    print("5. For each station, the amount of people that have exited at their desired destination: ", stats[4])
    print("6. For each station, the average travel time of people that have exited at that station: ", stats[5])
    print("7. Total amount of people that have traveled over the PRT: ", stats[6])
    print("8. Number of people that have successfully arrived at their desired destination: ", stats[7])
    print("9. Number of people still commuting when the experiment terminates: ", stats[8])
    print("10. Number of people with a destination that equals their origin station: ", stats[9])


if __name__ == '__main__':
    TIME = 500
    # Create the model
    model = Network("networks/simple.json", TIME, 50, 5)
    # model = StationTest()

    # Set up the Simulator
    sim = Simulator(model)
    # sim.setVerbose(None)
    sim.setClassicDEVS()         # IMPORTANT!! Ensures the usage of the Classic DEVS formalism
    sim.setTerminationTime(TIME)
    sim.simulate()

    print('\n\n\n\n\n\n\n\n\n')

    print_stats(model.statistics())

    # network = Network(path="networks/city.json")
    # network.visualise("img/main.svg")
