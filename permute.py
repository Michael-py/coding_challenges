# function to compute the permutations of a list
# using the backtracking algorithm

def permute(n, nums):

	if n == 1:
		return nums

	else:
		answer = [x + y for x in permute(1, nums) for y in permute(n - 1, nums)]

		return answer

print(permute(4, list('michael')))


# 
# lst = list('a')
# lst2 = list('ab')
# lst3 = list('abc')
# lst4 = list('abcd')

# n = len(lst)
# m = len(lst2)
# o = len(lst3)
# p = len(lst4)

# a = len(permute(n, lst))
# b = len(permute(m, lst2))
# c = len(permute(o, lst3))
# d = len(permute(p, lst4))

# l1 = ((b - a)/a) *100

# l2 = ((c - b)/b) * 100

# l3 = ((d - c)/c) * 100

# print(l2 - l1)
# print(l3 - l2)
