import random 
import os
random_unm = random.randint(1,10)
#طابع الرقم بس عشان اتاكد ان الكود شغال في الحالتين 
print(random_unm)
while True:
    user_num = int(input("guess the number between 1:10 "))
    if user_num!=random_unm:
        print("wrong guess press any key to continue")
        input("")
        os.system("cls")
    else:
        break
print("congratulation you guessed the right number")
