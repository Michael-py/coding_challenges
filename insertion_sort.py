
"""
# The insertion sort algorithm

HOW IT WORKS

1. We take the unsorted list and divide it into 2 sub-lists
	(sorted and unsorted)
2. the first list will have the length of 1
3. we take the very first element in the unsorted seq and 
	move to the sorted sublist
4. once moved, we compare the item with the item in the sorted
	sublist already. if the item we're trying to sort is smaller
	than the item to its immediate left, then we swap their 
	positions
"""

def insertion_sort(sequence):

	indexing_length = range(1, len(sequence))

	for i in indexing_length:
		value_to_sort = sequence[i]

		while sequence[i-1] > value_to_sort and i > 0:
			sequence[i], sequence[i-1] = sequence[i-1], sequence[i]

			i = i - 1
	return sequence
