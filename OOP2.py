class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        print(f"BankAccount {self.account_number} is being destroyed.")


class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = None

    def create_bank_account(self, account_number, balance, account_type):
        self.bank_account = BankAccount(account_number, balance, account_type)

    def __del__(self):
        print(f"Customer {self.name} is being destroyed.")


customer1 = Customer("Puja", 23, "Lalitpur")
customer1.create_bank_account("12345", 1000, "Savings")

customer2 = Customer("Sonika", 24, "Kathmandu")
customer2.create_bank_account("67890", 2000, "Saving")

