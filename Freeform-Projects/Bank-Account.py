"""
The bank account class you'll create should have methods for each of the following:
1. Accepting deposits
2. Allowing withdrawals
3. Showing the balance
4. Showing the details of the account
"""
class BankAccount(object):
  #member variable
  balance = 0
  
  #parameter 'name' specifies who the account belongs to
  def __init__(self, name):
    self.name = name
    
  #__repr__ returns a message stating who the account belongs to and the actual balance
  def __repr__(self):
    return 'The Owner is: ' + self.name + ' , actual balance: ' + str(self.balance)
  
  #create a method which prints the users balance
  def show_balance(self):
    print float(self.balance)
    
  #create a method to deposit a value to your balance
  def deposit(self, amount):
    if amount <= 0:
      print 'Not enough budget!'
      return
    else:
      print "Your wished deposit is %s. Do you wish to proceed?" % (str(amount))
      self.balance += amount
      self.show_balance()
      
  #create a method to withdraw a value from your balance
  def withdraw(self, amount):
    if amount > self.balance:
      print 'Not enough budget!'
      return
    else:
      print "Your wished withdraw is %s. Do you wish to proceed?" % (str(amount))
      self.balance -= amount
      self.show_balance()

#test      
my_account = BankAccount('Barbara')
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account
