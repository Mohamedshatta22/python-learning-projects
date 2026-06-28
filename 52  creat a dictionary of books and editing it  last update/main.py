
   import os
def clear():
 os.system("cls") if os.name =="nt" else os.system("clear")
books = {}
def add_a_book():
 while True:
    book_isbn =(input("enter the book isbn: "))
    book_title = input("please type the book title: ")
    book_author = (input("please type the book author: "))
    books[book_isbn]={"title":book_title,"author":book_author,"availability":"True"}
    clear()
    print(f"{books[book_isbn]["title"]} was added successfully the catalog with isbn {book_isbn}..")
    input("press enter here")
    clear()
    new_qu= input("do you want to add another book(y/n)?: ").lower()
    if new_qu=="y":
     continue 
    else:
     clear()
     break
def check_out_book():
 book_isbn =input("please enter the isbn of the book to check out:\n")
 clear()
 while True:
    if book_isbn in books and books[book_isbn]["availability"]== "True" :
     books[book_isbn]["availability"]= "False"
     print(f"book. {books[book_isbn]["title"]} is checked out successfuly")
     new_qu= input("do you want to check out another one (y/n)?: ").lower()
     if new_qu=="y":
      book_isbn =input("please enter the isbn of the book to check out:\n")
      clear()
      continue 
     else:
      clear()
      break
    elif book_isbn in books and books[book_isbn]["availability"]== "False":
     print("this book is checked out already ")
     book_isbn = input("please enter an isbn of an avaliable book or click no to exit: ").lower()
     if book_isbn== "no":
      clear()
      break
     else:
      clear()
      continue
    else:
     print("invalid isbn please retype again.. ")
     book_isbn =input("please enter the isbn of the book to check out:\n")
     clear()
def check_in_book():
 while True:
    book_isbn =input("please enter the isbn of the book to check in: \n")
    clear()
    if book_isbn in books and books[book_isbn]["availability"]== "False" :
     books[book_isbn]["availability"]= "True"
     clear()
     print(f"book. {books[book_isbn]["title"]} is checked in successfuly")
     new_qu= input("do you want to check out another one (y/n)?: ").lower()
     if new_qu=="y":
      book_isbn =input("please enter the isbn of the book to check in:\n").lower()
      clear()
      continue 
     else:
       clear()
       break
    elif book_isbn in books and books[book_isbn]["availability"]== "True":
     print("this book is checked in already ")
     book_isbn = input("please enter an isbn of a non availabe book or click no to exit: ").lower()
     if book_isbn== "no":
      clear()
      break
     else:
      clear()
      continue
    else:
     print("invalid isbn please retype again.. ")
     book_isbn =input("please enter the isbn of the book to check out:\n")
     clear()
 
while True :
 print("book library")
 print("menu")

 print("""1- add a book
2- check out book
3- check in book
4- list book
5- exit """)
 print("please choose a number from 1-5 ")
 qu = int(input())
 clear()
 if qu == 1:
  add_a_book()
 elif qu == 2:
  check_out_book()
 elif qu == 3:
  check_in_book()
 elif qu == 4:
    for x in books:
        print(x)

        input("press enter here")
        clear()
        break
 elif qu == 5:
   print("exiting ... ")
   break
 else :
   print("invalid input exiting now ...")
   break
