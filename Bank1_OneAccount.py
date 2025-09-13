# Non-OOP
# Bank Version 1
# Single Account

accountName = 'Joey'
accountPassword = 'abcd1234'
accountBalance = 100

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
        userPassword = input('Please enter the password: ')
        if userPassword != accountPassword:
            print('Incorrect password!')
        else:
            print(accountBalance, '\n')

    elif action == 'd':
        print('Deposit: ')
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

    elif action == 's':
        print('Show:')
        print('\tName:', accountName)
        print('\tBalance:', accountBalance)
        print('\tPassword:', accountPassword)
        print()

    elif action == 'w':
        print('Withdraw:')

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

    elif action == 'q':
        break

print('Done')
