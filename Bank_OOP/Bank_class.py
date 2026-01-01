from BankAccount_class import BankAccount
from SavingsAccount_class import SavingsAccount


class Bank:
    def __init__(self, accounts : list = None):
        if accounts is None:
            self.accounts = []
        else:
            self.accounts = accounts
    
    def add_account(self, account : BankAccount | SavingsAccount):
        self.accounts.append(account)
    
    def get_total_balance(self) -> float:
        total = 0
        for i in self.accounts:
            total += i.balance
        return total

    def list_accounts(self):
        for account in self.accounts:
            print(f"Name: {account.owner} | Balance: {account.balance}")