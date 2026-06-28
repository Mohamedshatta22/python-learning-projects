import random
import time 
import os
import sys
user_cards = []
pc_cards = []
numbers =[2,3,4,5,6,7,8,9,10,11,10,10,10]
def logo():
     print(""" _                      _                                     
| |                    | |                                    
| |___      _____ _ __ | |_ _   _             ___  _ __   ___ 
| __\ \ /\ / / _ \ '_ \| __| | | |           / _ \| '_ \ / _ \
| |_ \ V  V /  __/ | | | |_| |_| |          | (_) | | | |  __/
 \__| \_/\_/ \___|_| |_|\__|\__, |           \___/|_| |_|\___|
                             __/ |  ______                    
                            |___/  |______|                   """)
def clear():
 os.system("cls") if os.name =="nt" else os.system("clear")
def screen():
     print("chose a game to start")
     print("1- froggy")
     print("2- twenty one")
     print("3- snake")
def giving_cards():
 while True:
    global user_cards
    global pc_cards
    new_man_card = random.choice(numbers)
    new_pc_card = random.choice(numbers)
   
    if sum(user_cards)== 0 :
     user_cards += random.choices(numbers,k=2)
    else :
       if new_man_card == 10:
          if sum(user_cards)==11:
             user_cards.append(new_man_card)
          elif sum(user_cards)<11:
             user_cards.append(10) 
          elif sum(user_cards)>11:
             user_cards.append(1)
             
       else:
          user_cards.append(new_man_card)
     
    if sum(pc_cards)== 0 :
       pc_cards += random.choices(numbers,k=2)
    else :
       if sum(pc_cards)<17:
         if new_pc_card ==10 and new_pc_card+sum(pc_cards)==17:
            pc_cards.append(new_pc_card)
         elif new_pc_card ==10 and new_pc_card+sum(pc_cards)!=17:
           pc_cards.append(1)
         else:
          pc_cards.append(new_pc_card)
    
    print(f"now you have these cards which is {user_cards} ")
    print(f"  the result of your collection is {sum(user_cards)}" )

    print(f"and the pc now has {pc_cards[0]}")
    qu = input("do you wanna take another card: ")
    if qu =="y":
       print("okey waiting.... giving other cards for you and see the pc desicion also..")
       time.sleep(3)
       clear()
       continue
    else:
       break
def calculating_the_cards():
   global user_cards
   global pc_cards
   sum_of_user_cards = sum(user_cards)   
   sum_of_pc_cards = sum(pc_cards) 
   print(f"the result of your cards is {sum_of_user_cards}")
   return sum_of_user_cards,sum_of_pc_cards
def the_result(sum_of_user_cards,sum_of_pc_cards):
    if sum_of_user_cards==21 and sum_of_pc_cards<sum_of_user_cards:
       result = " you won "
    elif sum_of_user_cards<21 and sum_of_pc_cards < sum_of_user_cards:
       result = " you won "
    elif sum_of_pc_cards==21 and sum_of_user_cards< sum_of_pc_cards:
       result="you lost"
    elif sum_of_pc_cards<21 and sum_of_user_cards<sum_of_pc_cards:
       result="you lost"
    elif sum_of_user_cards==sum_of_pc_cards:
       result="its draw"
    elif sum_of_user_cards>21 and sum_of_pc_cards==21:
       result="you lost"
    elif sum_of_user_cards> 21 and sum_of_pc_cards<21:
       result="you lost"
    elif sum_of_pc_cards>21 and sum_of_user_cards==21:
       result="you won"
    elif sum_of_pc_cards >21 and sum_of_user_cards<21:
       result="you won"
    elif sum_of_user_cards>21 and sum_of_pc_cards>21:
       result="both you faild"
    return result
    
def starting_the_game():
  
    while True:
        logo()
        screen()
        qu = input("")
        if qu == "2":
            giving_cards()
            user_sum, pc_sum = calculating_the_cards()
            result = the_result(user_sum, pc_sum)
            print(f"pc got {pc_cards}")
            print(f"the result of the pc cards is {pc_sum}")

            print(result)
            time.sleep(5)
            sys.exit()
        else:
            sys.exit()
      
      
     
     
      

starting_the_game()

