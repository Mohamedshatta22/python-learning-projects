my soluation

import random
list =["apple", "mango", "water"]
chosen_word = random.choice(list)
little_list=[]
length = len(chosen_word)
print(chosen_word)
for m in chosen_word:
    little_list.append("_")
while "_" in little_list and length > 0 :
 user_chosen =input("please guess a letter  ").lower()
 if user_chosen in chosen_word:
  for x in range(len(chosen_word)):
    if chosen_word[x] == user_chosen:
        little_list[x] = user_chosen
        print(little_list)
    else:
        length -= 1
        print(f"Wrong guess! You lost one try. You still have {length} tries.")

print("congratulation u finished ")
--------------------------------
AI one + MINE 
import random

list = ["apple", "mango", "water"]
chosen_word = random.choice(list)
little_list = []
length = len(chosen_word)

print(chosen_word)

for m in chosen_word:
    little_list.append("_")

while "_" in little_list and length > 0:
    user_chosen = input("please guess a letter  ").lower()

    if user_chosen in chosen_word:
        for x in range(len(chosen_word)):
            if chosen_word[x] == user_chosen:
                little_list[x] = user_chosen
        print("_".join(little_list))
    else:
        length -= 1
        print(f"Wrong guess! You lost one try. You still have {length} tries.")

print("congratulation u finished ")
