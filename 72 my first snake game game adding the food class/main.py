from snake import Snake 
from food import Food
from turtle import Turtle,Screen
import time
window = Screen()
window.bgcolor("black")
window.setup(1000,1000)
window.tracer(0)
snake = Snake()
food1 = Food()
game_on = True
while game_on:
    time.sleep(0.05)

    snake.snake_movement()
    window.update()
    window.listen()
    window.onkey(snake.up,"w")
    window.onkey(snake.down,"s")
    window.onkey(snake.right,"d")
    window.onkey(snake.left,"a")
    if snake.head.distance(food1)<15:
        food1.removing_food()
        

 
window.exitonclick()