import time
import os
def clear():
 os.system("cls") if os.name =="nt" else os.system("clear")
print("welcome to user management ...")
users = {
 
}
class saving_user ():
 def __init__(self,user_id,first_name,last_name,status="inactive"):
  self.user_id = user_id
  self.first_name = first_name
  self.last_name = last_name
  self.status = status
def asks():
  print("please choose an action: " )
  print("1- add a member")
  print("2- disaplay all users")
  print("3-search for a member")
  print("4- exit...")

def saving_to_opp():
  first_name = input("please enter your first name: " )
  last_name = input("please enter your last name: " )
  user_id = input("please enter an id for the member")
  activity = input("please enter member status, or click to enter")
  if "active" in activity:
   return saving_user(user_id,first_name,last_name,status="active")
  else :
    return saving_user(user_id,first_name,last_name,)
def num1():
  for x in range(1,10000000000):
   x = saving_to_opp()
   users[x.user_id]= {"first_name":x.first_name,"last_name":x.last_name,"status":x.status
                    }
   clear()
   print("user was added successfully..")
   break
def num2():
  print("display all users....")
  time.sleep(3)
  for c in users:
   print(f"the id user is: {c}")
   print(f"first name is: {users[c]["first_name"]}")
   time.sleep(1)
   print(f"last name is: {users[c]["last_name"]}")
   time.sleep(1)
   print(f"the user status is :{users[c]["status"]} ")
   print("------------------")
   time.sleep(3)
   clear()
def num3():
 while True:
   clear()
   print("search by...")
   print("1- membership id")
   print("2- first name")
   print("3-membership status")
   qu = int(input("please choose an action:"))
   if qu == 1:
    ask = input("enter the membership id here please: ")
    if ask in users:
     print(f"the id user is: {ask}")
     print(f"first name is: {users[ask]["first_name"]}")
     time.sleep(1)
     print(f"last name is: {users[ask]["last_name"]}")
     time.sleep(1)
     print(f"the user status is :{users[ask]["status"]} ")
     print("------------------")
     time.sleep(3)
    else:
     print("wrong membership id")
     time.sleep(2)
     clear()
     continue
   elif qu ==2:
    ask = input("enter the membership first name here please: ")
    for x in users:
     if ask == users[x]["first_name"]:
      print(f"the id user is: {x}")
      print(f"first name is: {users[x]["first_name"]}")
      time.sleep(1)
      print(f"last name is: {users[x]["last_name"]}")
      time.sleep(1)
      print(f"the user status is :{users[x]["status"]} ")
      print("------------------")
      time.sleep(3)
      clear()
     else:
      time.sleep(2)
      clear()
      continue
   elif qu == 3:
    ask = input("enter the membership status here (active/inactive)?: ")
    for x in users:
     if ask == users[x]["status"]:
      print(f"the id user is: {x}")
      print(f"first name is: {users[x]["first_name"]}")
      time.sleep(1)
      print(f"last name is: {users[x]["last_name"]}")
      time.sleep(1)
      print(f"the user status is :{users[x]["status"]} ")
      print("------------------")
      time.sleep(1)
  
while True:
 asks()
 qu = int(input("please enter your choice: "))
 if qu == 1:
   num1()
 elif qu == 2:
   num2()
 elif qu == 3:
  num3()
 else:
  break
--------------------------------------------
النسخة المعربة import time
import os
import arabic_reshaper
from bidi.algorithm import get_display

# 1. بنعمل الاختصار بتاعنا مرة واحدة بس فوق
def print_ar(text):
    reshaped_text = arabic_reshaper.reshape(text)
    final_text = get_display(reshaped_text)
    print(final_text)
def input_ar(text):
    reshaped_text = arabic_reshaper.reshape(text)
    final_text = get_display(reshaped_text)
    return input(final_text)
def clear():
 os.system("cls") if os.name =="nt" else os.system("clear")
print("welcome to user management ...")
users = {
 
}
class saving_user ():
 def __init__(self,user_id,first_name,last_name,status="inactive"):
  self.user_id = user_id
  self.first_name = first_name
  self.last_name = last_name
  self.status = status
