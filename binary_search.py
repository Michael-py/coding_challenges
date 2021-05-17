
"""
# The binary search algorithm
## uses an already sorted sequence

HOW IT WORKS

1. from a given sequence of items we take a midpoint
	of the sequence. we need the starting and ending position too

2. then we compare the midpoint item with the search 
	item. if the search item is greater than the midpoint,
	then we check to the right of the midpoint

3. if the item is lower than the midpoint, then we check
	to the left of the midpoint

4. if we find the item in the sequence, we stop the algorithm
	and return the position of the item
"""


def binary_search(sequence, item):

	starting_index = 0
	end_index = len(sequence) - 1

	while starting_index <= end_index:

		midpoint = starting_index + (end_index - starting_index) // 2
		midpoint_value = sequence[midpoint]

		if midpoint_value == item:
			return midpoint

		elif item < midpoint_value:
			end_index = midpoint - 1

		else:
			starting_index = midpoint + 1


	return None