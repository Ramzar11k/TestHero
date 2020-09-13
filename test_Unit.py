import unittest
from Unit import Unit
from Hero import Hero

testUnit = Hero(name="Ordeus",
              healthRange=(70, 80),
              strengthRange=(70, 80),
              defenceRange=(45, 55),
              speedRange=(40, 50),
              luckRange=(10, 30))


class TestUnit(unittest.TestCase):
    def test_type(self):
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, 2)
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, "Orderus", (70, 80), (70, 80), (45, 55), "Hello", (10, 30))
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, "Orderus", [70, 80], (70, 80), (45, 55), (45, 55), (10, 30))
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, "Orderus", (70, 80), (70, 80), (45, 55), 5)
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, "Orderus", (70, 80), (70, 80), (45, 55), (40, 50))
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, "Orderus", (70, 80), (70, 80), (45, 55), (40, 50), (10, 30), (20, 20))
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, 32, (70, 80), (70, 80), (45, 55), (40, 50), (10, 30))
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, True, (70, 80), (70, 80), (45, 55), (40, 50), (10, 30))
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, None, (70, 80), (70, 80), (45, 55), (40, 50), (10, 30))
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, "Orderus", (70, 80), ("Orderus", 80), (45, 55), (40, 50), (10, 30))
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, "Orderus", (70, 80), (80, 80.0), (45, 55), (40, 50), (10, 30))
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, "Orderus", (70, 80), (80, None), (45, 55), (40, 50), (10, 30))
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, "Orderus", (70, 80), (80, 90), (45, 55), (40, 50), None)
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, "Orderus", (70, 80), (80, 80.0), (45, 55), (40, 50), 4)
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, "Orderus", (70, 80), (80, 80.0), (45, 55), (40, 50), (True, False))
        self.assertRaises(TypeError, Unit.ValidateInputs, testUnit, "Orderus", (70, 80), (80j, 80), (45, 55), (40, 50), (10, 30))

    def test_value(self):
        self.assertRaises(ValueError, Unit.ValidateInputs, testUnit, "Orderus", (70, 80, 4), (80, 80), (45, 55), (40, 50), (10, 30))
        self.assertRaises(ValueError, Unit.ValidateInputs, testUnit, "Orderus", (-70, 80), (80, 80), (45, 55), (40, 50), (10, 30))
        self.assertRaises(ValueError, Unit.ValidateInputs, testUnit, "Orderus", (70, 80), (-10, -5), (45, 55), (40, 50), (10, 30))
        self.assertRaises(ValueError, Unit.ValidateInputs, testUnit, "Orderus", (70, 60), (10, 5), (45, 55), (40, 50), (10, 30))
        self.assertRaises(ValueError, Unit.ValidateInputs, testUnit, "Orderus", (70, -60), (10, 5), (45, 55), (40, 50), (10, 30))
        self.assertRaises(ValueError, Unit.ValidateInputs, testUnit, "Orderus", (-50, -60), (10, 5), (45, 55), (40, 50), (10, 30))

    def test_attack(self):
        self.assertRaises(TypeError, Unit.Attack, testUnit, None)
        self.assertRaises(TypeError, Unit.Attack, testUnit, testUnit, True)
        self.assertRaises(TypeError, Unit.Attack, testUnit, 12)
        self.assertRaises(TypeError, Unit.Attack, testUnit, 13.3)
        self.assertRaises(TypeError, Unit.Attack, testUnit, Unit)
        self.assertRaises(TypeError, Unit.Attack, testUnit, True)
        self.assertRaises(TypeError, Unit.Attack, testUnit, (12, -3j))

    def test_calculateDamageTaken(self):
        self.assertRaises(TypeError, Unit.CalculateDamageTaken, testUnit, 20.0)
        self.assertRaises(TypeError, Unit.CalculateDamageTaken, testUnit, True)
        self.assertRaises(TypeError, Unit.CalculateDamageTaken, testUnit, str)
        self.assertRaises(TypeError, Unit.CalculateDamageTaken, testUnit, "Hi")
        self.assertRaises(TypeError, Unit.CalculateDamageTaken, testUnit)

        self.assertRaises(ValueError, Unit.CalculateDamageTaken, testUnit, -10)

    def test_takeDamage(self):
        self.assertRaises(TypeError, Unit.TakeDamage, testUnit, 20.0)
        self.assertRaises(TypeError, Unit.TakeDamage, testUnit, True)
        self.assertRaises(TypeError, Unit.TakeDamage, testUnit, str)
        self.assertRaises(TypeError, Unit.TakeDamage, testUnit, "Hi")
        self.assertRaises(TypeError, Unit.TakeDamage, testUnit)

        self.assertRaises(ValueError, Unit.TakeDamage, testUnit, -10)