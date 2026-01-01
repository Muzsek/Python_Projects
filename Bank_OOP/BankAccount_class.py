class BankAccount:
    def __init__(self, owner : str, balance : int = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount : int):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount : int):
        if amount > 0 and self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insuficient funds")

    def transfer(self,target : BankAccount, amount : int):
        if amount > 0 and self.balance - amount >= 0:
            self.withdraw(amount)
            target.deposit(amount)
        else:
            print("Transfer failed: Insufficient funds or invalid amount")

    def info(self):
        print(f"Bank account Infromation\nName: {self.owner}\nBalance: {self.balance}")