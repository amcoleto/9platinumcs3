class BankAccount:
  """ 
  A class for a bank account that protects the account number, prevents negative balances, and allows controlled access through methods.

  Attributes:
  account_number (integer): account number of a bank account
  balance (integer): balance of a bank account
  """
  def __init__(self, account_number:int, balance: float):
    self.__account_number = 0  # Private Attributes
    self.__balance = 0
    self.set_account_number(account_number)  # Public Methods
    self.set_balance(balance)

  def set_account_number(self,account_number):
    """ This function sets the account number, it also validates whether an account number is positive or not. """
    if account_number > 0:
      self.__account_number = account_number

  def set_balance(self, balance):
    """ This function sets the balance, it also validates if the balance is negative. If the balance is negative, then a warning will appear and ignore the negative balance."""
    if balance < 0:
      print("The balance must be not be a negative number.")
    else:
      self.__balance = balance

  def get_account_number(self):
    """ This function returns the account number. """
    return self.__account_number
    
  def get_balance(self):
    """ This function returns the balance of an account. """
    return f"{self.__balance:.2f}"

# Testing

a1 = BankAccount(12345,1000)

print("Output:")
print("\nAccount 1")
print(f"Account Number: {a1.get_account_number()} ")
print(f"Balance: {a1.get_balance()} ")

print("\nUpdate balance to -100")
a1.set_balance(-100)
print(f"Account Number: {a1.get_account_number()} ")
print(f"Balance: {a1.get_balance()} ")

  
      
  
      
      
