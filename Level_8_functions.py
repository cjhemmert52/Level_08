class BankAccount: 
    starting_balance = 0

    def __init__(self, account_name, account_number):
        self.name = account_name
        self.id = account_number

    def withdraw(self, balance):
        amount = int(input('How much would you like to withdraw?'))
        self.balance -= amount
        return balance

    def deposit(self, balance):
        amount = int(input('How much would you like to deposit?'))
        self.balance += amount
        return balance
    
    def account_info(account_name, account_number, balance):
        print(BankAccount.balance)
        print(BankAccount.account_name)
        print(BankAccount.account_number)