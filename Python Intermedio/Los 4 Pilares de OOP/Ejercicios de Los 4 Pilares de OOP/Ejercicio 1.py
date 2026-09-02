class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if amount > self.balance:
            raise ValueError("Fondos insuficientes.")
        self.balance -= amount
        return self.balance

    def __repr__(self):
        return f"{self.__class__.__name__}(balance={self.balance})"


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        self.balance = balance
        self.min_balance = min_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if self.balance - amount < self.min_balance:
            raise ValueError(
                f"No se puede retirar ${amount}: el balance quedaría en "
                f"${self.balance - amount}, por debajo del mínimo (${self.min_balance})."
            )
        self.balance -= amount
        return self.balance

