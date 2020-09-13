import unittest
from Arena import Arena
from Hero import Hero
from Beast import Beast

testUnit = Hero(name="Ordeus",
              healthRange=(70, 80),
              strengthRange=(70, 80),
              defenceRange=(45, 55),
              speedRange=(40, 50),
              luckRange=(10, 30))
testUnit2 = Beast(name="Beast",
              healthRange=(60, 90),
              strengthRange=(60, 90),
              defenceRange=(40, 60),
              speedRange=(40, 60),
              luckRange=(25, 40))

testArena = Arena(name="Emagia", fighter1=testUnit, fighter2=testUnit2, maxTurns=20)


class TestArena(unittest.TestCase):
    def test_type(self):
        self.assertRaises(TypeError, Arena.ValidateInputs, testArena)
        self.assertRaises(TypeError, Arena.ValidateInputs, testArena, True, testUnit, testUnit2, 20)
        self.assertRaises(TypeError, Arena.ValidateInputs, testArena, 12, testUnit, testUnit2, 20)
        self.assertRaises(TypeError, Arena.ValidateInputs, testArena, "Orderus", testUnit, testUnit2, "20")
        self.assertRaises(TypeError, Arena.ValidateInputs, testArena, "Orderus", testUnit, testUnit2, 20.0)
        self.assertRaises(TypeError, Arena.ValidateInputs, testArena, "Orderus", True, testUnit2, 20)
        self.assertRaises(TypeError, Arena.ValidateInputs, testArena, "Orderus", testUnit, testUnit, 20)
        self.assertRaises(TypeError, Arena.ValidateInputs, testArena, "Orderus", testUnit, testUnit2, 20, None)
        self.assertRaises(TypeError, Arena.ValidateInputs, testArena, "Orderus", testUnit, Hero, 20)

    def test_value(self):
        self.assertRaises(ValueError, Arena.ValidateInputs, testArena, "Orderus", testUnit, testUnit2, 0)
        self.assertRaises(ValueError, Arena.ValidateInputs, testArena, "Orderus", testUnit, testUnit2, -3)