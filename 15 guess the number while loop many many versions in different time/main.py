import random
pc_num = random.randint(1,10)
num = int(input("guess the number between 1:10 "))

while num != pc_num:
    if pc_num>num:
        print(" hhhhhhh oops thats too low try to guess again")
        num = int(input(""))
    else:
        print("oops hhhhhh thats too high try to guess again")
        num = int(input(""))
print("coungratulation you guessed the same number")
----------------------------------------------
pc_chosen = 6
user_number =int(input("guess a number between 1:10 "))
while pc_chosen != user_number:
   if pc_chosen>user_number:
      print("too low guess again")
      user_number =int(input("guess a number between 1:10 "))
   else:
       print("too high guess again")
       user_number =int(input("guess a number between 1:10 "))

print("thats correct") 
