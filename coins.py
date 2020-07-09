import random


class Coin(object):
    def __init__(self, value, color, diameter, thickness, edges, rare=False):
        self.rare = rare
        if (self.rare):
            self.value = float(value) + .25
        else:
            self.value = value
        self.color = color
        self.heads = True
        self.edges = edges
        self.diameter = diameter  # mm
        self.thickness = thickness  # mm

    def switch_side(self):
        self.heads = False

    def flip(self):
        self.heads = random.choice([True, False])

    def rust(self):
        self.color = "dark " + self.color

    def clean(self):
        self.color = self.color[0:5]

    def __del__(self):
        print("Coin Spent!")


dollar = Coin(1.00, 'silver', 25.88, 1.65, 7)
print(dollar.value)
