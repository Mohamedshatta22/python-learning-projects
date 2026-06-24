import os
import time
import random

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
def clear_the_screen():

     if os.name=="nt":
          os.system("cls")
     else:
          os.system("clear")
def screen():
     print("chose a game to start")
     print("1- froggy")
     print("2- twenty one")
     print("3- snake")
while True:
 screen()
 game_choose = int(input(""))
 if game_choose ==2:
     clear_the_screen()
     print("starting game .....")
     time.sleep(3)
     clear_the_screen()
     logo()
     time.sleep(1)
     pc_papers = random.choices(numbers, k=2)
     man_papers = random.choices(numbers, k=2)
     print(f"your cards are {man_papers} current score is {sum(man_papers)} ")
     print(f"computers first card is {pc_papers[0]}")
     getting_card = input("get another card y/n: ")
     while getting_card == "y":
          new_card_for_men = random.choice(numbers)
          man_papers.append(new_card_for_men) 
          if new_card_for_men == 11 and sum(man_papers)>21 :
             ace_index = man_papers.index(11)
             man_papers[ace_index] = 1
          print(f"your cards are {man_papers} current score is {sum(man_papers)} ")
          print(f"computers first card is {pc_papers[0]}")
          getting_card = input("get another card y/n: ")
          clear_the_screen()
     while sum(pc_papers) < 17:
          new_card_for_pc = random.choice(numbers)
          pc_papers.append(new_card_for_pc)
     if sum(man_papers) > sum(pc_papers) :
         if sum(man_papers) >21:
            result = "you lost "
         elif sum(man_papers) <=21:
             result = "congratulation u won "
         
     elif sum(man_papers) < sum(pc_papers):
          if sum(pc_papers) >21:
            result = "you won "
          elif sum(pc_papers) <=21:
             result = "you lost "

     
     print(f"your cards are {man_papers} current score is {sum(man_papers)} ")
     print("")
     print(f"the pc cards are  {pc_papers} current pc score is {sum(pc_papers)} ")
     print(f"the result is {result} ")
     play_again = input("do you want to go to the main menu again y/n:  ")
     if play_again == "y":
         print("getting the game ready again for you please wait...")
         time.sleep(2)
         clear_the_screen()
     else:
         clear_the_screen()
         break
-------------------------------------- 
اخر تحديث تاني بعد ما رجعت اخد الكورس مع ملاحظة اخطاء في النسخة القديمة كمان  تم الانتهاء من النسخة الجديدة بتاريخ 2026 شهر 6 يوم #19##

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

