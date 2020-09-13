import unittest
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
    def test_rapidStrikes(self):
        self.assertRaises(TypeError, Hero.RapidStrike, testUnit, testUnit, "20")
        self.assertRaises(TypeError, Hero.RapidStrike, testUnit, testUnit, True)
        self.assertRaises(TypeError, Hero.RapidStrike, testUnit, testUnit2, 20j)
        self.assertRaises(TypeError, Hero.RapidStrike, testUnit, Hero, 20)
        self.assertRaises(TypeError, Hero.RapidStrike, testUnit, testUnit2)
        self.assertRaises(TypeError, Hero.RapidStrike, testUnit, testUnit2, 20, None)

    def test_magicShield(self):
        self.assertEqual(Hero.MagicShield(testUnit, 30, 100), 15)

        self.assertRaises(TypeError, Hero.MagicShield, testUnit, 30, "20")
        self.assertRaises(TypeError, Hero.MagicShield, testUnit, True, 20)
        self.assertRaises(TypeError, Hero.MagicShield, testUnit, 30, 20, None)
        self.assertRaises(TypeError, Hero.MagicShield, testUnit, 30)
