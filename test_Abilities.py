import unittest
from Abilities import *
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


class TestArena(unittest.TestCase):
    def test_RapidStrike(self):
        self.assertRaises(TypeError, RapidStrike, testUnit, testUnit2, "20")
        self.assertRaises(TypeError, RapidStrike, testUnit, testUnit2, True)
        self.assertRaises(TypeError, RapidStrike, testUnit, testUnit2, 20j)
        self.assertRaises(TypeError, RapidStrike, testUnit, Hero, 20)
        self.assertRaises(TypeError, RapidStrike, testUnit, testUnit, 20)
        self.assertRaises(TypeError, RapidStrike, Hero, testUnit2, 20)
        self.assertRaises(TypeError, RapidStrike, testUnit, testUnit2)
        self.assertRaises(TypeError, RapidStrike, testUnit, testUnit2, 20, None)

    def test_MagicArmor(self):
        self.assertEqual(MagicShield(testUnit, 30, 100), 15)
        self.assertEqual(MagicShield(testUnit, 30, 0), 30)

        self.assertRaises(TypeError, MagicShield, testUnit, 30, "20")
        self.assertRaises(TypeError, MagicShield, testUnit, True, 20)
        self.assertRaises(TypeError, MagicShield, Hero, 30, 20)
        self.assertRaises(TypeError, MagicShield, testUnit, 30, 20, None)
        self.assertRaises(TypeError, MagicShield, testUnit, 30)