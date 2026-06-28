def move_n_jump():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
while not at_goal():
    if front_is_clear():
       move()
    else: 
       move_n_jump()
