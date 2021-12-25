from pypdevs.DEVS import CoupledDEVS

from models.collector import Collector
from models.generator import Generator


class PlatformTest(CoupledDEVS):
    def __init__(self):
        super().__init__("PlatformTest")

        self.generator = self.addSubModel(Generator(origin="main", destinations=["main"], lines={"main": ["main"]}, mu=100, sigma=0))
        self.collector = self.addSubModel(Collector(origin="main"))

        self.connectPorts(self.generator.out_port, self.collector.in_port)

