import random
print("WELCOME TO MY APP GIVE THE NAMES AND I WILL TELL YOU WHO SHOULD PAY THE DINNER")
names = input("if you are ready give me the names separated by comma and space please\n").lower()
split_names = names.split(", ")
len_split_names = len(split_names)-1
the_number_of_the_people=random.randint(0,len_split_names)
print(f"okay no worries then the dinner on {split_names[the_number_of_the_people]}")
