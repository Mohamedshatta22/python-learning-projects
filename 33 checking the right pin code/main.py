import random
pc_pin = random.randint(1000,9999)
users_pin = int(input("please enter your pin "))
if users_pin<1000:
    print("you entered less than 4 numbers try again")
elif  users_pin>9999:
    print("you entered more than 4 numbers try again")
elif users_pin == pc_pin :
     print("you entered the right pin code ")
else :
         print("wrong please try again ")
