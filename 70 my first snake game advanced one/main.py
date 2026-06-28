from snake import Snake 
from turtle import Turtle,Screen
import time
window = Screen()
window.bgcolor("black")
window.setup(1000,1000)
snake = Snake()
window.tracer(0)
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
 
window.exitonclick()