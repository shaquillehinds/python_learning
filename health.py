import random
import math
difficulty = 3


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.missing_health = 0

    def potion(self, difficulty):
        min_heal = int(self.missing_health / 2)
        random_potion = random.randint(min_heal, self.missing_health)
        self.health = int(self.health + random_potion)
        self.missing_health = 100 - self.health

    def damage(self, difficulty):
        random_damage = random.randint(10, 20)
        self.health = int(self.health - random_damage*difficulty)
        self.missing_health = 100 - self.health


me = Person('Shaquille', 25)
reached_max = 0
while(me.health > 0):
    me.damage(difficulty)
    me.damage(difficulty)
    me.potion(difficulty)
    if(me.health == 100):
        reached_max += 1
print("Reached Max "+str(reached_max)+" times")
print("I'm Dead. Current health = "+str(me.health))
