def m(i, ss=[]):

	# output: 1, 1/2, 1/3, 1/4, 1/5...

	if i > 1:
		ss.append(f'1/{i}')
		return m(i-1, ss)

	else:
		ss.append('1')

	return ss[::-1]


def ss(i, res=[]):

	# output: 1/3, 2/5, 3/7, 4/9...

	if i > 0:
		res.append(f'{i}/{((2*i)+1)}')
		return ss(i-1, res)

	return res[::-1]


def mss(i, res=[]):

	# output: 1/2, 2/3, 3/4, 4/5...

	if i > 0:
		res.append(f'{i}/{i+1}')
		return mss(i-1, res)

	return res[::-1]

print(mss(10))
