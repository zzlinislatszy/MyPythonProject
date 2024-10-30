"""
File: quadratic_solver.py
Name: zzz.
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	solve a quadratic: ax*x+b*x+c=0
	set b*b-4ac as a discriminant, get 3 situations
	"""
	print("stanCode Quadratic Solver!")
	# from user-end
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	c = int(input("Enter c: "))
	if b*b-4*a*c < 0:
		# root must be positive
		print("No real roots")
	else:
		y = math.sqrt(b*b-(4*a*c))
		# two situations +y,-y
		x_pos = (-b+y)/2*a
		x_neg = (-b-y)/2*a
		if b*b-4*a*c > 0:
			print("Two roots:" + str(x_pos) + "," + str(x_neg))
		if b*b-4*a*c == 0:
			print("One roots:" + str(x_pos))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
