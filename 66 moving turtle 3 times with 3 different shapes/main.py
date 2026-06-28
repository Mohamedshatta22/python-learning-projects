import random
from turtle import Turtle,Screen
dudu = Turtle() 
dudu.color("white")
dudu.shapesize(2)
dudu.speed("fastest")
Window= Screen()
Window.setup(1000,1000)
Window.bgcolor("black")
def move_in_cirlce(turtle_name):
    for _ in range(20):
      turtle_name.penup()
      turtle_name.goto(-350,-350)
      turtle_name.pendown()
      turtle_name.circle(50)
      turtle_name.left(20)
    turtle_name.penup()
    turtle_name.goto(0,0)
    turtle_name.pendown()
def move_tringle(turtle_name):
   for _ in range(40):

    for _ in range(4):
       turtle_name.forward(100)
       turtle_name.left(90)
    turtle_name.left(10)
def move_in_square(turtle_name):
   turtle_name.penup()
   turtle_name.goto(350,350)
   turtle_name.pendown()
   for _ in range(20):
      turtle_name.left(20)
      for _ in range(3):
        turtle_name.forward(100)
        turtle_name.left(120)
