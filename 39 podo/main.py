import random
ran = random.randint(0,1)
pc_num3 = random.randint(1,10)
result=""
countries=["syria", "egypt"]
sep = []
li= []
ind = [] 
tries =7
pc_chosen = random.choice(countries)
len_word = int(len(pc_chosen))
for letters in pc_chosen:
   sep +=letters
   ind +="_"
try6 = """ 
  +---+
  |   |
      |
      |
      |
      |
=========''', '''"""
try5="""
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''"""
try4=""" 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''"""
try3="""  
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''"""
try2=""" 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''"""
try1=""" 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''"""
try0="""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']"""
print("welcome to my game")
print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⠀⠀⢀⣠⣤⣶⣶⣶⣶⣶⣶⣶⣦⣤⣀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡔⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣫⣯⣷⣾⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣷⡙⢿⣿⣿⣿⣿⣿⣿⡿⢋⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣙⠿⠿⠿⢟⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡏⠉⠙⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⡿⡍⠳⣄⡀⢀⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⢿⡄⠸⡿⢄⠛⣘⢠⣼⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡞⣼⡻⡄⠳⡤⠽⠾⠿⠿⠿⢛⣻⣿⣿⣿⣷⡀⠀⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣄⠙⢶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀
⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⢉⣁⣀⣀⣀⣀⣀⣉⡉⠙⠛⠻⢿⣿⣿⣿⣿⣿⣯⣻⣍⡲⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⢀⡀⣶⣤⣌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⣁⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣈⠛⢿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⡿⠟⠛⠛⠁⠀⠀
⣰⣿⣿⣿⣿⣿⣿⣿⣝⢿⣿⣿⣿⣿⣿⣿⣟⣡⣶⠿⢛⣛⣉⣭⣭⣤⣤⡴⠶⠶⠶⠶⢲⣴⣤⠭⠭⡭⣟⠻⠦⣝⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⣀⣠⣶⣿⣆⠀⠀
⠹⣿⣿⣿⣿⣿⣿⣙⠻⣿⣮⣛⠿⣿⣿⣿⣫⣵⡶⠟⣛⣋⣭⣭⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣮⣽⣿⣿⣿⠿⠟⠛⠉⢀⣴⣿⣿⣿⣿⣿⣿⣶⡀
⠀⠈⠙⠋⠁⠀⠈⠉⠛⠳⣭⣛⢷⣦⣸⣿⣯⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⡟⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⠿⠿⢿⣹⣿⣧⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⡏⣀⣴⣾⣿⣿⠿⠛⠉⠀⠀⠀⠈⠛⠛⠉⠀
⠀⠀⠀⠀⢀⣴⠿⠛⠋⠁⠀⠀⠀⢀⣯⢿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⠣⣟⡻⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⣀⣴⣾⣿⠈⡿⣿⠃⠀⠀⠀⠈⠉⠛⠻⠿⣿⣿⣿⣿⣿⠿⠛⠉⠉⠀⠈⠉⠛⣿⣽⡟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣤⣶⣾⣿⣿⣿⣿⣿⣀⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣹⡟⣻⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⢹⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⣰⣿⢣⡇⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠟⠋⠙⠛⠻⣿⣿⣿⣿⣿⠏⠀⠈⢿⣿⣿⣿⣦⣄⣀⣀⣀⣠⣴⣿⣏⡞⢻⣸⣿⣷⣄⠀⠀⣀⣤⠴⣾⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⠃⠀⠀⠀⠈⢿⣿⣵⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣶⠾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣏⠀⠀⠀⠀⠀⣀⣼⣿⡛⢿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠟⣡⣾⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⢠⣶⣿⣿⣯⣿⡇⠀⢹⣿⣿⣿⣿⣷⣤⣤⣦⣶⣿⣿⣿⣿⣿⡇⠀⣿⣿⢸⣿⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣠⣴⣾⣿⣟⣿⠟⠁⣿⡇⠀⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⡇⢀⣿⣿⠙⢮⣛⠿⣷⣦⣄⣀⣀⣀⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣶⣶⣾⣿⣿⡿⣛⣽⠞⠋⠀⠀⠀⣿⣷⠀⣍⠇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠉⡄⣸⣿⡿⠀⠀⠈⠙⠮⣟⠿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣹⣿⣿⣿⢵⡿⠋⠀⠀⠀⠀⠀⠀⢿⣿⣦⣿⡷⣄⠙⠿⣿⢹⣿⣿⢼⡿⠋⣡⣶⣳⣿⣿⣿⠃⠀⠀⠀⠀⠀⠈⠿⠬⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣷⣻⢿⣶⣬⣈⣉⣉⣤⣴⣿⣻⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⡇⣿⣇⣿⢹⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⡿⠏⠀""")
user_name =input("may i lnow your name please ")
print(f"""now {user_name} you are walking with your gf ashley she is 18 years old ans she lives in syria or egypt you still dont know and sudenly she was kidnaped by some body gaurds
       and then they escaped so fourtunately you could know her location but the location 
       did not give you wich house you should enter so you are standing now in front of 3 houses a red one and blue one and a black one""")
#red هوا البيت الصحيح
chosen_house =input("wich one will you choose to go in \n").lower()
if chosen_house=="red":
   print(" great and now there are 2 doors in front of you a red door 🚪 and blue one 🚪 ")
   chosen_door = input("wich one will you chose to open \n").lower()
   # الباب الازرق هوا الي بيدخل علي البودي جارد
   if chosen_door == "blue": 
     print("great you entered a room")
     print(f"""and in front of you a very mad bodygaurd and he says
     if you want to pass you have to win him in toss coin game if you win you pass if you dont
     you are died""")
     print("type 1 to start")
     
     user_choise = int(input())
     user_choise_face =input("enter what do you choose head or tales ").lower()
     if user_choise ==  1 and ran ==0:
         pc_choise = "head"
     elif user_choise==1 and ran ==1: 
         pc_choise = "tales"
     if user_choise_face == pc_choise:
       print(f"you won the coin is{pc_choise}")
       print(f"""now the bodygaur let you in and noy you are in front of a door
             and be side this door you saw the son of the kidnaper and he told you if you want to
             pass you have to beat him first in paper rock and scissors""")
       while result!="won":
                     pc_choice2 = random.randint(0,2)
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
                     starting = input("press enter to continue or type help for some rules").lower()
                     if starting:
                       print("****rules****\n1:you chose then the pc chosese\n2:rock smashes scissors -> rock wins\n3:scissors cut paper -> scissors win\n4:paper covers rock -> paper wins ")
                     else:
                       print("okay")
                     choice = input("chose between rock paper scissors \n").lower() 
                     if choices[pc_choice2]==choice:
                        result= "draw"
                     elif choices[pc_choice2] == "paper" and choice == "scissors" or \
                          choices[pc_choice2] == "rock" and choice == "paper" or \
                          choices[pc_choice2] == "scissors" and choice == "rock":
                            result="won"
                     else: 
                       result="lost"
                     if choice=="paper":
                       image=("""---'    __)____
           ____)
          _____)
         _____)
