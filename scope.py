item = 'nuggets'


def global_scope():
    global item
    global sin
    sin = 'Greed'
    item = 'chicken'


global_scope()
print(item, sin)


def about(name, age, likes='Javascript'):
    sentence = "Meet {}! They are {} years old and they like {}".format(
        name, age, likes)
    return sentence


print(about('Hakeem', 25))
dina = {"name": "Dina", "age": 24, "likes": "food"}
print(about(**dina))
