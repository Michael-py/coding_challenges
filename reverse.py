def rev_int(n, res=""):
	x = str(n)
	y = len(x)

	if y == 1:
		res+=x
		return int(res)
	else:

		res+=x[-1]

		return rev(x[0:y-1], res)

	return int(res)


def rev_s(s, res=""):

	x = len(s)

	if x == 1:
		res += s
		return res

	else:

		res += s[-1]
		return rev_s(s[0:x-1], res)

	return res

print(rev_s("michael"))
