"""
@author Tyler C

This is my first example to showcase the similarities and
differences between Object-Oriented and Functional programming,
which gives a case that plays to OOP's strengths, and not so much
FP's. 

This code is a simple RPG with a hero, a monster, and a boss monster.
The hero can attack and heal, the monster can attack, and the boss monster
can do the same and block the healing of the hero.
"""


class Creature:
    def __init__(self, name, damage, hp):
        self.name = name
        self.damage = damage
        self.hp = hp

    def logMessage(self, message):
        print(message)

class Hero (Creature):
    def __init__(self, name, damage, hp, heal):
        super().__init__(name, damage, hp)
        self.heal = heal
        self.canHeal = True

    def attack(self, monster):
        monster.hp -= self.damage
        self.logMessage(f"Hero {self.name} attacks {monster.name}: {self.damage} damage dealt!")

    def healSelf(self):
        if self.canHeal:
            self.hp += self.heal
            self.logMessage(f"Hero {self.name} heals: {self.heal} hp regained!")
        else:
            self.logMessage(f"Hero {self.name}'s healing is blocked!")
            self.canHeal = True

class Monster(Creature):
    def __init__(self, name, damage, hp):
        super().__init__(name, damage, hp)

    def attack(self, hero):
        hero.hp -= self.damage
        self.logMessage(f"{self.name} attacks Hero {hero.name}: {self.damage} damage dealt!")

class BossMonster(Monster):
    def __init__(self, name, damage, hp):
        super().__init__(name, damage, hp)

    def blockHeal(self, hero):
        hero.canHeal = False
        self.logMessage(f"{self.name} blocks Hero {hero.name}'s healing!")


if __name__ == '__main__':
    Lobo = Hero('Lobo', 5, 24, 3)
    Orc = Monster('Orc', 3, 10)
    Orgalorg = BossMonster('Orgalorg', 5, 20)

    print("Lobo fights Orc!")

    Lobo.attack(Orc)
    Orc.attack(Lobo)
    Lobo.healSelf()
    Lobo.attack(Orc)
    
    print("Orc was defeated!")

    print("Lobo fights Orgalorg!")

    Lobo.attack(Orgalorg)
    Orgalorg.attack(Lobo)
    Orgalorg.blockHeal(Lobo)
    Lobo.healSelf()
    Lobo.attack(Orgalorg)
    Lobo.attack(Orgalorg)
    Orgalorg.attack(Lobo)
    Lobo.healSelf()
    Orgalorg.attack(Lobo)
    Lobo.healSelf()
    Lobo.attack(Orgalorg)
