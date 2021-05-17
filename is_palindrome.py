
def is_palindrome(item):
	if type(item) != str:
		print("expected string")
	
	item = item.replace(" ","").replace(",","").replace(".","").lower()
	print(item)
	
	if item == item[::-1]:
		print("is_palindrome")
	else:
		print("not_palindrome")


def is_palindrome_recurse(s):

	if len(s) <= 1:
		return True

	elif s[0] != s[len(s) - 1]:
		return False

	else:

		return is_palindrome_recurse(s[1 : len(s)-1])



