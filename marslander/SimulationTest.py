import unittest
import random

from Simulation import Simulation

from Vehicle import Vehicle
from BurnDataStream import BurnDataStream
from OnBoardComputer import OnBoardComputer
from DescentEvent import DescentEvent
from BurnInputStream import BurnInputStream

class SimulationTest(unittest.TestCase):

    def test_runSimulationLanding(self):
        burns = [200, 200, 200, 200, 200, 200, 200, 200, 200,
                 100, 100, 100, 100,
                 150, 125, 120, 100, 100, 100, 103,
                 100, 100, 100, 100]
        print("\n*** Data Stream\n\n")
        burnSource = BurnDataStream(burns)
        game = Simulation(Vehicle(5000))
        result = game.run_simulation(burnSource)
        self.assertEqual(result, Vehicle.SUCCESS)

    def test_runSimulationCrash(self):
        burns = [0, 0, 0, 0, 0]
        print("\n*** Data Stream\n\n")
        burnSource = BurnDataStream(burns)
        game = Simulation(Vehicle(5000))
        result = game.run_simulation(burnSource)
        self.assertEqual(result, Vehicle.DEAD)

    def test_runSimulationComputer(self):
        burnSource = OnBoardComputer()
        print("\n*** onboard Stream 10000\n\n")
        game = Simulation(Vehicle(10000))
        result = game.run_simulation(burnSource)
        self.assertEqual(result, Vehicle.SUCCESS)

    def test_runSimulationComputerRandom(self):
        burnSource = OnBoardComputer()
        print("\n*** onboard Stream (random altitude)\n\n")
        game = Simulation(Vehicle(Simulation.random_altitude()))
        result = game.run_simulation(burnSource)
        self.assertEqual(result, Vehicle.SUCCESS)

    def test_runSimulationComputer4000(self):
        burnSource = OnBoardComputer()
        print("\n*** onboard Stream 10000\n\n")
        game = Simulation(Vehicle(4500))
        result = game.run_simulation(burnSource)
        self.assertEqual(result, Vehicle.SUCCESS)

if __name__ == '__main__':
    unittest.main()