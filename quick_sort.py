
"""
# The quick sort algorithm

HOW IT WORKS

1. from a given sequence of items we pick a pivot item
	that we'll use to do comparisons - the last item

2. iterate over the remainder of the sequence and 
	compare each item to the pivot item

3. if the item is lower than the pivot, it is appended 
	to a Lower_than list

4. if the item is higher than the pivot, it is appended
	to a higher_than list

5. the 2 lists are then also passed to the algorithm till
	everything is sorted
"""

def quick_sort(sequence):

	if len(sequence) <= 1:
		return sequence

	else:
		# selection of pivot items
		pivot = sequence.pop()

		higher_than = []
		lower_than =[]

		for item in sequence:
			if item > pivot:
				higher_than.append(item)
			else:
				lower_than.append(item)

	return quick_sort(lower_than) + [pivot] + quick_sort(higher_than)
	