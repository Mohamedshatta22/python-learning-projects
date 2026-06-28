#حلي انا اخيرا بعد البحث و الفهم
list = []
words = input("please enter a sentence here ").split(" ")
num_of_words = len(words)
for x in range(-1,-num_of_words-1,-1):
    list.append(words[x])
print(" ".join(list))
    
