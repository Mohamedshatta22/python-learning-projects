import string
sentence = input("please enter a sentence here ")
new_sentence=''
puncitaion_check = string.punctuation
for c in sentence:
    if c not in puncitaion_check:
        new_sentence+=c
     
print(new_sentence)
