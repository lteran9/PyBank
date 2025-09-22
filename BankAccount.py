# Non-OOP
# Bank Version 4
# Any number of accounts with a list of dictionaries

import Account

accountsList = []

# Create two sample accounts
print('Joe\'s account is account number:', len(accountsList))
accountsList.append(Account.Account('Joe', 100, 'soup'))

print('Mary\'s account is account number:', len(accountsList))
accountsList.append(Account.Account('Mary', 12345, 'nuts'))

while True:
    print('\n--------------------------')
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print('--------------------------\n')

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get balance:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        password = input('Please enter your password: ')
        balance = accountsList[userAccountNumber].getBalance(password)
        if balance != None:
            print('Your balance is:', balance)
        

    elif action == 'd':
        print('Deposit: ')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        amountToDeposit = input('Please enter amount to deposit: ')
        amountToDeposit = int(amountToDeposit)
        password = input('Please enter your password: ')
        balance = accountsList[userAccountNumber].deposit(amountToDeposit, password)
        if balance != None:
            print('Your balance is:', balance)

    elif action == 's':
        print('Show:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        accountsList[userAccountNumber].show()

    elif action == 'w':
        print('Withdraw:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        amountToWithdraw = input('Please enter amount to withdraw:')
        amountToWithdraw = int(amountToWithdraw)
        password = input('Please enter your password: ')
        balance = accountsList[userAccountNumber].withdraw(amountToWithdraw, password)
        if balance != None:
            print('Your balance is:', balance)

    elif action == 'q':
        break

print('Done')
