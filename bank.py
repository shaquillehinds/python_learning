class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Not enought funds!")

    def statement(self):
        return print("Account Balance: ${}".format(self.balance))


class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return "{}'s Current Account: Balance ${}".format(self.name, self.balance)


class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return "{}'s Current Account: Balance ${}".format(self.name, self.balance)


shaq = Savings('Shaq', 6000000)
S = Current("Shaq", 1000000)


shaq.withdraw(6000500)
S.withdraw(1000100)
print(shaq)
print(S)
