import random
countries=["egypt", "malay", "indonsia", "libya", "moroco", "mozambiq"]
sep = []
li= []
ind = [] 
pc_chosen = random.choice(countries)
len_word = int(len(pc_chosen))
len_word2 = int(len(pc_chosen))
print(pc_chosen)
sep.append(pc_chosen)
for x in range(0,len_word):
   li.append(sep[0][x])
for m in range (0,len_word):
   ind +="_"
while len_word2+1<len_word+len_word:
   user_choise=input("please choose a littre ").lower()
   if user_choise not in li:
      len_word2 +=1
      print("wrong please choose a littre ")
   else:
        print(user_choise)
        ind.remove("_")
        ind+=user_choise
        len_word2+=1
        print(ind)
_________________________________________________________________
import random
countries=["egypt", "malay", "indonsia", "libya", "moroco", "mozambiq"]
sep = []
#sep = pc choise
li= []
# li = litters of pc choise
ind = [] 
tries =6
pc_chosen = random.choice(countries)
len_word = int(len(pc_chosen))
for letters in pc_chosen:
   sep +=letters
   ind +="_"
print(pc_chosen)
print(sep)
print(ind)
while sep!=ind and tries >0:
  user_choise=input("please choose a littre ").lower()
  for m in range(0,len_word):
    if pc_chosen[m]==user_choise:
      ind[m] = user_choise
      print(ind) 
  
   
print(f""" ****************
               you won
              *********""")
__________________________________________________________
import random
countries=["egypt", "syria", "libya", "moroco", "mozambiq"]
sep = []
#sep = pc choise
li= []
# li = litters of pc choise
ind = [] 
tries =7
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
pc_chosen = random.choice(countries)
len_word = int(len(pc_chosen))
for letters in pc_chosen:
   sep +=letters
   ind +="_"
print(ind)
print(f"the name of the country consists of {len_word} litters")
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
   print("you won")

---------------------------------
#Thursday, ‎June ‎11, ‎2026, ‏‎7:19:33 AM
# اخر تحديث
 try1 = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]
import random
guessd_letter =[]
word_list= []
words =["egypt", "malay", "indonsia", "libya", "moroco", "mozambiq"]
random_word = random.choice(words)
print(random_word)
lifes = 6
killed=0
word_list2 = ["_"] *len(random_word)
for x in random_word:
    word_list.append(x)
len_list = len(word_list)
print(f"{try1[0]}")
while word_list != word_list2 and lifes!= 0 :
    user_input = input("please enter a guessed letter: ")
    if user_input in word_list:
     if user_input in guessd_letter:
        print("u alreadyy guessd this before")
        print(f"u have more {lifes} tries ")
        continue
     guessd_letter+=user_input
     
     for index in range(len(word_list)):
        if word_list[index] == user_input:
         word_list2[index] = user_input
     print("".join(word_list2))
     print(f"u have more {lifes} tries ")
    else :
       lifes+=-1
       killed+=1
       print(f"u have more {lifes} tries ")
       print(f"{try1[killed]}")
if word_list == word_list2:
   print("congratulation u  won")
else:
   print("the dummy died i am sorry ")
