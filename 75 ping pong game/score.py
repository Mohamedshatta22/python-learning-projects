from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.goto(0,350)
    def write_score(self):
        self.clear()
        self.write(f"score: {self.score1}                             score: {self.score2}",align = "center",font =("arial",20,"normal"))
        
