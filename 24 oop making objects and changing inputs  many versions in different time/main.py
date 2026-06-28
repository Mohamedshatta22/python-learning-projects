class email:
    def __init__(self,messnger_name, sender_name, date, time, content, status):
        self.messnger_name=messnger_name
        self.sender_name=sender_name
        self.date=date
        self.time=time
        self.content=content
        self.status = status
    def changing_status(self):
          if self.status=="yes":
            self.status = "no"
    def display_task(self):
        print(self.messnger_name)
        print(self.sender_name)
        print(self.date)
        print(self.time)
        print(self.content)
        print(self.status)
    

mohamed = email("mohamed", "ahmed", "2024/05/22", "2024/05/23", "how are you doing", "yes")

print(mohamed.display_task())
print(mohamed.changing_status())
print(mohamed.display_task())
----------------------------------------------------------


class novels:
    def __init__(self, title, dircetor, releas_year, genre):
        self.title= title
        self.dircetor= dircetor
        self.releas_year= releas_year
        self.genre= genre
    def changing(self):
      if self.dircetor=="chris meme":
         self.dircetor="shokry sarhan"
      if self.dircetor=="frans fors":
         self.dircetor="ahmed mazhar"
      if self.dircetor=="bong jong":
         self.dircetor="ismail yassin"
    def printing_book(self):
        print(f"the book is {self.title}")
        print(f"the name of the director is {self.dircetor}")
        print(f"realeas year {self.releas_year}")
        print(f"type of the book {self.genre}")

book1 = novels("inception", "chris meme", 2010, "sci fi")
book2 = novels("good father", "frans fors", 1972, "crime")
book3 = novels("baraside", "bong jong", 2019, "thriller")

print(book1.printing_book())
print(book1.changing())
print()
print(book2.printing_book())
print(book2.changing())
print()

print(book3.printing_book())
print(book3.changing())
print()
print("changing move directors.....")
print()
print(book1.printing_book())
print()
print(book2.printing_book())
print()
print(book3.printing_book())
-----------------------------------------


class novels:
    def __init__(self, title, dircetor, releas_year, genre):
        self.title= title
        self.dircetor= dircetor
        self.releas_year= releas_year
        self.genre= genre
    def changing(self,new_director):
        self.dircetor=new_director
      
    def printing_book(self):
        print(f"the book is {self.title}")
        print(f"the name of the director is {self.dircetor}")
        print(f"realeas year {self.releas_year}")
        print(f"type of the book {self.genre}")

book1 = novels("inception", "chris meme", 2010, "sci fi")
book2 = novels("good father", "frans fors", 1972, "crime")
book3 = novels("baraside", "bong jong", 2019, "thriller")

print(book1.printing_book())
print(book1.changing(new_director="shokry sarhan"))
print()
print(book2.printing_book())
print(book2.changing(new_director="ahmed helmy"))
print()

print(book3.printing_book())
print(book3.changing(new_director="ahmed el saqa"))
print()
print("changing moveies directors.....")
print()
print(book1.printing_book())
print()
print(book2.printing_book())
print()
print(book3.printing_book())

