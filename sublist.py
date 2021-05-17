
# Function to create a sublist of a list

def cut(lst, start, stop):

	# get slice of the list from the start and stop indices

	lst_slice = lst[start:stop+1]

	# get the remaining list items from the right

	right_rem = lst[stop+1:]

	# get the remaining list items from the left

	left_rem = lst[0:start]


	# check if any of the left or right remainders
	# has a length of 0
	# and carry out appropriate actions

	if len(left_rem) == 0:
		nested_lst = [lst_slice] + right_rem

	elif len(right_rem) == 0:
		nested_lst = left_rem + [lst_slice]

	else:
		nested_lst = left_rem + [lst_slice] + right_rem

	return nested_lst


x = list(range(1,8))

print(x)
print(cut(x,2,4))