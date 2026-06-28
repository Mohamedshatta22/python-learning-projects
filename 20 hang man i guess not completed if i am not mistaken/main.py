


import random
words = ["apple", "mango", "banana", "water"]
word = []
tries = tries = [
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
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]
wrong_letter=[]
life_tries=7
showing_pic = 0
chosen_word = random.choice(words)
length = len(chosen_word)
for x in chosen_word:
 word+="_"
print(word)
print(chosen_word)
print(tries[0])
while "_" in word and life_tries>0:
  user_letter = input("please enter a letter ") 
  print(f" You more {life_tries} tries.")
  if user_letter in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == user_letter:
                word[i] = user_letter
        print(" ".join(word))
  elif user_letter in wrong_letter: 
      print(f"you enterd this before You still have {life_tries} tries. ")
  else:
        life_tries -= 1
        wrong_letter.append(user_letter)
        print(f"Wrong guess! You lost one try. You still have {life_tries} tries.")
        print(tries[showing_pic])
        showing_pic+=1
        print("".join(word))
      
if "_" not in word:
    print("you won")
else:
    print("you lost")
