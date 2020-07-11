import random


class Coin(object):
    def __init__(self, heads=True, is_clean=True, is_rare=False, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.is_rare = is_rare
        self.is_clean = is_clean
        if (self.is_rare):
            self.value = float(original_value) * 1.25
        else:
            self.value = self.original_value
        if self.is_clean:
            self.color = self.clean_color
        else:
            self.colour = self.rusty_color
        self.color = self.color
        self.heads = heads

    def switch_side(self):
        self.heads = not self.heads

    def flip(self):
        self.heads = random.choice([True, False])

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print("Coin Spent!")

    def __str__(self):
        if self.original_value >= 1:
            return "${} Coin".format(int(self.original_value))
        else:
            return "{}c Coin".format(int(self.original_value*100))


class Dollar(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_color": "silver",
            "rusty_color": "greenish silver",
            "edges": 7,
            "diameter": 25.85,
            "thickness": 1.65,
            "weight": 10
        }
        super().__init__(**data)


class One_cent(Coin):
    def __init__(self):
        data = {
            "diameter": 19,
            "thickness": 1.5,
            "edges": 1,
            "original_value": .01,
            "weight": 3.11,
            "clean_color": "copper",
            "rusty_color": "greenish copper",
        }
        super().__init__(**data)


class Five_cents(Coin):
    def __init__(self):
        data = {
            "diameter": 21,
            "thickness": 1.67,
            "edges": 1,
            "original_value": .05,
            "weight": 3.46,
            "clean_color": "silver",
            "rusty_color": "greenish silver",
        }
        super().__init__(**data)


class Ten_cents(Coin):
    def __init__(self):
        data = {
            "diameter": 17.77,
            "thickness": 1.35,
            "edges": 1,
            "original_value": .10,
            "weight": 2.09,
            "clean_color": "silver",
            "rusty_color": "greenish silver",
        }
        super().__init__(**data)


class Quarter(Coin):
    def __init__(self):
        data = {
            "diameter": 23.66,
            "thickness": 1.82,
            "edges": 1,
            "original_value": .25,
            "weight": 5.1,
            "clean_color": "silver",
            "rusty_color": "greenish silver",
        }
        super().__init__(**data)


coins = [One_cent(), Five_cents(), Ten_cents(), Quarter(), Dollar()]

for coin in coins:
    args = [coin, coin.color, coin.value, coin.diameter,
            coin.thickness, coin.edges, coin.weight]

    string = "{} - color: {}, value: {}, diamater(mm): {}, thickness(mm): {}, edges: {}, weight(g): {}".format(
        *args)

    print(string)
