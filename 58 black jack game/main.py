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
