
class AutoMachine():

	USERS_LIST = {'user_1': '1111', 'user_2':'2222'}
	USERS_BALANCE = {'user_1':50000, 'user_2':90000}

	def insert_card(self):
		
		try:
			user = input("Input User Name > ").lower()
			passw = input("Input Pin > ").lower()

			if AutoMachine.USERS_LIST[user] != passw:
				print("You have inputted a wrong pin \n Try again")
				return self.insert_card()
			else:
				return self.actions(user)
		except KeyError:
			print("User does not exist!")
			return self.create_acct(user, passw)

	
	def create_acct(self, user, passw):

		print("Do you want to create a new account? (y/n)")
		ans = input("> ").lower()

		if ans not in ['y', 'n']:
			print("wrong answer!")

		elif ans == 'y':
			AutoMachine.USERS_LIST[user] = passw
			AutoMachine.USERS_BALANCE[user] = 0

		else:
			print("Thank you for coming")
		return self.insert_card()


	def actions(self, user):

		print(f"Welcome to First Bank, {user}\n")
		print("\nWhat do you want to do?\n\n")

		print("\t1.Check Balance")
		print("\t2.Make Withdrawal")
		print("\t3.Make Deposit")
		print("\t4.Contact Customer Care")
		print("\t5.Exit\n\n")

		choice = int(input("Enter your choice > "))

		if choice not in range(1,6):
			print("\n\nYou have made an invalid choice\n\n")
			return self.actions(user)

		if choice == 1:
			print(f"Your balance is: #{AutoMachine.USERS_BALANCE[user]:#,.2f}")
			print("do you want to continue?")
			ans = input("(y/n) >").lower()
			if ans not in ["y", "n"]:
				print("invalid selection")
				ans = input("(y/n) >").lower()

				if ans == "y":
					return self.actions(user)

			elif ans == "y":
				return self.actions(user)

			else:
				print("\n\nThank you for banking with us :)\n\n")

		elif choice == 2:
			return self.withdraw(user)

		elif choice == 3:
			return self.deposit(user)

		elif choice == 4:
			return self.customer_care(user)

		else:
			print("\n\nThank you for banking with us :)\n\n")

	def withdraw(self, user):


		print("How much do you want to withdraw?\n\n")

		try:
			amount = int(input("Enter amount here > "))


			if amount%500 != 0:
				print("\nSorry! You can only withdraw in multiples of #500\n")
				return self.withdraw(user)

			elif amount == 0:
				print("Invalid deposit amount")
				return self.withdraw(user)

			elif amount > 50000:
				print("\nSorry! You have exceeded the withdrawal limit. \nEnter an amount lower than #50,000\n")
				return self.withdraw(user)

			elif amount > AutoMachine.USERS_BALANCE[user] and AutoMachine.USERS_BALANCE[user] == 0 :
				print("\nInsufficent Funds\n")
				return self.actions(user)

			else:
				print("Transaction Successful.\n")
				print("Please take your cash\n")
				AutoMachine.USERS_BALANCE[user] -= amount
				print(f"Your current balance is {AutoMachine.USERS_BALANCE[user]:#,.2f}")

			return self.actions(user)
		except ValueError:
			print("Invalid deposit amount")
			return self.withdraw(user)

	def deposit(self, user):

		print("Enter amount to deposit\n\n")

		try:
			deposit_amount = int(input("Enter amount here >"))

			if deposit_amount > 100000:
				print("You cannot make deposits larger than #100,000")
				return self.deposit(user)

			elif deposit_amount == 0:
				print("Invalid deposit amount")
				return self.deposit(user)

			else:
				AutoMachine.USERS_BALANCE[user] += deposit_amount
				print(f"Your current balance is {AutoMachine.USERS_BALANCE[user]:#,.2f}")

			return self.actions(user)

		except ValueError:
			print("Invalid deposit amount")
			return self.deposit(user)

	def customer_care(self, user):

		print(f"Thank you for reaching out, {user}")
		print("Kindly drop your email address, we will be in touch.")

		input("Enter Email Here >")

		print("Have a nice day!")




if __name__ == '__main__':
	atm = AutoMachine()
	atm.insert_card()
	