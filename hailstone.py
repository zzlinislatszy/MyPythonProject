"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program computes Hailstone sequences.
    -
    Algorithm
    1. use while loop
    2. discriminate number is an odd or even
    3. do the calculate
    """
    print("This program computes Hailstone sequences.")
    num = int(input("Enter a number: "))
    sum = 0
    while num != 1:
        if num % 2 != 0:
            # discriminate number is an odd or even
            num = int(3*num+1)
            sum += 1
            print(str(int((num-1)/3)) + " is odd, so I make 3n+1: " + str(num))
        else:
            num = int(num/2)
            sum += 1
            print(str(int(num*2)) + " is even, so I take half: " + str(num))
    print("It took "+str(sum)+" steps to reach 1.")



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
