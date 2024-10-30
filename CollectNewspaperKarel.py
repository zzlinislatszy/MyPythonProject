"""
File: CollectNewspaperKarel.py
Name: tsz.
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at street 4, avenue 3, facing east, without beeper
    post-condition: Karel is at street 4, avenue 3, facing east, with beeper
    """
    go_out()
    go_in()


def go_out():
    """
    pre-condition: Karel is at street 4, avenue 3, facing east
    post-condition: Karel is at street 3, avenue 6, facing east, pick beeper
    """
    for i in range(2):
        move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def go_in():
    """
    pre-condition: Karel is at street 3, avenue 6, facing east, pick beeper
    post-condition: Karel is at street 4, avenue 3, facing east, without beeper
    """
    # Karel is facing east
    for i in range(2):
        turn_left()
    move()
    turn_right()
    move()
    turn_left()
    for i in range(2):
        move()
    # Karel is facing west
    for i in range(2):
        turn_left()
    put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
