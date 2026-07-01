from turtle import Turtle
import random
import time
position_list = []
for x in range(-400,400):
   position_list.append(x)

class Food(Turtle):
    def __init__(self):
     super().__init__()
     self.position = (random.choice(position_list),random.choice(position_list))
     self.shape("turtle")
     self.color("green")
     self.penup()
     self.shapesize(1,1)
     self.appearing_food()
    def appearing_food(self):
      self.goto(self.position)
    def removing_food(self):
       self.goto(random.choice(position_list),random.choice(position_list))
       
       print("yummy")
    def moving_food(self):
        self.forward(10)
        if self.xcor() > 470 or self.xcor() < -470 or self.ycor() > 470 or self.ycor() < -470:
            self.right(random.randint(90, 180))


   
       
    
    


