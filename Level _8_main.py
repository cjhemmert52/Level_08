from Level_8_functions import BankAccount, make_deposit, make_withdrawal, view_account_info
import random

#Ask for the name and store it in a varible for the instance of the class
print('Welcome to the Bank of Chandler!')
name = input('Please enter your name: ')

account = BankAccount(name, random.randint(10000, 99999))

#Greets the customer and asks them what they want to do.
while True:
    print('\nPlease choose an option')
    print('\n1. Make a deposit')
    print('2. Make a withdrawal')
    print('3. View account information')
    print('4. Quit')

    selection = input('')

#Based on the selection, the corresponding function gets called
    if selection == '1':
        make_deposit(account)
    elif selection == '2':
        make_withdrawal(account)
    elif selection == '3':
        view_account_info(account)
    elif selection == '4':
        print('Thank you for your business!')
        break
    else:
        print('Invalid choice, please try again.')
