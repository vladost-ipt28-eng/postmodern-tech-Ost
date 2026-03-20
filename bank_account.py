class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним")
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума поповнення має бути більшою за нуль")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума зняття має бути більшою за нуль")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self.balance -= amount
        return self.balance