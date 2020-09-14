from Unit import Unit
from Abilities import RapidStrike, MagicShield
import random


class Hero(Unit):
    """
    Hero is a class that inherits from Unit.
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
        RapidStrike(caster=self, target=target, procChance=10)

    def CalculateDamageTaken(self, attackerStrength):
        """Calculates the damage this unit will take.
        Damage is calculated by : damage = AttackerStrength - DefenderDefence
        Has a chance equal to this units luck to avoid damage.

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

        if random.randint(0, 100) <= self.luck:
            print("{} gets lucky and avoids the attack".format(self.name))
            return
        damageTaken = max(attackerStrength - self.defence, 0)
        damageTaken = MagicShield(caster=self, incomingDamage=damageTaken, procChance=20)
        self.TakeDamage(damage=damageTaken)

    def TakeDamage(self, damage):
        """Damages this unit.

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
        self.health -= damage
        print("{0} took {1} damage, and has {2} health remaining".format(self.name, damage, self.health))

