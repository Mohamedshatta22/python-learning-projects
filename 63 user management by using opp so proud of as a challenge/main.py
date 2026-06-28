import time
import os
def clear():
 os.system("cls") if os.name =="nt" else os.system("clear")
print("welcome to user management ...")
users = {
 
}
class saving_user ():
 def __init__(self,first_name,last_name,email,password,status="inactive"):
  self.first_name = first_name
  self.last_name = last_name
  self.email = email
  self.password = password
  self.status = status
def asks():
  print("please choose an action: " )
  print("1- add a member")
  print("2- disaplay all users")
  print("3- exit...")

def saving_to_opp():
  first_name = input("please enter your first name: " )
  last_name = input("please enter your last name: " )
  email = input("please enter your email: " )
  password = input("please enter your password: " )
  if "@" in email:
   return saving_user(first_name,last_name,email,password,status="active")
  else :
    return saving_user(first_name,last_name,email,password,)
while True:
 asks()
 qu = int(input("please enter your choice: "))
 if qu == 1:
  for x in range(1,10000000000):
   x = saving_to_opp()
   users[x]= {"first_name":x.first_name,"last_name":x.last_name,"email":x.email,"status":x.status
                    }
   clear()
   print("users was added successfully..")
   break
 elif qu == 2:
  print("display all users....")
  time.sleep(3)
  for c in users:
   print(f"first name is: {users[c]["first_name"]}")
   time.sleep(1)
   print(f"last name is: {users[c]["last_name"]}")
   time.sleep(1)
   print(f"first name is: {users[c]["email"]}")
   time.sleep(1)
   print(f"the user status is :{users[c]["status"]} ")
   print("------------------")
 else:
  break
