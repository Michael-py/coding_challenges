# counting from 1 to 100 without for_loop

def count(n):

	if n < 100:
		n += 1
		print(n)
		count(n)
	
	

count(0)