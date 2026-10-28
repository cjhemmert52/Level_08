class BankAccount: 

#The init and the methods of the BankAccount class
    def __init__(self, account_name, account_number):
        self.balance = 0.0
        self.name = account_name
        self.account_number = account_number

#Any value that is invalid (negative or greater than the current amount) returns false
    def withdraw(self, amount):
        if amount > self.balance or amount <= 0:
            return False
        self.balance -= amount
        return True

#Any value that is invalid (negative or greater than the current amount) returns false
    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def account_info(self):
        print(f'Name: {self.name}')
        print(f'Account #: {self.account_number}')
        print(f'Balance: ${self.balance:.2f}')


#Accepts and validates an input, if the input is valid it makes the deposit    
def make_deposit(account):
    try:
        amount = float(input("How much would you like to deposit? "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    if amount <= 0:
        print("Invalid amount. Deposit must be greater than $0.00.")
    else:
        account.deposit(amount)
        print(f"Deposited ${amount:.2f}.")


#Works the same as the deposit function with validation, and calling the withdraw function
def make_withdrawal(account):
    try:
        amount = float(input("How much would you like to withdraw? "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    if amount <= 0:
        print("Invalid amount. Withdrawal must be greater than $0.00.")
    else:
        success = account.withdraw(amount)
        if success:
            print(f"Withdrew ${amount:.2f}.")
        else:
            print("Insufficient funds.")


def view_account_info(account):
    account.account_info()
