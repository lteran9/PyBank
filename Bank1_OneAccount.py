# Non-OOP
# Bank Version 2
# Single Account

accountName = ''
accountPassword = ''
accountBalance = 0


def newAccount(name, balance, password):
    global accountName, accountPassword, accountBalance
    accountName = name
    accountBalance = balance
    accountPassword = password


def show():
    global accountName, accountPassword, accountBalance
    print('\tName:', accountName)
    print('\tBalance:', accountBalance)
    print('\tPassword:', accountPassword)
    print()


def getBalance():
    global accountName, accountPassword, accountBalance
    userPassword = input('Please enter the password: ')
    if userPassword != accountPassword:
        print('Incorrect password!')
    else:
        print(accountBalance, '\n')


def deposit():
    global accountName, accountPassword, accountBalance
    userDepositAmount = input('Please enter amount to deposit: ')
    userDepositAmount = int(userDepositAmount)
    userPassword = input('Please enter the password: ')

    if userDepositAmount < 0:
        print('You cannot deposit a negative amount!')
    elif userPassword != accountPassword:
        print('Incorrect password!')
    else:
        accountBalance = accountBalance + userDepositAmount
        print('Your new balance is:', accountBalance)


def withdraw():
    global accountName, accountPassword, accountBalance
    userWithdrawAmount = input('Please enter the amount to withdraw:')
    userWithdrawAmount = int(userWithdrawAmount)
    userPassword = input('Please enter the password: ')

    if userWithdrawAmount < 0:
        print('You cannot withdraw a negative amount')

    elif userPassword != accountPassword:
        print('Incorrect password!')

    elif userWithdrawAmount > accountBalance:
        print('You cannot withdraw more than you have in your account')

    else:
        accountBalance = accountBalance - userWithdrawAmount
        print('Your new balance is:', accountBalance)


newAccount('Joey', 100, 'abcd1234')

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
        getBalance()

    elif action == 'd':
        print('Deposit: ')
        deposit()

    elif action == 's':
        print('Show:')
        show()

    elif action == 'w':
        print('Withdraw:')
        withdraw()

    elif action == 'q':
        break

print('Done')
