"""
File: CheckerboardKarel.py
Name: zzz.
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at street 1, avenue 1, stand on a white board post-condition: Karel can be anywhere,
    fill the checkerboard by putting beeper
    Algorithm
    1. fill one line: put the first beeper at (1,1), as the reference point,
    if Karel put one, she( or it?) would move twice.
    2. set two turning points:
        a. facing north, not on beeper or on beeper
        b. facing south, not on beeper or on beeper
    3. set the stop point
    """
    # finish the first avenue
    turn_left()
    put_beeper()
    fill()
    # set two turning pints
    # a. facing north, not on beeper or on beeper
    # b. facing south, not on beeper or on beeper
    while not front_is_clear():
        if facing_north():
            if not on_beeper():
                turn_right()
                move()
                put_beeper()
                turn_right()
                fill()
            else:
                turn_right()
                if front_is_clear():
                    move()
                    turn_right()
                    fill()
        if facing_south():
            if not on_beeper():
                turn_left()
                if front_is_clear():  # discussed the 'stop' condition w/ Kang
                    move()
                    put_beeper()
                    turn_left()
                    fill()
            else:
                turn_left()
                move()
                turn_left()
                fill()


def fill():
    while front_is_clear():
        if on_beeper():
            move()
        else:
            move()
            put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
