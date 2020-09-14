import random
from Unit import Unit

def RapidStrike(caster, target, procChance):
    """RapidStrike gives the caster a chance to attack a second time.
    Cannot proc off itself.

    Parameters
    ----------
    target: Unit
        The unit which this unit will attack.
    procChance: float
        The chance for the ability to proc (5 = 5%).

    Raises
    ------
    TypeError
        If there are more or less than two parameters passed.
        If caster does not inherit from Unit.
        If target does not inherit from the Unit.
        If caster==target.
        If procChance is not a number
    """

    if len(locals()) != 3:
        raise TypeError("Hero.RapidStrike(target, procChance) takes two parameters")
    if not issubclass(type(caster), Unit):
        raise TypeError("Target must inherit from class Unit")
    if not issubclass(type(target), Unit):
        raise TypeError("Target must inherit from class Unit")
    if caster is target:
        raise TypeError("Caster cannot target itself")
    if type(procChance) is not float and type(procChance) is not int:
        raise TypeError("procChance must be a number")

    if random.random() <= float(procChance) / 100.0:
        print("{0} uses Rapid Strikes, attacking {1} again!".format(caster.name, target.name))
        target.CalculateDamageTaken(caster.strength)


def MagicShield(caster, incomingDamage, procChance):
        """MagicShield gives the caster a chance to reduce damage recevied by half.

        Parameters
        ----------
        incomingDamage: int
            Amount of incoming damage
        procChance: float
            The chance for the ability to proc (5 = 5%).

        Raises
        ------
        TypeError
            If there are more or less than two parameters passed.
            If caster does not inherit from Unit.
            If incomingDamage is not an int.
            If procChance is not a number.

        Return
        ------
        Int
           Returns the amount of damage the Hero will take, affected by the
           damage reduction if it procs.
        """

        if len(locals()) != 3:
            raise TypeError("Hero.MagicShield(incomingDamage, procChance) takes two parameters")
        if not issubclass(type(caster), Unit):
            raise TypeError("Caster must inherit from class Unit")
        if type(incomingDamage) is not int:
            raise TypeError("incomingDamage must be of type int")
        if type(procChance) is not float and type(procChance) is not int:
            raise TypeError("procChance must be a number")

        if random.random() <= float(procChance) / 100.0:
            print("{} uses Magic Shield, reducing damage taken in half!".format(caster.name))
            incomingDamage = incomingDamage // 2
        if incomingDamage < 0:
            incomingDamage = 0
        return incomingDamage