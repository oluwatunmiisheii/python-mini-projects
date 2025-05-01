from zombie import *
from ogre import *
from hero import *
from weapon import *


def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print('----------------')
        e1.special_attack()
        e2.special_attack()

        e2.attack()
        e1.health_points -= e2.attack_damage

        print(f'{e1.get_type_of_enemy()} has {e1.health_points} health points left.')
        print(f'{e2.get_type_of_enemy()} has {e2.health_points} health points left.')

        e1.attack()
        e2.health_points -= e1.attack_damage

       

    print('------------------')

    if e1.health_points > 0:
        print(f'{e1.get_type_of_enemy()} wins!')
    else:
        print(f'{e2.get_type_of_enemy()} wins!')


def hero_battle(hero: Hero, enemy: Enemy):
    enemy.special_attack()

    while hero.health_points > 0 and enemy.health_points > 0:
        print('----------------')

        enemy.attack()
        hero.health_points -= enemy.attack_damage

        print(f'Hero has {hero.health_points} health points left.')
        print(f'{enemy.get_type_of_enemy()} has {enemy.health_points} health points left.')

        hero.attack()
        enemy.health_points -= hero.attack_damage

    print('------------------')

    if hero.health_points > 0:
        print('Hero wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!')


zombie = Zombie(health_points=10, attack_damage=1)
ogre = Ogre(health_points=20, attack_damage=3)
hero = Hero(health_points=10, attack_damage=1)
weapon = Weapon(weapon_type='Sword', attack_increase=15)
hero.weapon = weapon
hero.equip_weapon()

battle(zombie, ogre)
hero_battle(hero, ogre)