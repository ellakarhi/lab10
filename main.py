import os

def menu(id):
  print ("Press 1 to view account balance ")
  print ("Press 2 to withdraw")
  print ("Press 3 to deposit")
  print ("Press 4 to exit") 

  try:
    choice = int(input())
    if choice == 1:
      with open(id + ".txt") as f:
        account = f.readlines()
        if account:
          print(account[0])
        else:
          print("Your balance is $0")

    elif choice == 2:
      print(2)
    elif choice == 3:
      print(3)
    else:
      quit()
  except:
    menu(id)

def create_account(id):
  fwrite = open(id + ".txt", "w")
  menu(id)
  
def start():
  try:
    id = int(input("Please enter your bank ID: "))
    str_id = str(id)
    if os.path.isfile(id + ".txt"):
      menu(id)
    
    else:
      create_account(str_id)

  except:
    start()

menu(id)

new_line = ""
""""
with open("alice.txt") as f:
  new_line = f.readlines()

f.close()

print (new_line)

new_line[0] = "Hello\n"

print (new_line)

fwrite = open("alice.txt", "w")
for line in new_line:
  fwrite.write(line)

fwrite.close()
"""