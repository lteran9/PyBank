# Test program using Accounts
# Version 3 - Using a dictionary of accounts

# Bring in all the code from the Account class
from Account import *

accountsDict = {}
nextAccountNumber = 0

# Create two accounts
oAccount = Account('Joe', 100, 'password')
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = oAccount
print('Account number for Joe is:', joesAccountNumber)
nextAccountNumber = nextAccountNumber + 1

oAccount = Account('Mary', 12345, 'anotherPassword')
marysAccountNumber = nextAccountNumber
accountsDict[marysAccountNumber] = oAccount
print('Account number for Mary is:', marysAccountNumber)
nextAccountNumber = nextAccountNumber + 1

# Show the accounts
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
print()

# Call some methods on the different accounts
print('Calling methods on the two accounts...')
accountsDict[joesAccountNumber].deposit(50, 'password')
accountsDict[marysAccountNumber].withdraw(345, 'anotherPassword')
accountsDict[marysAccountNumber].deposit(100, 'anotherPassword')

# Show the accounts
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
print()

# Create another account with information from the user
print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = oAccount
print('Account number for new account is:', newAccountNumber)
nextAccountNumber = nextAccountNumber + 1

# Show the newly created user account
accountsDict[newAccountNumber].show()

# Let's deposit 100 into the new account
accountsDict[newAccountNumber].deposit(100, userPassword)
usersBalance = accountsDict[newAccountNumber].getBalance(userPassword)
print()
print("After depositing 100, user's balance is:", usersBalance)

# Show the new account
accountsDict[newAccountNumber].show()
