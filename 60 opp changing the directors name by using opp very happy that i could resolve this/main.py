class movies:
    def __init__ (self,title,director,reales_year,genre):
     self.title = title
     self.director= director
     self.reales_year = reales_year
     self.genre = genre
   
    def changing_names(self,new_name):
       self.director = new_name
       


move1 = movies("inception","christopher nolan","2010","sci_fi")
move2 = movies("the god father","francis ford coppola","1972","crime")
move3 = movies("parasite","boong joon-ho","2019","thriller")
moveeeee = [move1,move2,move3]
for movee in moveeeee:
    print("...move list....")
    print(f"title:{movee.title}")
    print(f"director: {movee.director}")
    print(f"reales year: {movee.reales_year}")
    print(f"genre{movee.genre}")
    print("\n")
move1.changing_names("shokry sarhan") 
move2.changing_names("ahmed mazhar") 
move3.changing_names("ismail yassin") 
print("after changing the directors>>>>")
print("\n")
for movee in moveeeee:
    print("...move list....")
    print(f"title:{movee.title}")
    print(f"director: {movee.director}")
    print(f"reales year: {movee.reales_year}")
    print(f"genre{movee.genre}")
