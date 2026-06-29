from turtle import Turtle
import random
position_list = []
for x in range(-400,400):
   position_list.append(x)

class Food(Turtle):
    def __init__(self):
     super().__init__()
     self.position = (random.choice(position_list),random.choice(position_list))
     self.shape("square")
     self.color("red")
     self.penup()
     self.shapesize(0.5,0.5)
     self.appearing_food()
    def appearing_food(self):
      self.goto(self.position)
    def removing_food(self):
       self.goto(random.choice(position_list),random.choice(position_list))
       print("yummy")
       
    
    


