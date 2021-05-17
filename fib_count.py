count = 0

def main():

	index = eval(input("Enter an index for a fibonacci number: "))

	print("The fibonacci number at index, ", index, "is", fib(index))

	print(count)

def fib(index):
	global count
	
	if index == 0:
		return 0

	elif index == 1:
		return 1

	else:
		count+=1
		return fib(index-1) + fib(index-2)

main()