def asks():
  print_ar("اختار مدخل")
  print_ar("ادخل عضو جديد1- ")
  print_ar("2- اعرض كل المستخدمين")
  print_ar("3-ابحث عن مستخدمين")
  print_ar("4- اخرج...")

def saving_to_opp():
  first_name = input_ar("ادخل الاسم الاول رجاء: " )
  last_name = input_ar("ادخل الاسم الاخير رجاء: " )
  user_id = input_ar("ادخل الرقم التعريفي للمستخدم")
  activity = input_ar("رجاء ادخل الحالة اما active/inactive")
  if "active" in activity:
   return saving_user(user_id,first_name,last_name,status="active")
  else :
    return saving_user(user_id,first_name,last_name,)
def num1():
  for x in range(1,10000000000):
   x = saving_to_opp()
   users[x.user_id]= {"first_name":x.first_name,"last_name":x.last_name,"status":x.status
                    }
   clear()
   print_ar("تمت اضافة المستخدم بنجاح..")
   break
def num2():
  print_ar("عرض كل المستخدمين....")
  time.sleep(3)
  for c in users:
   print_ar(f"الرقم التعريفي للمستخدم هوا: {c}")
   print_ar(f"الاسم الاول للمستخدم هوا : {users[c]["first_name"]}")
   time.sleep(1)
   print_ar(f"الاسم الاخير للمستخدم هوا : {users[c]["last_name"]}")
   time.sleep(1)
   print_ar(f"حالة المستخدم :{users[c]["status"]} ")
   print("------------------")
   time.sleep(3)
   clear()
def num3():
 while True:
   clear()
   print_ar("البحث عن المستخدمين عن طريق ؟...")
   print_ar("1- الرقم التعريفي للمستخدم")
   print_ar("2- الاسم الاول ")
   print_ar("3-حالة المستخدم")
   qu = int(input_ar("رجاء اختر طريقة:"))
   if qu == 1:
    ask = input_ar("ادخل الرقمالتعريفي الخاص بالمستخدم رجاء: ")
    if ask in users:
     print_ar(f"الرقم التعريفي للمستخدم هوا: {ask}")
     print_ar(f"الاسم الاول هوا : {users[ask]["first_name"]}")
     time.sleep(1)
     print_ar(f"الاسم الاخير هوا : {users[ask]["last_name"]}")
     time.sleep(1)
     print_ar(f"حالة المستخدم هي  :{users[ask]["status"]} ")
     print("------------------")
     time.sleep(3)
    else:
     print_ar("رقم تعريفي للمستخدم غير صحيح")
     time.sleep(2)
     clear()
     continue
   elif qu ==2:
    ask = input_ar("ادخل الاسم الاول للمستخدم هنا رجاء: ")
    for x in users:
     if ask == users[x]["first_name"]:
      print_ar(f"  الرقم التعريفي للمستخدم هوا  : {x}")
      print_ar(f"الاسم الاول هوا : {users[x]["first_name"]}")
      time.sleep(1)
      print_ar(f"الاسم الاخير هوا : {users[x]["last_name"]}")
      time.sleep(1)
      print_ar(f"حالة المستخدم هي  :{users[x]["status"]} ")
      print("------------------")
      time.sleep(3)
      clear()
     else:
      time.sleep(2)
      clear()
      continue
   elif qu == 3:
    ask = input_ar("ادخل حالة المستخد هنا (active/inactive)?: ")
    for x in users:
     if ask == users[x]["status"]:
      print_ar(f"الرقم التعريفي للمستخدم هوا : {x}")
      print_ar(f"الاسم الاول هوا : {users[x]["first_name"]}")
      time.sleep(1)
      print_ar(f"الاسم الاخير هوا : {users[x]["last_name"]}")
      time.sleep(1)
      print_ar(f"حالة المستخدم هي :{users[x]["status"]} ")
      print("------------------")
      time.sleep(1)
  
while True:
 asks()
 qu = int(input_ar("ادخل اختيارك هنا رجاء: "))
 if qu == 1:
   num1()
 elif qu == 2:
   num2()
 elif qu == 3:
  num3()
 else:
  break
