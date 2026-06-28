import time
def obtaining_info():
 user_name = input("please enter the user name: ")
 email = input("please enter you email here:  ")
 checking_email(email, user_name)
 return user_name and email 
 
def checking_email(email,user_name):
     if "@" in email and "." in email:
        print("checking user name....")
        time.sleep(3)
        print("validating email....")
        time.sleep(3)
        print(f"user {user_name} with email {email} successfully added")
     else:
        print("checking user name....")
        time.sleep(3)
        print("validating user name....")
        time.sleep(3)
        print(f"invaild email format registaration faild")
obtaining_info()
  _______________________________
# ربنا يصبرني 2026 شهر 6 يوم 17

import time
import os
def clear():
 os.system("cls") if os.name =="nt" else os.system("clear")

def getting_info ():
  name = input("what is your name please: ")
  clear()
  print("cheking your name please wait.....")
  time.sleep(2)
  email = input("what is your email please: ")
  clear()
  print("cheking your email please wait.....")
  time.sleep(2)
  
  checking_email(name,email)

def checking_email(name,email):
 while True:
  if  "@" in email and "." in email:
    print(f"right {name} your email is valid you can access ")
    break
  else:
    print("invalid email please retyp again")
    email = input("what is your email please: ")
    clear()
    print("cheking your email please wait.....")
    time.sleep(2)


getting_info ( )
