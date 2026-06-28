import random
list =["apple", "mango", "water"]
chosen_word = random.choice(list)
nun_of_words = len(chosen_word)
user_chosen =input("please guess a letter  ")
for x in chosen_word:
 if user_chosen in x:
  print("right")
 else:
  print("wrong")
