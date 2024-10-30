"""
File: StoneMasonKarel.py
Name: tsz.
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at street 1, avenue 1, facing east
    post-condition: Karel is at the rightest of the world, built all columns, facing east
    Algorithm
    1. set two definite loops( height of a column, distance of two columns)
    2. set a module( a.build a column, b.move to another column)
    3. set a conditional statement( if not front_is_clear) to stop
    * discussed the "put_beeper" part w/ Kang.
    """
    while front_is_clear():
        turn_left()
        # Karel will go up, put beepers and go down
        build_column()
        # Karel is facing south
        for i in range(4):
            move()
    if not front_is_clear():
        turn_left()
        build_column()


def build_column():
    for i in range(5):
        if on_beeper():
            if front_is_clear():
                move()
        if not on_beeper():
            put_beeper()
    turn_around()
    for i in range(4):
        move()
    turn_left()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
