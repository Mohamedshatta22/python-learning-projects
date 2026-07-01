from turtle import Turtle
score = 0 
class Score(Turtle):
    def __init__(self):
     super().__init__()
     self.result = 0
     self.penup()
     self.goto(0,460)
     self.pendown()
     self.pencolor("white")
     self.hideturtle()
     self.write_score()
    def write_score(self):
     self.write(f"your current score is: {self.result} ",align="center",font=("arial",20,"normal"))
    def increase_score(self):
      self.result +=1
      self.clear()
      self.write_score()
    def game_over(self):
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(0,0)
        self.hideturtle()
        self.write(f"لقد خسرت قد ارتطم ا لثعبان بالحائط وفرت السلحفاة الاخيرة",align="center",font=("arial",30,"normal"))
    def body_game_over(self):
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(0,0)
        self.hideturtle()
        self.write(f"لقد خسرت قد ارتطم الثعبان بنفسه",align="center",font=("arial",30,"normal"))


   