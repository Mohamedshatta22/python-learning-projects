from turtle import Turtle

class Snake():
    def __init__(self):
        self.turtles = []
        self.possitions = [(-40,0),(-20,0),(0,0),(20,0),(40,0),(60,0),(80,0)]
        self.snake_body()
    def snake_body(self):
      for x in range(len(self.possitions)):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(self.possitions[x])
        self.turtles.append(new_turtle)
    def snake_movement(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto((self.turtles[i+1]).pos())
        self.turtles[-1].forward(20)
    def up(self):
        self.turtles[-1].setheading(90)
    def down(self):
        self.turtles[-1].setheading(270)
    def left(self):
        self.turtles[-1].setheading(180)
    def right(self):
        self.turtles[-1].setheading(0)












        
