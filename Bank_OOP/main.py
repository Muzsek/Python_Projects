from Bank_class import Bank
from BankAccount_class import BankAccount
from SavingsAccount_class import SavingsAccount


if __name__ == "__main__":
    my_bank = Bank()

    acc1 = BankAccount("Adam", 1000)
    acc2 = SavingsAccount("Eva",2000,0.05)

    my_bank.add_account(acc1)
    my_bank.add_account(acc2)

    print(f"Total balance: {my_bank.get_total_balance()}")
    my_bank.list_accounts()
    