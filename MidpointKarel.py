"""
File: MidpointKarel.py
Name: zzz.
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at street 1, avenue1
    post-condition: Karel is at the mid-point of street 1, put a beeper
    Algorithm
    1. set two reference points: put one beeper at(1,1), the other at the terminal
    2. in between: move back n forth between two beepers.
    pick one then move, until Karel stand between two beeper.
    DONE!
    """
    first_ref()
    # set two reference points
    while not on_beeper():
        go_back_n_forth()
    # repeat checking Karel's spot
    # below: Karel is between two beepers, then pick all beepers, go back to mid-point
    pick_beeper()
    turn_around()
    move()
    pick_beeper()
    put_beeper()


def first_ref():
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    move()


def go_back_n_forth():
    while not on_beeper():
        move()
    pick_beeper()
    turn_around()
    move()
    put_beeper()
    move()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
