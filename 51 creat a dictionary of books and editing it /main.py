import os
def clear_the_screen():

     if os.name=="nt":
          os.system("cls")
     else:
          os.system("clear")
def print_screen():
    print("1- add book")
    print("2- check out book")
    print("3- check in book")
    print("4- list book")
    print("5- exit")
def add_book():
    while True:
        clear_the_screen()
        ISBN_book = input("enter please book ISBN: ")
        title_of_book = input("enter the title: ")
        name_of_autour = input("enter the name of the authour: ")
        books[ISBN_book]={
            "title":title_of_book, 
            "autour":name_of_autour, 
            }
        print(f"the book {books[ISBN_book]["title"]} by {books[ISBN_book]["autour"] } added to the catalog with ISBN {ISBN_book} ")
        exit_que = input("do you want to add another book y/n: ")
        if exit_que.lower() == "y":
                clear_the_screen()
                continue 
        elif exit_que.lower() == "n":
                clear_the_screen()
                break  
        else:
                print("invalid choice, returning to main menu...")
                break
def check_out_book():
     while True :
        askin_ISBN = input("please enter the ISBN book that you want to check out: : ")
        if askin_ISBN in books:
         print(f"the book {books[askin_ISBN]["title"]} checked out successfully ")
         books_2[askin_ISBN] = {}
         books_2[askin_ISBN]["title"]=books[askin_ISBN]["title"]
         books[askin_ISBN]["title"] = ""
         exit_que = input("do you want to check out another book y/n: ")
         if exit_que.lower() == "y":
                clear_the_screen()
                continue 
         elif exit_que.lower() == "n":
                clear_the_screen()
                break  
        else:
             clear_the_screen()
             print("invalid choice, returning to main menu...")
             break
def check_in_book():
     while True:
         askin_ISBN = input("please enter the ISBN book that you want to check in: ")
         if askin_ISBN in books:
             
             books[askin_ISBN]["title"]=books_2[askin_ISBN]["title"]
             print(f"your book {books[askin_ISBN]["title"]}  has been returned successfuly")
             exit_que = input("do you want to check in another book y/n: ")
         if exit_que.lower() == "y":
                clear_the_screen()
                continue 
         elif exit_que.lower() == "n":
                clear_the_screen()
                break  
         else:
            print("invalid choice, returning to main menu...")
            break
books = {}
books_2={}
while True:
      print_screen()
      user_choice = int(input("please enter your choice here: "))
      if user_choice==1:
       add_book()
      elif user_choice==2:
       check_out_book()
      elif user_choice==3:
        check_in_book()
      elif user_choice ==4:
          clear_the_screen()
          for x in books:
           print(f"the isbn book is {x} the name of the book is {books[x]["title"]} written by {books[x]["autour"]} ")
      else:
          break   
