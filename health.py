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
        random_potion = random.randint(0, min_heal)
        self.health = int(self.health + random_potion + min_heal)
        self.missing_health = 100 - self.health

    def damage(self, difficulty):
        random_damage = random.randint(10, 20)
        self.health = int(self.health - random_damage*difficulty)
        self.missing_health = 100 - self.health


me = Person('Shaquille', 25)

me.potion(difficulty)
print(me.health)
me.damage(difficulty)
print(me.health, me.missing_health)
me.potion(difficulty)
print(me.health, me.missing_health)
