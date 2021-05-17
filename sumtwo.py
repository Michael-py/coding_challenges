
def sum2(nums, target):
	found = {}

	for i, num in enumerate(nums):
		n = target - num
		if num not in found:
			found[n] = i
		else:
			return [found[num], i]

lst = list(range(9))
print(sum2(lst, 9))
