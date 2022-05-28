# ATM Program
import os

def menu(id):
  print ("Press 1 to view account balance")
  print ("Press 2 to withdraw")
  print ("Press 3 to deposit")
  print ("Press 4 to exit")

  try:
    choice = int(input())
    if choice == 1:
      with open(id + ".txt") as f:
        account = f.readlines()
      
      if account:
        print ("Your balance is $" + account[0])
        menu(id)
      else:
        print ("Your balance is $0")
        menu(id)
    elif choice == 2:
      withdraw(id)
      menu(id)
    elif choice == 3:
      deposit(id)
      menu(id)
    else:
      print("Thank you!")
      return
  except:
    menu(id)

def withdraw(id):
  """with draws amount from id file"""
  new_balance = 0
  
  with open(id + ".txt") as f:
    balance = f.readlines()
  f.close()

  try:
    amount = int(input("Please enter amount: $"))
  except:
    withdraw(id)

  if amount > int(balance[0]):
    print ("You cannot withdraw more than you have.")
    withdraw(id)

  int_balance = int(balance[0])
  new_balance = int_balance - amount
                    
  fwrite = open(id + ".txt", "w")
  fwrite.write(str(new_balance))
  print(f"Your new balance is {new_balance}")
  fwrite.close()

def deposit(id):
  """Deposits input amount into id file"""
  with open(id + ".txt") as f:
    balance = f.readlines()
  f.close()
  try:
    deposit_amount = int(input("Please enter the amount you want to deposit: $"))
  except:
    deposit(id)
  if deposit_amount < 0:
    print("You cannot deposit a negative amount")
    deposit(id)
  int_balance = int(balance[0])
  new_balance = int_balance + deposit_amount

  fwrite = open(id + ".txt", "w")
  fwrite.write(str(new_balance))
  print(f"Your new balance is {new_balance}")
  fwrite.close()
     

def create_account(id):
  """creates an account if one doesn't already exist and gives it a starting value of 0"""
  new_account = open(id + ".txt", "w")
  new_account.write('0')
  new_account.close()
  menu(id)

def start():
  try:
    id = int(input("Please enter your bank ID: "))
    str_id = str(id)
    if os.path.isfile(str_id + ".txt"):
      menu(str_id)
    else:
      create_account(str_id)
  except:
    start()

start()
#menu("9999")