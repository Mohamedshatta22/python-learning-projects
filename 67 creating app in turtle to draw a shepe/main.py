import os
import time
import random
def clear():
 os.system("cls") if os.name =="nt" else os.system("clear")
from turtle import Turtle,Screen
dudu = Turtle() 
dudu.color("white")
dudu.shapesize(2)
dudu.shape("turtle")
Window= Screen()
Window.setup(1000,1000)
Window.bgcolor("black")
def move_in_cirlce(turtle_name):
    turtle_name.shape("turtle")
    turtle_name.color("white")
    for _ in range(1):
      turtle_name.circle(50)
def move_square(turtle_name):
  turtle_name.shape("circle")
  turtle_name.color("pink")
  for _ in range(4):
    turtle_name.forward(100)
    turtle_name.left(90)
    
def move_in_tringle(turtle_name):  
  turtle_name.color("red") 
  for _ in range(3):
    turtle_name.forward(100)
    turtle_name.left(120)
while True:
 
 result = Window.textinput(title="ادخل جملتك هنا",prompt=("رجاء اختار بين مربع او مثلث او دائرة"))
 if result=="مربع":
  move_square(dudu)
  time.sleep(1)
  continue
 elif result == "مثلث":
  move_in_tringle(dudu)
  time.sleep(1)
  continue
 elif result=="دائرة":
   move_in_cirlce(dudu)
   time.sleep(1)
   continue
 elif result == "اخرج":
   dudu.clear()
   dudu.hideturtle()
   dudu.write("اضغط علي اي مكان للخروج",font=("arial",40,"bold"), align ="center")
   Window.exitonclick()
 else:
   continue
