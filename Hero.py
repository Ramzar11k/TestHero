from Unit import Unit
import random


class Hero(Unit):
    """
    Hero is a class that inherits from Unit.
    It gain the abilities RapidStrike and MagicShield.

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
    RapidStrike(target, procChance)
        Has a chance to attack a second time
    MagicShield(incomingDamage, procChance)
        Has a chance to reduce incoming damage in half
    Defeat()
        Runs when the unit is defeated (health <= 0)
    """

    def Attack(self, target):
        """Tells the hero unit which unit to attack

        Parameters
        ----------
        target: Unit
            The unit which this unit will attack

        Raises
        ------
        TypeError
            If there is not one parameter passed
            If the selected target does not inherit from the Unit class
        """

        super().Attack(target=target)
        print("{0} attacks {1}".format(self.name, target.name))
        target.CalculateDamageTaken(attackerStrength=self.strength)
        self.RapidStrike(target=target, procChance=10)

    def CalculateDamageTaken(self, attackerStrength):
        """Calculates the damage this unit will take
        Damage is calculated by : damage = AttackerStrength - DefenderDefence

        Parameters
        ----------
        attackerStrength: int
            The strength of the attacking unit
            Value must be non negative

        Raises
        ------
        ValueError
            If the value of attackerStrength is negative
        TypeError
            If there is not one parameter passed
            If attackerStrength is not an int
        """

        super().CalculateDamageTaken(attackerStrength)
        damageTaken = max(attackerStrength - self.defence, 0)
        damageTaken = self.MagicShield(damageTaken, 20)
        self.TakeDamage(damage=damageTaken)

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
            If the value of damage is negative
        TypeError
            If there is not one parameter passed
            If damage is not an int
        """

        super().TakeDamage(damage)
        if random.randint(0, 100) <= self.luck:
            print("{} gets lucky and avoids the attack".format(self.name))
            return
        self.health -= damage
        print("{0} took {1} damage, and has {2} health remaining".format(self.name, damage, self.health))

    def RapidStrike(self, target, procChance):
        """RapidStrike gives the user a chance to attack a second time.
        Whenever the user attacks there is a chance to proc this.
        Cannot proc of itself.

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
            If the selected target does not inherit from the Unit class.
            If procChance is not a number
        """

        if len(locals()) != 3:
            raise TypeError("Hero.RapidStrike(target, procChance) takes two parameters")
        if not issubclass(type(target), Unit):
            raise TypeError("Target must inherit from class Unit")
        if type(procChance) is not float and type(procChance) is not int:
            raise TypeError("procChance must be a number")

        if random.random() <= float(procChance) / 100.0:
            print("{0} uses Rapid Strikes, attacking {1} again!".format(self.name, target.name))
            target.CalculateDamageTaken(self.strength)

    def MagicShield(self, incomingDamage, procChance):
        """MagicShield gives the hero a chance to reduce damage recevied by half.
        Whenever the user is attacked there is a chance to proc this.

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
            If incomingDamage is not an int
            If procChance is not a number

        Return
        ------
        Int
           Returns the amount of damage the Hero will take, affected by the
           damage reduction if it procs.
        """

        if len(locals()) != 3:
            raise TypeError("Hero.MagicShield(incomingDamage, procChance) takes two parameters")
        if type(incomingDamage) is not int:
            raise TypeError("incomingDamage must be of type int")
        if type(procChance) is not float and type(procChance) is not int:
            raise TypeError("procChance must be a number")

        if random.random() <= float(procChance) / 100.0:
            print("{} uses Magic Shield, reducing damage taken in half!".format(self.name))
            incomingDamage = incomingDamage // 2
        if incomingDamage < 0:
            incomingDamage = 0
        return incomingDamage