from turtle import Turtle,Screen
import pandas
import time
import os 
import sys

the_file = pandas.read_csv("Coordinates.csv")
countries_list = the_file.country.to_list()
screen = Screen()
screen.setup(995,482)
screen.bgpic("map.gif")
screen.title("لعبة اختبار الخرائط")
guessed_countries = 0 
turtle = Turtle()
turtle.penup()
turtle.hideturtle()
def printing_countries(country_data):
    
    x_Coordinate = country_data["x"]
    y_Coordinate = country_data["y"]
    country_name = country_data["country"]
    real_country_name = country_name.iloc[0]
    real_x = x_Coordinate.iloc[0]
    real_y = y_Coordinate.iloc[0]
    return real_x,real_y,real_country_name
# BTW, I used the onclick() method to obtain each coordinate separately,
# one by one, and saved them manually in the Coordinates.csv file.
def write(x,y,z):
   turtle.goto(x,y)
   turtle.write(f"{z}",align="center",font=("arial",20,"normal"))
   
game_on = True
while game_on:
    time.sleep(1.5)
    turtle.clear()
    qu = screen.textinput(f"عدد الدول المخمنةهي {guessed_countries }","من فضلك ادخل اسم دولة ").capitalize()
    if qu in countries_list:
     guessed_countries += 1
     country_data = the_file[the_file.country==qu]
     printing_countries(country_data)
     x,y,z = printing_countries(country_data)
     write(x,y,z)
     countries_list.remove(qu)

    elif qu == "Exit" :
       data = pandas.DataFrame({"countries":countries_list})
       data.to_csv("countries you couldnt guess.csv")
       os.startfile("countries you couldnt guess.csv")
       sys.exit()
       
       
    elif qu not in countries_list:
       turtle.write(f"Sorry, this country is not available here. Please choose another country or type exit to quit.",align="center",font=("arial",20,"normal"))
       time.sleep(2)
    
screen.mainloop()


