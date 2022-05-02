"""
@author Tyler C

This is the second part of the first example
of my analysis of OOP and FP. This example plays
to OOP's strengths and not so much to FP's

This is a simple RPG programmed using FP in Python.
It follows the same rules as ex1_RPG_OOP.py
"""

def logMessage(message):
    print(message)

def healSelf(hero):
    if 'heal' in hero and 'canHeal' in hero and hero['canHeal']:
        hero['hp'] += hero['heal']
        logMessage(f"Hero {hero['name']} heals: {hero['heal']} hp regained!")
    else:
        logMessage(f"{hero['name']} unable to heal!")
        if 'canHeal' in hero:
            hero['canHeal'] = True

def attack(entity1, entity2):
    entity2['hp'] -= entity1['attack']
    logMessage(f"{entity1['name']} attacks {entity2['name']}: {entity1['attack']} damage dealt")

def blockHeal(boss, hero):
    if hero['canHeal']:
        hero['canHeal'] = False
        logMessage(f"{boss['name']} blocks {hero['name']}'s healing!")
    else:
        logMessage(f"{boss['name']} cannot block {hero['name']}'s healing!")


if __name__ == '__main__':
    Lobo = {
            'name': 'Lobo',
            'attack': 5,
            'hp': 24,
            'heal': 3,
            'canHeal': True
            }

    Orc = {
            'name': 'Orc',
            'attack': 3,
            'hp': 10
            }
    
    Orgalorg = {
            'name': 'Orgalorg',
            'attack': 5,
            'hp': 20
            }

    print("Lobo fights Orc!")

    attack(Lobo, Orc)
    attack(Orc, Lobo)
    healSelf(Lobo)
    attack(Lobo, Orc)

    print("Orc was defeated!")

    print("Lobo fights Orgalorg!")

    attack(Lobo, Orgalorg)
    attack(Orgalorg, Lobo)
    blockHeal(Orgalorg, Lobo)
    healSelf(Lobo)
    attack(Lobo, Orgalorg)
    attack(Lobo, Orgalorg)
    attack(Orgalorg, Lobo)
    healSelf(Lobo)
    attack(Orgalorg, Lobo)
    healSelf(Lobo)
    attack(Lobo, Orgalorg)
