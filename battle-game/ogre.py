from enemy import *
import random

class Ogre(Enemy):
    def __init__(self, health_points: int = 10, attack_damage: int = 1):
        super().__init__(type_of_enemy='Ogre', health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print("*Ogre is slamming hands all around...*")
    
    def special_attack(self):
        if random.random() < 0.2:
            self.attack_damage += 4
            print("Ogre gets angry and increases attack damage by 4!")