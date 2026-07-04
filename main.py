from turtle import Turtle,Screen
from objects import Objects
from paddle import Paddle
from score import Score
import time
good_shapes = ["square","circle","turtle","arrow"]
screen = Screen()
screen.setup(1000,1000)
screen.bgcolor("black")
screen.title("                                                                                                                                  welcome to my new game")
screen.listen()
screen.tracer(0)
paddle = Paddle((0,-450))
screen.onkey(paddle.left,"a")
screen.onkey(paddle.right,"d")
score = Score()
game_on = True
while game_on:
 new_object = Objects()
 while True:
  score.write_score()
  time.sleep(0.015)
  screen.update()
  if new_object.x.distance(paddle) < 70 and new_object.x.ycor() < -430:
   if new_object.x.shape()=="turtle" and new_object.x.fillcolor() == "white":
     
     game_on = False
     print("game over")
     break
     
   elif new_object.x.shape()=="triangle":
     score.current_score = 0
     new_object.x.goto(1500,1500)
     break
     
   elif new_object.x.shape() in good_shapes:
    score.current_score += 1
    new_object.x.goto(1500,1500)
    break
   
  new_object.moving_objects()
  if new_object.x.ycor()<-600:
   break

 




screen.exitonclick()
