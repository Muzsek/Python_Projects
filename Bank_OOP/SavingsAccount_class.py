from BankAccount_class import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self,owner : str, balance : int, interestrate : float):
        super().__init__(owner, balance)
        self.interestrate = interestrate

    def add_interest(self):
        self.balance = self.balance + self.balance * self.interestrate

    def withdraw(self, amount : int):
        print("You cannot withdraw from a saving's account!")