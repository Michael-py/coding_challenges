def moveDisks(n, fromTower, toTower, viaTower):

	if n == 1:

		print(f"Move disk {n} from {fromTower} to {toTower}")

	else:

		moveDisks(n-1, fromTower, viaTower, toTower)

		print(f"Move disk {n} from {fromTower} to {toTower}")

		moveDisks(n-1, viaTower, toTower, fromTower)


def main():

	disks = eval(input("Enter the number of disks to move:> "))

	moveDisks(disks, 'A', 'B', 'C')


main()