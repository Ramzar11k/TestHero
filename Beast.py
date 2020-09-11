from Unit import Unit
import random


class Beast(Unit):
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
        super().Attack(target)
        print("{0} attacks {1}".format(self.name, target.name))
        target.CalculateDamageTaken(attackerStrength=self.strength)

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

        damageTaken = max(attackerStrength - self.defence, 0)
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
            If there is no parameter passed
            If the value of damage is negative
        TypeError
            If damage is not an int
        """

        super().TakeDamage(damage)
        if random.randint(0, 100) <= self.luck:
            print("{} gets lucky and avoids the attack".format(self.name))
            return
        self.health -= damage
        print("{0} took {1} damage, and has {2} health remaining".format(self.name, damage, self.health))

    def Defeat(self):
        print("ouch")
