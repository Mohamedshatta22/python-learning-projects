import random
list =["apple", "mango", "water"]
chosen_word = random.choice(list)
little_list=[]
length = len(chosen_word)
print(chosen_word)
for m in chosen_word:
    little_list.append("_")
while little_list[length-1] !=chosen_word[length-1]:
 user_chosen =input("please guess a letter  ").lower()
 for x in range(len(chosen_word)):
    if chosen_word[x] == user_chosen:
        little_list[x] = user_chosen
        print(little_list)
print("congratulation u finished ")
