
def main():

	n = detect(input("Enter a non-negative integer:> "))

	print(f"The factorial of {n} is {loop_fact(n)}")

	print(count_nums(factorial(n)))


def loop_fact(n):

	# n * (n-1)!

	if n == 0:
		return 1

	else:
		fact = 1

		for i in range(1, n+1):

			fact *= i

		return fact


def factorial(n):

	if n == 0:
		return 1

	else:
		return n * factorial(n - 1)



main()


# def f(n):

# 	if n > 0:

# 		print(n % 10)

# 	else:

# 		f(n//10)


# def f(n):

# 	if n == 1:
# 		return 1

# 	else:
# 		return n + f(n-1)



