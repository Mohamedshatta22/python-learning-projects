from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,possition):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(possition)
        self.shapesize(1,8)
    def right(self):
        self.goto(self.xcor()+90,self.ycor())
    def left(self):
        self.goto(self.xcor()-90,self.ycor())
