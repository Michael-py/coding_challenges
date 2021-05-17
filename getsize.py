import os


def main():
	path = 'c:\\desktop_files'

	try:
		print(dir_size(path), 'bytes')

	except:
		print("Path or file does not exist")

def dir_size(directory):

	size = 0

	if not os.path.isfile(directory):

		for d in os.listdir(directory):

			size += dir_size(directory + "\\" + d)

	else:
		size += os.path.getsize(directory)

	return size

main()