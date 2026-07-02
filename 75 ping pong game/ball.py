from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ymove =17
        self.xmove =10

    def moving_the_ball(self):
        
        self.goto(self.xcor()+self.xmove,self.ycor()+self.ymove)
        

