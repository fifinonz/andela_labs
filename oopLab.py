#OOP LAB
#Create a class called BankAccount
#Create a constructor that takes in an integer and assigns this to a `balance` property.
#Create a method called `deposit` that takes in cash deposit amount and updates the balance accordingly.
#Create a method called `withdraw` that takes in cash withdrawal amount and updates the balance accordingly. if amount is greater than balance return `"invalid transaction"`
#Create a subclass MinimumBalanceAccount of the BankAccount class


class BankAccount(object):
  def __init__(self,  balance = 90):
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
    
    else:
      return 'invalid transaction'

class MinimumBalanceAccount(BankAccount):
  def __init__(self,  minimum):
    self.balance = minimum