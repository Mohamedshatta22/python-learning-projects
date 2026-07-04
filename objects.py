from turtle import Turtle
import random

class Objects():
    def __init__(self):
        self.shapes = ("square","triangle","circle","turtle","arrow")
        self.colors = ("red","white","green","yellow","blue","olive")
        self.size = (1,2,3,4)
        self.x = self.creating_objects()
        
    def creating_objects(self):
        obje = Turtle()
        obje.shape(random.choice(self.shapes))
        obje.color(random.choice(self.colors))
        obje.shapesize(random.choice(self.size))
        obje.penup()
        obje.goto(random.randint(-460,460),600)
        obje.setheading(270)
        return obje
    def moving_objects(self):
         self.x.forward(10)




        



