#Saturday, ‎August ‎2, ‎2025, ‏‎5:34:59 PM

import random
pc_chosen = random.randint(0,2)
choices= ["paper", "rock", "scissors"]
list =["""  _____
---'    __)____
           ____)
          _____)
         _____)
---.__________)""", """ _____
---'   __)
      (___)
      (___)
      (__)
---.__(_)""", """ _____
---'   __)____
          ____)
       ________)
      (__)
---.__(_)"""]
print("welcome to paper rock and scissors game ")
man = input("press enter to continue or type help for some rules").lower()
if man:
    print("****rules****\n1:you chose then the pc chosese\n2:rock smashes scissors -> rock wins\n3:scissors cut paper -> scissors win\n4:paper covers rock -> paper wins ")
choice = input("now please chose between rock paper scissors \n").lower() 
if pc_chosen==0 and choice =="rock" or pc_chosen==1 and choice =="scissors" or pc_chosen==2 and choice =="paper":
   result="you lost and the pc beat u"
elif pc_chosen==0 and choice =="scissors" or pc_chosen==1 and choice =="paper" or pc_chosen==2 and choice =="rock":
   result="you won u beat the pc"
else:
    result="its a draw"
if choice=="paper":
   print("you chosed paper")
   print(list[0])
elif choice=="rock":
    print("you chosed rock")
    print(list[1])
else:
     print("you chosed scissors")
     print(list[2])
print(f"pc chosed {choices[pc_chosen]} ")
print(list[pc_chosen])
print(result)
---------------------------------------------------
#Saturday, ‎March ‎28, ‎2026, ‏‎12:47:39 PM
import random
choices= ["paper", "rock", "scissors"]
list =["""  _____
---'    __)____
           ____)
          _____)
         _____)
---.__________)""", """ _____
---'   __)
      (___)
      (___)
      (__)
---.__(_)""", """ _____
---'   __)____
          ____)
       ________)
      (__)
---.__(_)"""]
pc_chosen_number= random.randint(0,2)
print("welcome to paper rock and scissors game ")
help = input("press enter to continue or type help for some rules ").lower()
if help:
 print("****rules****\n1:you chose then the pc chosese\n2:rock smashes scissors -> rock wins\n3:scissors cut paper -> scissors win\n4:paper covers rock -> paper wins ")
user_choice = input("now please chose between rock paper scissors \n").lower() 
if user_choice == "paper" and pc_chosen_number ==2 or user_choice == "rock" and pc_chosen_number ==0 or user_choice == "scissors" and pc_chosen_number ==1:
 result = " u lose "
elif user_choice == "paper" and pc_chosen_number ==1 or user_choice == "rock" and pc_chosen_number ==2 or user_choice == "scissors" and pc_chosen_number ==0:
 result = "u win"
else :
 result = "draw"
print(f"you chosed {user_choice}")
index = choices.index(user_choice)
print(list[index])
print("")
print(f"pc chosed {choices[pc_chosen_number]}")
print(list[pc_chosen_number])
print(result)




