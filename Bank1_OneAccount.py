# Non-OOP
# Bank Version 3
# Any number of accounts with index

accountNamesList = []
accountPasswordsList = []
accountBalancesList = []


def newAccount(name, balance, password):
    global accountNamesList, accountPasswordsList, accountBalancesList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)


def show(accountNumber):
    global accountNamesList, accountPasswordsList, accountBalancesList
    print('Account:', accountNumber)
    print('\tName:', accountNamesList[accountNumber])
    print('\tBalance:', accountBalancesList[accountNumber])
    print('\tPassword:', accountPasswordsList[accountNumber])
    print()


def getBalance(accountNumber):
    global accountNamesList, accountPasswordsList, accountBalancesList
    userPassword = input('Please enter the password: ')
    if userPassword != accountPasswordsList[accountNumber]:
        print('Incorrect password!')
    else:
        print(accountBalancesList[accountNumber], '\n')


def deposit(accountNumber):
    global accountNamesList, accountPasswordsList, accountBalancesList
    userDepositAmount = input('Please enter amount to deposit: ')
    userDepositAmount = int(userDepositAmount)
    userPassword = input('Please enter the password: ')

    if userDepositAmount < 0:
        print('You cannot deposit a negative amount!')
    elif userPassword != accountPasswordsList[accountNumber]:
        print('Incorrect password!')
    else:
        accountBalancesList[accountNumber] = accountBalancesList[accountNumber] + \
            userDepositAmount
        print('Your new balance is:', accountBalancesList[accountNumber])


def withdraw(accountNumber):
    global accountNamesList, accountPasswordsList, accountBalancesList
    userWithdrawAmount = input('Please enter the amount to withdraw:')
    userWithdrawAmount = int(userWithdrawAmount)
    userPassword = input('Please enter the password: ')

    if userWithdrawAmount < 0:
        print('You cannot withdraw a negative amount')

    elif userPassword != accountPasswordsList[accountNumber]:
        print('Incorrect password!')

    elif userWithdrawAmount > accountBalancesList[accountNumber]:
        print('You cannot withdraw more than you have in your account')

    else:
        accountBalancesList[accountNumber] = accountBalancesList[accountNumber] - \
            userWithdrawAmount
        print('Your new balance is:', accountBalancesList[accountNumber])


# Create two sample accounts
print("Joe's account is account number:", len(accountNamesList))
newAccount("Joe", 100, 'soup')

print("Mary's account is account number:", len(accountNamesList))
newAccount("Mary", 12345, 'nuts')

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
        getBalance(userAccountNumber)

    elif action == 'd':
        print('Deposit: ')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        deposit(userAccountNumber)

    elif action == 's':
        print('Show:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        show(userAccountNumber)

    elif action == 'w':
        print('Withdraw:')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        withdraw(userAccountNumber)

    elif action == 'q':
        break

print('Done')
