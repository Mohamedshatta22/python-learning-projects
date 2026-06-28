owned_library=[]
wish_list=[]
add_books = input("enter the name of the book you own /n")
add_books2 = input("enter the name of another book you own or pres enter to skip /n")
if add_books2:
    owned_library.append(add_books)
    owned_library.append(add_books2)
    print(f"you library now has {owned_library} ")
elif add_books:
     owned_library.append(add_books)
     print(f"you library now has {owned_library} ")
else:
    print("its okay ")
add_wish_books = input("add the name of a book you wish to have in the future")
add_wish_books2 = input("add the name of another book you wish to have in the future or press enter to skip")
if add_wish_books2:
    wish_list.append(add_wish_books)
    wish_list.append(add_wish_books2)
    print(f"you library now has {wish_list} ")
elif add_wish_books:
     wish_list.append(add_wish_books)
     print(f"you library now has {wish_list} ")
else:
    print("its okay ")
acquired_books = input("enter a name of a book from your wish list that you have acquired or press enter to skip")
if acquired_books in wish_list:
    wish_list.remove(acquired_books)
    owned_library.append(acquired_books)
    print(f"""your updated list
          1- your library books {owned_library}
          2- your wish list books {wish_list}
""")
else:
    print("its okay then")
donated_books = input("enter a name of a book from you library you wish to donate so soon or press enter to skip")    
if donated_books in owned_library:
    owned_library.remove(donated_books)
    print(F"your final library is {owned_library}")
else:
    print(f"""its okay then your final update 
          {owned_library}
          {wish_list}""")
------------------------------------------------------------------


own_books = []
wish_list = [] 
qu = input("enter a name of a book u own now ")
own_books.append(qu)
qu = input("enter a name of another book u have or press enter to skip ")
if qu:
    own_books.append(qu)
    print(f"now your books list are {own_books}")
else:
    print("")

qu = input("enter a name of a book u wish to have in the future ")
wish_list.append(qu)
qu = input("enter a name of another book u wish to have or press enter to skip ")
if qu:
    wish_list.append(qu)
    print(f"now your wish list books are {wish_list}")
else:
    print("")
qu = input("enter a name from you wish list that u have acquired or press enter to skip ")
if qu:
    wish_list.remove(qu)
    own_books.append(qu)
    print(f"now your wish list books are {wish_list}")
    print(f"now your books list are {own_books}")
else:
    print("")
qu = input("enter a name from you book list you wish to donate or press enter to skip ")

if qu:
    own_books.remove(qu)
    print(f"now your wish list books are {wish_list}")
    print(f"now your books list are {own_books}")
else:
    print("")



    
