# Non-OOP
# Bank Version 4
# Any number of accounts with a list of dictionaries

accountsList = []

def newAccount(aName, aBalance, aPassword):
    global accountsList
    newAccountDict = { 'name': aName, 'balance': aBalance, 'password': aPassword }
    accountsList.append(newAccountDict)

def show(accountNumber):
    global accountsList
    print('Account:', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('\tName:', thisAccountDict['name'])
    print('\tBalance:', thisAccountDict['balance'])
    print('\tPassword:', thisAccountDict['password'])
    print()

def getBalance(accountNumber):
    global accountsList
    userPassword = input('Please enter the password: ')
    thisAccountDict = accountsList[accountNumber]
    if userPassword != thisAccountDict['password']:
        print('Incorrect password!')
    else:
        print(thisAccountDict['balance'], '\n')

def deposit(accountNumber):
    global accountsList
    thisAccountDict = accountsList[accountNumber]

    userDepositAmount = input('Please enter amount to deposit: ')
    userDepositAmount = int(userDepositAmount)
    userPassword = input('Please enter the password: ')

    if userDepositAmount < 0:
        print('You cannot deposit a negative amount!')
    elif userPassword != thisAccountDict['password']:
        print('Incorrect password!')
    else:
        thisAccountDict['balance'] = thisAccountDict['balance'] + userDepositAmount
        print('Your new balance is:', thisAccountDict['balance'])

def withdraw(accountNumber):
    global accountsList
    userWithdrawAmount = input('Please enter the amount to withdraw:')
    userWithdrawAmount = int(userWithdrawAmount)
    userPassword = input('Please enter the password: ')
    thisAccountDict = accountsList[accountNumber]
    if userWithdrawAmount < 0:
        print('You cannot withdraw a negative amount')
    elif userPassword != thisAccountDict['password']:
        print('Incorrect password!')
    elif userWithdrawAmount > thisAccountDict['balance']:
        print('You cannot withdraw more than you have in your account')
    else:
        thisAccountDict['balance'] = thisAccountDict['balance'] - userWithdrawAmount
        print('Your new balance is:', thisAccountDict['balance'])

# Create two sample accounts
print("Joe's account is account number:", len(accountsList))
newAccount("Joe", 100, 'soup')

print("Mary's account is account number:", len(accountsList))
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
