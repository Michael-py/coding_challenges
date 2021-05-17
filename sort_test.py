
# function takes two lists as arguments

def sort_and_test(list1, list2):

	# check if the 2 lists are of the same length
	# return False, if not

	if len(list1) != len(list2):
		return False


	else:

		# sort the first list ans store in a variable lst

		lst = sorted(list1)

		# iterate over the first list

		for i in lst:

			# check if each number in lst occur in list2
			# return True if it occurs
			# Else return False

			if i in list2:
				return True

			else:
				return False


x = [10,9,8,7,6,5]
y = list(range(5,11))

print(sort_and_test(x, y))
