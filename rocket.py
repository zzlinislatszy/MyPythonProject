"""
File: rocket.py
Name: zzz.
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 2


def main():
    """
    Build different size of rockets!
    -
    Algorithm
    1. define functions "head, "belt", "upper", "lower"
    2. break apart every unit "/", "\", "+", "=", "|", "."
    3. modularize the units
    4. compose
    5. to the Mars ✧
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        for j in range(SIZE - i):
            # for space: size - for-loop times
            print(" ", end="")
        for j in range(i + 1):
            print("/", end="")
        for j in range(i + 1):
            print("\\", end="")
        print("")


def belt():
    # other ideas? mirror? backwards for-loop?
    for i in range(1):
        for j in range(1):
            print("+", end="")
        for j in range(SIZE * 2):
            print("=", end="")
        for j in range(1):
            print("+", end="")
        print("")


def upper():
    for i in range(SIZE):
        for j in range(1):
            print("|", end="")
        for j in range(SIZE - 1 - i):
            # SIZE=3, "."=2 1 0, for-loop 0 1 2
            print(".", end="")
        for j in range(i + 1):
            # SIZE=3, pack "/\", pack 1 2 3, for-loop 0 1 2
            for k in range(1):
                print("/", end="")
                for z in range(1):
                    print("\\", end="")
        for j in range(SIZE - 1 - i):
            # SIZE=3, "."=2 1 0, for-loop 0 1 2
            print(".", end="")
        for j in range(1):
            print("|", end="")
        print("")


def lower():
    for i in range(SIZE):
        for j in range(1):
            print("|", end="")
        for j in range(i):
            print(".", end="")
        for j in range(-i + SIZE):
            # SIZE=3, pack "\/", pack 3 2 1, for-loop 0 1 2
            for k in range(1):
                print("\\", end="")
                for z in range(1):
                    print("/", end="")
        for j in range(i):
            print(".", end="")
        for j in range(1):
            print("|", end="")
        print("")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
