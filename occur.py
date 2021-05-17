counts = 0

def occur(s, t, count=0):

	global counts

	if len(s) == 1 and s[0] == t:
		count += 1

	for i in range(len(s)):

		if s[i] == t:
			count+=1

		else:
			counts += 1
			occur(s[i+1:], t, count)

	return count


print(occur("propylleucineglycogen", "i"))
print(counts)