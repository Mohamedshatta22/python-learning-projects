import os
import time
import random
def clear():
 os.system("cls") if os.name =="nt" else os.system("clear")
from turtle import Turtle,Screen
possitions = [(-40,0),(-20,0),(0,0),(20,0),(40,0),(60,0),(80,0)]
angles = [90,0,0,0,0]
colors =("white","white","white","white","white","white","white")
turtles = []
window = Screen()
window.setup(1000,1000)
window.bgcolor("black")


for x in range(len(possitions)):
 if x ==6:
  new_turtle = Turtle("circle")
  new_turtle.color(colors[x])
  new_turtle.penup()
  new_turtle.goto(possitions[x])
  turtles.append(new_turtle)
 else:
  new_turtle = Turtle("square")
  new_turtle.color(colors[x])
  new_turtle.penup()
  new_turtle.goto(possitions[x])
  turtles.append(new_turtle)

 
game = True
while game:
 window.update()
 time.sleep(0.1)
 for i in range(len((turtles))-1):
  turtles[i].goto(turtles[i+1].pos())
 turtles[-1].forward(20)
 turtles[-1].left(random.choice(angles))
 
 

window.exitonclick()
