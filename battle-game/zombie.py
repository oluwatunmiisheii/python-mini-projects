from enemy import *
import random

class Zombie(Enemy):
    def __init__(self, health_points: int = 10, attack_damage: int = 1):
        super().__init__(type_of_enemy='Zombie', health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print("*Zombie is Grumbling...*")

    def spread_disease(self):
        print("Zombie is trying to spread infection!")
    
    def special_attack(self):
        if random.random() < 0.5:
            self.health_points += 2
            print("Zombie has gained 2 health points!")