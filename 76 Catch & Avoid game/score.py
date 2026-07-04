from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.goto(0,450)
    def write_score(self):
        self.clear()
        self.write(f"score: {self.current_score}",align = "center",font =("arial",20,"normal"))