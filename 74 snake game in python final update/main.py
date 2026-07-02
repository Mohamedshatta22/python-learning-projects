from snake import Snake 
import pygame
from food import Food
from score import Score
from turtle import Turtle,Screen
import time
pygame.mixer.init()
import sys
import os

current_dir = os.path.dirname(sys.argv[0])

eat_sound = pygame.mixer.Sound(os.path.join(current_dir, "eat.mp3"))
game_over = pygame.mixer.Sound(os.path.join(current_dir, "game over.mp3"))
score = 0
window = Screen()
window.bgcolor("black")
window.setup(1000,1000)
window.tracer(0)
snake = Snake()
food1 = Food()
score1 = Score()
window.listen()
game_on = True
while game_on:
    time.sleep(0.05)
    food1.moving_food()
    window.update()
    snake.snake_movement()
    window.onkey(snake.up,"w")
    window.onkey(snake.down,"s")
    window.onkey(snake.right,"d")
    window.onkey(snake.left,"a")
    if snake.head.distance(food1)<20:
        eat_sound.play()
        score1.increase_score()
        food1.removing_food()
        snake.get_taller()
    if snake.head.xcor() > 490 or snake.head.xcor() < -490 or snake.head.ycor() > 490 or snake.head.ycor() < -490:
           game_over.play()
           time.sleep(3)
           window.clear()
           score1.game_over()
           game_on = False
    for x in range(len(snake.turtles)-1):
     if snake.head.distance(snake.turtles[x].pos())<10:
         game_over.play()
         time.sleep(3)
         window.clear()
         score1.body_game_over()
         game_on = False
window.exitonclick()
