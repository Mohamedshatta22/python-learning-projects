from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,possition):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(possition)
        self.shapesize(7,1)
    def up(self):
        self.goto(self.xcor(),self.ycor()+130)
    def down(self):
        self.goto(self.xcor(),self.ycor()-130)
    def moving_paddle(self):
        self.forward(500)