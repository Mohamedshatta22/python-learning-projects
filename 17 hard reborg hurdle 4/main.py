def move_n_jump():
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
while not at_goal():
    if front_is_clear() and wall_on_right():
       move()
    elif wall_on_right():
       turn_left()
    else: 
       move_n_jump()
