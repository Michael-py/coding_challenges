

def special_or(x, y):

	if x and y:
		return True

	elif x and not y:
		return True

	elif not x and y:
		return True

	elif not x and not y:
		return False
	else:
		None

print(special_or(False, False))