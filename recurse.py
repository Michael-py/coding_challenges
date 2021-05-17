
def bin_search(arr, target):
	low = 0
	high = len(arr) - 1

	return bin_search_helper(arr, target, low, high)


def bin_search_helper(arr, target, low, high):

	if low > high:
		return "Not Found"


	mid = (low + high)//2

	if target < arr[mid]:
		return bin_search_helper(arr, target, low, mid-1)

	elif target == arr[mid]:
		return mid

	else:
		return bin_search_helper(arr, target, mid + 1, high)


def main():

	arr = [3,5,6,8,9,12,34,36]

	print(bin_search(arr, 37))



import time

start = time.perf_counter()
main()

print(time.perf_counter() - start)