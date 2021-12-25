import logging
import random

from tests.generator_collector_test import GeneratorCollectorTest
from tests.junction_test import JunctionTest
from tests.rail_test import RailTest
from tests.split_test import SplitTest
from tests.station_test import StationTest

from pypdevs.simulator import Simulator


def station_test(time: int):
    model = StationTest()

    setting_up_and_run_sim(time, model)

    trollies = model.collector.state["trollies"]
    print("Arrived trollies: ", len(trollies))
    print("Info about trollies: ", end="[")
    for trolley in trollies:
        print(f"({trolley[1].name}, {trolley[0]})", end=", ")
    print("]")
    print("Amount of passengers on trolley 1: ", len(trollies[0][1].passengers))
    print("Amount of passengers on trolley 2: ", len(trollies[1][1].passengers))

    print("Info passengers on trolley 1: ", end="[")
    for passenger in trollies[0][1].passengers:
        print("(", passenger.used_trolley, ",", passenger.departed_at, ")", end=", ")
    print("]")
    print("Info passengers on trolley 2: ", end="[")
    for passenger in trollies[1][1].passengers:
        print("(", passenger.used_trolley, ",", passenger.departed_at, ")", end=", ")
    print("]")


def split_test(time: int):
    model = SplitTest()

    setting_up_and_run_sim(time, model)

    print("Amount trollies arrived collector 1: ",
          len(model.collector_one.state["trollies"]))
    print("Amount trollies arrived collector 2: ",
          len(model.collector_two.state["trollies"]))
    print("Name trollies collector 1: ",
          model.collector_one.state["trollies"][0][1].name)
    print("Name trollies collector 2: ",
          model.collector_two.state["trollies"][0][1].name)
    print("Arrived at collector 1: ",
          model.collector_one.state["trollies"][0][0])
    print("Arrived at collector 2: ",
          model.collector_two.state["trollies"][0][0])


def rail_test(time: int):
    model = RailTest()

    setting_up_and_run_sim(time, model)

    print("Amount arrived trollies: ", len(model.collector.state["trollies"]))
    print("Arrived trolley times: [", end="[")
    for trolley in model.collector.state["trollies"]:
        print(trolley[0], end=", ")
    print("]")
    print("Trolley names: [", end="")
    for trolley in model.collector.state["trollies"]:
        print(trolley[1].name, end=", ")
    print("]")


def junction_test(time: int):
    model = JunctionTest()

    setting_up_and_run_sim(time, model)

    print("Amount: ", len(model.collector.state["trollies"]))
    print("Arrived at: [", end="")
    for trolley in model.collector.state["trollies"]:
        print(trolley[0], end=", ")
    print("]")
    print("Trolley names: [", end="")
    for trolley in model.collector.state["trollies"]:
        print(trolley[1].name, end=", ")
    print("]")


def generator_collector_test(time: int):
    model = GeneratorCollectorTest()

    setting_up_and_run_sim(time, model)

    print("Amount: ", len(model.collector.state["passengers"]))
    print("Departed from: ", model.collector.state["passengers"][0].origin)
    print("Destination: ", model.collector.state["passengers"][0].destination)
    print("Time generated: ", model.collector.state["passengers"][0].arrived_at)


def setting_up_and_run_sim(time: int, model):
    # Set up the Simulator
    sim = Simulator(model)
    # sim.setVerbose(None)
    sim.setClassicDEVS()  # IMPORTANT!! Ensures the usage of the Classic DEVS formalism
    sim.setTerminationTime(time)
    logging.debug("GENERAL: starting the simulation")
    sim.simulate()
    logging.debug("GENERAL: finishing the simulation")


if __name__ == '__main__':
    # set the logging defaults
    logging.basicConfig(level=logging.DEBUG,
                        format="%(levelname)s - %(message)s")
    # fix the seed
    seed = 123
    random.seed(seed)

    # Create and run the test
    station_test(240)
    # split_test(20)
    # rail_test(175)
    # junction_test(30)
    # generator_collector_test(100)

    # network = Network(path="networks/city.json")
