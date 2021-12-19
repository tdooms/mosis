import logging
import random

import numpy as np
from pypdevs.simulator import Simulator

from models.network import Network
import matplotlib.pyplot as plt


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


def plot_statistics(stats):
    def reset_plot():
        plt.clf()
        plt.cla()
        plt.close()

    # Exited stats
    x = stats[3].keys()
    x_axis = np.arange(len(x))

    plt.barh(x_axis - 0.2, stats[3].values(), 0.4, label='Exited somewhere')
    plt.barh(x_axis + 0.2, stats[4].values(), 0.4, label='Exited at destination')

    plt.yticks(x_axis, x)
    plt.xlabel("Number of Passengers")
    plt.title(f"Amount of people using the PRT: {stats[6]}\nAmount of people at their desired station: {stats[7]}")
    plt.tight_layout()
    plt.legend()
    plt.savefig('img/stats/exited.png')

    reset_plot()

    # Avg time stats
    plt.barh(list(stats[5].keys()), list(stats[5].values()))
    plt.ylabel("Number of Passengers")
    plt.title(f"Average travel time of people; {stats[0]:.2f}")
    plt.tight_layout()
    plt.legend()
    plt.savefig('img/stats/avg.png')

    reset_plot()

    for trolley, values in stats[1].items():
        plt.plot(list(range(len(values))), values, linestyle='-', label=f"{trolley}, avg: {stats[2][trolley]:.2f}")
    plt.ylabel("Passengers in trolley")
    plt.title("trolley capacities over time")
    plt.legend()
    plt.savefig('img/stats/fullness.png')


if __name__ == '__main__':
    # set the logging defaults
    logging.basicConfig(format="%(levelname)s - %(message)s")
    # fix the seed
    random.seed(123)

    TIME = 60 * 60 * 4

    # Create the model
    model = Network("networks/city.json", TIME, 8640, 24)
    model.visualise("img/main.svg")
    # model = StationTest()

    # Set up the Simulator
    sim = Simulator(model)
    # sim.setVerbose(None)
    sim.setClassicDEVS()         # IMPORTANT!! Ensures the usage of the Classic DEVS formalism
    sim.setTerminationTime(TIME)
    logging.debug("GENERAL: starting the simulation")
    sim.simulate()
    logging.debug("GENERAL: finishing the simulation")

    stats = model.statistics()
    print_stats(stats)
    plot_statistics(stats)

    # network = Network(path="networks/city.json")
