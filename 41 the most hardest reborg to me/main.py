def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
   while wall_on_right() and front_is_clear(): 
     move()
   if wall_on_right() and not front_is_clear():
     turn_left()
   if right_is_clear() and front_is_clear():
     turn_right()
     move()
   if right_is_clear() and not front_is_clear():
     turn_right()
     move()
