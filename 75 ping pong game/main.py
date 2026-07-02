from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
import pygame
pygame.mixer.init()
import sys
import os
current_dir = os.path.dirname(sys.argv[0])

tak_sound = pygame.mixer.Sound(os.path.join(current_dir, "hit.mp3"))
out_sound = pygame.mixer.Sound(os.path.join(current_dir, "Get out sound.mp3"))
screen = Screen()
screen.bgcolor("black")
screen.setup(800,800)
right_paddle = Paddle((370,0))
left_paddle = Paddle((-370,0))
screen.tracer(0)
ball = Ball()
score =Score()
screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")
game_on = True
time1 = 0.0555
while game_on:
    
    score.write_score()
    screen.update()
    time.sleep(time1)
    ball.moving_the_ball()
    if ball.ycor()>=360 or ball.ycor()<=-360:
        tak_sound.play()
        ball.ymove  *= -1
        
    if ball.xcor() > 340 and ball.distance(right_paddle) < 70:
     tak_sound.play()
     ball.xmove *= -1.2
     ball.ymove *= 1.2
     
    elif ball.xcor() < -340 and ball.distance(left_paddle) < 70:
     tak_sound.play()
     ball.xmove *= -1.2
     ball.ymove *= 1.2
     
    elif  ball.xcor()>=500:
        out_sound.play()
        ball.goto(0,0)
        ball.xmove  *= -1
        score.score1 +=1
        ball.ymove =17
        ball.xmove =10

    elif  ball.xcor()<=-500:
        out_sound.play()
        ball.goto(0,0)
        ball.xmove  *= -1
        score.score2 +=1
        ball.ymove =17
        ball.xmove =10
         
screen.exitonclick()
