def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move2():
    move()
    turn_left()
    move()
def move3():
    move()
    turn_right()
    move()
    turn_left()
for x in range(0,6):
   move2()
   turn_right()
   move3()
