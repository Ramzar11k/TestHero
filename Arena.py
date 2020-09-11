import random
import time


class Arena:
    def __init__(self, name, fighter1, fighter2, maxTurns):
        self.name = name
        self.combatInProgress = False
        self.currentTurn = 1
        self.maxTurns = maxTurns

        self.fighter1 = fighter1
        self.fighter2 = fighter2

        self.DetermineAttackOrder()

    def DetermineAttackOrder(self):
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

    def SwapTurn(self):
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
        self.attacker.Attack(target=self.defender)

    def StartCombat(self):
        print("------------------------------------")
        self.attacker.PrintInfo()
        self.defender.PrintInfo()
        print("------------------------------------")
        self.combatInProgress = True
        while self.combatInProgress and self.currentTurn < self.maxTurns:
            print("Turn {}:".format(self.currentTurn))
            self.CombatAttack()
            if self.SwapTurn():
                print("------------------------------------")
                break
            print("------------------------------------")
            time.sleep(3)

