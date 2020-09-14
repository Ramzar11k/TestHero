import random
import time
from Unit import Unit


class Arena:
    """
    An Arena takes two units and has them fight each other.

    ...

    Attributes
    ----------
    name : str
        Name of the arena.
    fighter1: Unit
        First fighter.
    fighter2: Unit
        Second fighter.
    maxTurns: int
        Maximum number of turns until combat is over.
        A turn ends when the attacker and defender swap.
        Minimum of 1 turn.
    currentTurn: int
        The current combat turn.
    combatInProgress: bool
        True while the units are fighting.

    Methods
    -------
    DetermineAttackOrder()
        Decides which fighter attacks first based on who has the higher speed.
        If their speeds are equal the higher luck attacks first.
        If their luck is also equal it is determined by chance.
    EndTurn()
        Checks if the combat has ended, either by knockout or turn limit.
        If it is not over it swaps the attacker and defender and continues.
    CombatAttack()
        Makes the attacker attack the defender.
    StartCombat()
        Starts the fight.
    """

    def __init__(self, name, fighter1, fighter2, maxTurns):
        """
        Initializes the arena.

        Parameters
        ----------
        name : str
            The name of the arena
        fighter1: Unit
            The first fighter.
        fighter2: Unit
            The second fighter.
        maxTurns: int
            The maximum number of turns that can happen until combat is over.
            A turn ends when the attacker and defender swap.
            Minimum of 1 turn.

        Raises
        ------
        TypeError
            If there are not four parameters passed.
            If name is not a string.
            If fighter1 does not inherit from the Unit class.
            If fighter2 does not inherit from the Unit class.
            If fighter1 is fighter2.
            If maxTurns is not an int.

        ValueError
            If maxTurns is less than 1.
        """

        self.ValidateInputs(name=name,
                              fighter1=fighter1,
                              fighter2=fighter2,
                              maxTurns=maxTurns)
        self.name = name
        self.maxTurns = maxTurns
        self.currentTurn = 1
        self.combatInProgress = False

        self.fighter1 = fighter1
        self.fighter2 = fighter2

        self.DetermineAttackOrder()

    def ValidateInputs(self, name, fighter1, fighter2, maxTurns):
        if len(locals()) != 5:
            raise TypeError("Arena class takes four parameters")

        if type(name) is not str:
            raise TypeError("Arena name must be a string")
        if not issubclass(type(fighter1), Unit):
            raise TypeError("Fighter1 must inherit from class Unit")
        if not issubclass(type(fighter2), Unit):
            raise TypeError("Fighter2 must inherit from class Unit")
        if fighter1 is fighter2:
            raise TypeError("You need two different unit")
        if type(maxTurns) is not int:
            raise TypeError("Max turns must be an int")

        if maxTurns < 1:
            raise ValueError("Max turns must be at least 1")



    def DetermineAttackOrder(self):
        """
        Determines which fighter attacks first.
        The fighter with the higher speed starts.
        If their speeds are equal the higher luck attacks first.
        If their luck is also equal it is determined by chance.
        """

        if self.fighter1.speed > self.fighter2.speed:
            self.attacker = self.fighter1
            self.defender = self.fighter2
        elif self.fighter2.speed > self.fighter1.speed:
            self.attacker = self.fighter2
            self.defender = self.fighter1
        else:
            if self.fighter1.luck > self.fighter2.luck:
                self.attacker = self.fighter1
                self.defender = self.fighter2
            elif self.fighter2.luck > self.fighter1.luck:
                self.attacker = self.fighter2
                self.defender = self.fighter1
            else:
                if random.random() <= 0.5:
                    self.attacker = self.fighter1
                    self.defender = self.fighter2
                else:
                    self.attacker = self.fighter2
                    self.defender = self.fighter1

    def EndTurn(self):
        """
        Checks if the combat has ended, either by knockout or turn limit.
        If it is not over it swaps the attacker and defender and continues.

        Returns
        -------
        True
            If the defenders health is <= 0
            If currentTurn == maxTurns
        False
            Otherwise
        """

        if self.defender.health <= 0:
            print("{0} ran out of health and passed out, {1} is the victor!".format(self.defender.name, self.attacker.name))
            return True
        self.currentTurn += 1
        if self.currentTurn >= self.maxTurns:
            print("Both parties got bored of the fight and parted ways, draw!")
            return True
        self.attacker, self.defender = self.defender, self.attacker
        return False

    def CombatAttack(self):
        """
        Makes the attacker attack the defender.
        Calls the attacking Units Attack method.
        """
        self.attacker.Attack(target=self.defender)

    def StartCombat(self):
        """
        Starts the fight, the combat cycle also occurs here.
        The fight continues until one of the end conditions from
        EndTurn() is met.
        """

        print("------------------------------------")
        self.fighter1.PrintInfo()
        self.fighter2.PrintInfo()
        print("------------------------------------")
        self.combatInProgress = True
        while self.combatInProgress and self.currentTurn < self.maxTurns:
            print("Turn {}:".format(self.currentTurn))
            self.CombatAttack()
            if self.EndTurn():
                print("------------------------------------")
                break
            print("------------------------------------")
            time.sleep(3)

