from Hero import Hero
from Beast import Beast
from Arena import Arena

ordeus = Hero(name="Ordeus",
              healthRange=(70, 80),
              strengthRange=(70, 80),
              defenceRange=(45, 55),
              speedRange=(40, 50),
              luckRange=(10, 30))
billy = Hero(name="Billy",
             healthRange=(75, 95),
             strengthRange=(65, 85),
             defenceRange=(40, 60),
             speedRange=(45, 55),
             luckRange=(5, 25))
beast = Beast(name="Beast",
              healthRange=(60, 90),
              strengthRange=(60, 90),
              defenceRange=(40, 60),
              speedRange=(40, 60),
              luckRange=(25, 40))

fight = Arena(name="Emagia", fighter1=ordeus, fighter2=beast, maxTurns=20)
fight.StartCombat()

print("Combat Ended")


