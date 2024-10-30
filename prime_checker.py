"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	This program help user check if the input is a prime number.
	-
	Algorithm
	1. A prime has only 2 factors
	2. check zone will be itself to 2 (ex:2-13)
	"""
	print("Welcome to the prime checker!")
	while True:
		n = int(input("n: "))
		division = n - 1
		if n == EXIT:
			print("Have a good one!")
			break
		if n % 2 != 0:
			# exclude evens
			if n == 3:
				# exclude 3
				print(str(n) + " is a prime number.")
			else:
				while division != 1:
					# check if n%(n to 2) == 0
					if n % division != 0:
						division -= 1
						# start from n-1
						if division == 2:
							print(str(n) + " is a prime number.")
					else:
						print(str(n) + " is not a prime number.")
						break
		else:
			print(str(n) + " is not a prime number.")

		# below down is unsolved for-loop solution
		# if n == EXIT:
		# 	print("Have a good one!")
		# 	break
		# for i in range(2, n):
		# 	if n % i == 0:
		# 		print(str(n)+" is not a prime number.")
		# 		break
		# if
		# 	# else:
		# 	# 	print(str(n) + " is not a prime number.")
		# 	# 	break


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
