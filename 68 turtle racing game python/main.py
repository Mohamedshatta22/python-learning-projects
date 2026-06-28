import os
import time
import random
def clear():
 os.system("cls") if os.name =="nt" else os.system("clear")
from turtle import Turtle,Screen
speed = ("fastest","fast","slowest","slow")
move = (1,2,3,4,5,6,7,8,9)
dudu = Turtle() 
bubu = Turtle()
ahmed = Turtle()
dudu.color("pink")
dudu.penup()
dudu.goto(-480,300)
dudu.shape("turtle")
bubu.color("red")
bubu.shape("turtle")
bubu.penup()
bubu.goto(-480,0)
ahmed.color("blue")
ahmed.shape("turtle")
ahmed.penup()
ahmed.goto(-480,-300)
window = Screen()
window.setup(1000,1000)
window.bgcolor("black")
def turtle_move(turtle_name):
    turtle_name.speed(random.choice(speed))
    turtle_name.forward(random.choice(move))
    return turtle_name.xcor()

distance_dudu = 0
distance_bubu = 0
distance_ahmed = 0
qu = window.textinput("ادخل من فضلك","اي من السلاحف سيكسب بوبو ام دودو او احمود")
while True:
  distance_dudu=turtle_move(dudu)
  if distance_dudu>=480:
    result = "دودو"
    break
  distance_bubu=turtle_move(bubu)
  if distance_bubu>=480:
    result = "بوبو"
    break
  distance_ahmed=turtle_move(ahmed)
  if distance_ahmed>=480:
    result = "احمود"

    break
time.sleep(2)
if qu == result:
  window.clear()
  window.bgcolor("black")
  dudu.penup()
  dudu.goto(0,0)
  dudu.pendown()
  dudu.pencolor("white")
  dudu.hideturtle()
  dudu.write(f"نعم صحيح {result} فاز شطور ",align="center",font=("arial",30,"normal"))
else:
  window.clear()
  window.bgcolor("black")
  dudu.penup()
  dudu.goto(0,0)
  dudu.pendown()
  dudu.pencolor("white")
  dudu.hideturtle()
  dudu.write(f"غير صحيح من فاز هوا {result} ",align="center",font=("arial",30,"normal"))



print(distance_dudu)
print(distance_bubu)
print(distance_ahmed)


window.exitonclick()  
