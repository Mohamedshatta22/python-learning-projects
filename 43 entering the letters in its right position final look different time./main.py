#Wednesday, ‎June ‎10, ‎2026, ‏‎6:55:58 AM
import random
word_list = []
word_list2= []
words =["egypt","syria","milk","coffee"]
random_word = random.choice(words)
print(random_word)

for x in random_word:
    word_list.append(x)
    word_list2.append("_")

while word_list!=word_list2:
    user_input = input("please enter a guessed letter: ")
    if user_input in word_list:
     index = word_list.index(user_input)
     word_list2[index] = ""
     word_list2[index] += user_input
     print(word_list)
     print(word_list2)
