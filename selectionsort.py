
def main():
	arr = [1,2,4,5,3,8,9,6,12,24,1,3,4,1,2,3]
	sort(arr)
	print(arr)

def sort(arr):
	selection_sort(arr, 0, len(arr)-1)

def selection_sort(arr, low, high):

	if low < high:

		index_of_min = low
		min_ = arr[low]

		for i in range(low + 1, high + 1):

			if arr[i] < min_:

				min_ = arr[i]

				index_of_min = i


		arr[index_of_min] = arr[low]
		arr[low] = min_

		selection_sort(arr, low + 1, high)


main()