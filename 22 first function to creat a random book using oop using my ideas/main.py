def randdom_book():
 import random
 names = ["momo", "meme", "koko"]
 authorties = ["ahmed", "samih", "fayza"]
 pagess = random.randint(0,200)
 class book:
    name =""
    authour = ""
    pages = pagess
 my_book = book()
 my_book.name= random.choice(names)
 my_book.authour= random.choice(authorties)
 my_book.pages= pagess
 print(my_book.name)
 print(my_book.authour)
 print(my_book.pages)
randdom_book()
