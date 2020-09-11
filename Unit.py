import random
from abc import ABC, abstractmethod

class Unit(ABC):
    """
    Unit is a base abstract class from which more complex units can be built,
    adding abilities and interactions.

    ...

    Attributes
    ----------
    name : str
        The name of the unit
    healthRange: tuple(minInt, maxInt)
        Range of values used to determine the units health
        Passed values must be non negative and minInt <= maxInt
    strengthRange: tuple(minInt, maxInt)
        Range of values used to determine the units strength
        Passed values must be non negative and minInt <= maxInt
    defenceRange: tuple(minInt, maxInt)
        Range of values used to determine the units defence
        Passed values must be non negative and minInt <= maxInt
    speedRange: tuple(minInt, maxInt)
        Range of values used to determine the units speed
        Passed values must be non negative and minInt <= maxInt
    luckRange: tuple(minInt, maxInt)
        Range of values used to determine the units luck
        Passed values must be non negative and minInt <= maxInt

    Methods
    -------
    PrintInfo()
        Prints the units stats to the console
    Attack(target)
        Tells the unit which unit to attack
    CalculateDamageTaken(attackerStrength)
        Calculates how much damage this unit will take from an attack
    TakeDamage(damage)
        Damages this unit
    Defeat()
        Runs when the unit is defeated (health <= 0)
    """

    def __init__(self, name, healthRange, strengthRange, defenceRange, speedRange, luckRange):
        """
        Initializes the units stats.

        Parameters
        ----------
        name : str
            The name of the unit.
        healthRange: tuple(minInt, maxInt)
            Range of values used to determine the units health.
            Passed values must be non negative and minInt <= maxInt.
        strengthRange: tuple(minInt, maxInt)
            Range of values used to determine the units strength.
            Passed values must be non negative and minInt <= maxInt.
        defenceRange: tuple(minInt, maxInt)
            Range of values used to determine the units defence.
            Passed values must be non negative and minInt <= maxInt.
        speedRange: tuple(minInt, maxInt)
            Range of values used to determine the units speed.
            Passed values must be non negative and minInt <= maxInt.
        luckRange: tuple(minInt, maxInt)
            Range of values used to determine the units luck.
            Passed values must be non negative and minInt <= maxInt.

        Raises
        ------
        TypeError
            If name is not a string.
            If any of the ranges is not a tuple.

        ValueError
            If there are not six parameters passed.
            If a range is not in the format (int, int).
            If a range value is negative.
            If a ranges minVal is bigger than its maxVal.
        """

        self.__ValidateInputs(name=name,
                              healthRange=healthRange,
                              strengthRange=strengthRange,
                              defenceRange=defenceRange,
                              speedRange=speedRange,
                              luckRange=luckRange)
        self.name = name
        self.health = random.randint(healthRange[0], healthRange[1])
        self.strength = random.randint(strengthRange[0], strengthRange[1])
        self.defence = random.randint(defenceRange[0], defenceRange[1])
        self.speed = random.randint(speedRange[0], speedRange[1])
        self.luck = random.randint(luckRange[0], luckRange[1])

    @staticmethod
    def __ValidateInputs(name, healthRange, strengthRange, defenceRange, speedRange, luckRange):
        if len(locals()) != 6:
            raise ValueError("Unit class takes six parameters")

        ranges = [(healthRange, "healthRange"),
                  (strengthRange, "strengthRange"),
                  (defenceRange, "defenceRange"),
                  (speedRange, "speedRange"),
                  (luckRange, "luckRange")]
        if type(name) is not str:
            raise TypeError("Unit name must be a string")

        for statRange in ranges:
            if type(statRange[0]) is not tuple:
                raise TypeError("{} must be a tuple".format(statRange[1]))

            if len(statRange[0]) != 2:
                raise ValueError("{} must have the format (minValue, maxValue)".format(statRange[1]))

            if type(statRange[0][0]) is not int or type(statRange[0][1]) is not int:
                raise ValueError("{} values must be (int, int)".format(statRange[1]))

            if statRange[0][0] < 0 or statRange[0][1] < 0:
                raise ValueError("{} values must be non negative".format(statRange[1]))

            if statRange[0][0] > statRange[0][1]:
                raise ValueError("{} minValue cannot be lower than maxValue (minValue, maxValue)".format(statRange[1]))

    def PrintInfo(self):
        """Prints out the units stats to the console"""
        print("Name: ", self.name,
              " Health: ", self.health,
              " Strength: ", self.strength,
              " Defence: ", self.defence,
              " Speed: ", self.speed,
              " Luck: ", self.luck)

    @abstractmethod
    def Attack(self, target):
        """Tells the unit which unit to attack

        Parameters
        ----------
        target: Unit
            The unit which this unit will attack

        Raises
        ------
        ValueError
            If there is no parameter passed
        TypeError
            If the selected target does not inherit from the Unit class
        """

        if len(locals()) != 2:
            raise ValueError("Unit.Attack(target) takes one parameter")
        if not issubclass(type(target), Unit):
            raise TypeError("Target must inherit from class Unit")

    @abstractmethod
    def CalculateDamageTaken(self, attackerStrength):
        """Calculates the damage this unit will take
        Damage is calculated by : damage = AttackerStrength - DefenderDefence

        Parameters
        ----------
        attackerStrength: int
            Amount of damage this unit will take
            Value must be non negative

        Raises
        ------
        ValueError
            If there is no parameter passed
            If the value of attackerStrength is negative
        TypeError
            If attackerStrength is not an int
        """

        if len(locals()) != 2:
            raise ValueError("Unit.CalculateDamageTaken(attackerStrength) takes one parameter")
        if type(attackerStrength) is not int:
            raise TypeError("attackerStrength must be of type int")
        if attackerStrength < 0:
            raise ValueError("attackerStrength must be non negative")

    @abstractmethod
    def TakeDamage(self, damage):
        """Damages this unit.
        Has a chance equal to this units luck to avoid damage.

        Parameters
        ----------
        damage: int
            Amount of damage this unit will take
            Value must be non negative

        Raises
        ------
        ValueError
            If there is no parameter passed
            If the value of damage is negative
        TypeError
            If damage is not an int
        """

        if len(locals()) != 2:
            raise ValueError("Unit.TakeDamage(damage) takes one parameter")
        if type(damage) is not int:
            raise TypeError("damage must be of type int")
        if damage < 0:
            raise ValueError("damage must be non negative")

    @abstractmethod
    def Defeat(self):
        print("ouch")
