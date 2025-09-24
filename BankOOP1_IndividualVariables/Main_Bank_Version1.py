# Test program using accounts
# Version 1 - using explicit variables for each Account object

# Bring in all code from the Account class file
from Account import *

# Create two test accounts
oJoesAccount = Account('Joe', 100, 'password')
print('Created an account for Joe')

oMarysAccount = Account('Mary', 12345, 'anotherPassword')
print('Created an account for Mary')

oJoesAccount.show()
oMarysAccount.show()
print()

# Call methods on differing accounts
oJoesAccount.deposit(50, 'password')
oMarysAccount.withdraw(345, 'anotherPassword')
oMarysAccount.deposit(100, 'anotherPassword')

# Show the accounts
oJoesAccount.show()
oMarysAccount.show()

# Create another account with information from the user
print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for the new user account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oNewAccount = Account(userName, userBalance, userPassword)

# Show the newly created user account
oNewAccount.show()

# Deposit 100 into the new account
newBalance = oNewAccount.deposit(100, userPassword)
print()
print('After depositing 100, user\'s balance is:', newBalance)

# Show the new account
oNewAccount.show()