---.__________)""")
                     elif choice == "rock":
                         image=("""""_____
---'   __)
      (___)
      (___)
      (__)
---.__(_)""""")

                     else:
                        image=(""""_____
---'   __)____
          ____)
       ________)
      (__)
---.__(_)
     """)
       
                     print(f"you chosed")
                     print(f"{image}")
                     print("the kid also chosed")
                     print(list[pc_choice2])
                     print(f"you {result}")
     
       if result=="won":
           print(f"""now finally you could beat this naught chiled
                 and you passed the door and while walking you saw another door
                 but this time no one stays beside the door
                 you tried to open it but unf
                 its locked you have to enter a password to the door to open it and you tried many times but you 
                 couldnt and sud an old wise man passed beside you and told
                 i can help you but undirectly if you want and you still a few times 
                 before it locks forever""")
           answer=input("do you want my help son ? (yes/no) ")
           if answer == "no":
               print("okay then continu alone bitch")
               print(pc_num3)
               num3 = int(input("guess the number between 1:10 "))
               for b in range(1,3):
                 if num3!=pc_num3:
                     print(f"you are losing again and now you are alone because you refused the old man to help you now you still have {b} tries")
                     num3 = int(input("guess the number between 1:10 "))
                 else:
                    print("you lost")
           else:
              print("for sure my son i am going to help you")  
              num3 = int(input("guess the number between 1:10 ")) 
              for t in range(0,10):
               if pc_num3>num3:
                 print(" hhhhhhh oops thats too low try to guess again")
                 num3 = int(input(""))
               elif pc_num3<num3:
                 print("oops hhhhhh thats too high try to guess again")
                 num3 = int(input(""))
               else:
                  print(f"""you won my son coungratulation now the door is open now you entered the room 
                        and you saw something unbeliveble you saw your woman finally but this
                        time you saw her while she is hanged and the kidnaper is standing there
                        telling you hey {user_name} you are here 
                         and it seems like you want to get your woman back i will only 
                          give her back to you if you guessed this work corectly otherwise
                           she will die you only got 6 tries now you need to write your woman 
                            country if you love her you will remember it since
                             the first game and it consists of {len_word} words """)
                  while sep!=ind and tries >0:
                    user_choise=input("please choose a littre ").lower()
                    if user_choise not in pc_chosen and tries==7:
                     tries-=1
                     print(f"you lost a try of 6 tries you still have {tries} {try6}")
                    elif user_choise not in pc_chosen and tries==6:
                     tries-=1
                     print(f"you lost a try of 6 tries you still have {tries} {try5}")
                    elif user_choise not in pc_chosen and tries==5:
                     tries-=1
                     print(f"you lost a try of 6 tries you still have {tries} {try4}")
                    elif user_choise not in pc_chosen and tries==4:
                     tries-=1
                     print(f"you lost a try of 6 tries you still have {tries} {try3}")
                    elif user_choise not in pc_chosen and tries==3:
                     tries-=1
                     print(f"you lost a try of 6 tries you still have {tries} {try2}")
                    elif user_choise not in pc_chosen and tries==2:
                     tries-=1
                     print(f"you lost a try of 6 tries you still have {tries} {try1}")
                    elif user_choise not in pc_chosen and tries==1:
                     tries-=1
                     print(f"you lost a try of 6 tries you still have {tries} {try0}")   
                    else:
                     for m in range(0,len_word):
                      if pc_chosen[m]==user_choise:
                       ind[m] = user_choise
                       print(ind) 
                  if tries==0:
                   print("unfo you lost")
                  else:
                     print(f"you won {user_name} congratulation here you are taking your woman back")

              
           
                     

     else:
        print(f"you lost the coin is {pc_choise}")
   else:
      print("you choesed a bears door you are dead")
elif chosen_house=="blue":
   print(' you chose the crocodile house🐊🐊🐊')
elif chosen_house=="black":
   print(' you chose the killer house you are dead now ')
else:
  print("invalide house")
