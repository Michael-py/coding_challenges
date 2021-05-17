import datetime
import random
import re

now = datetime.datetime.now()

database = {}


# prompt the user to enter a valid First name and Last name
# Both names must not include digital numbers

def welcome():
    try:
        Option_Selected = False
        print(">>> Hello, Welcome to Debby's World Bank <<<")
        print(now.strftime("%Y-%B-%d %H:%M:%S"))
        while not Option_Selected:
            select_option = int(input("""Do you want to;
        1. Open an account
        2. Already have an account? Then login with your details\n
        """))
            if select_option == 1:
                Option_Selected = True
                register()
            elif select_option == 2:
                Option_Selected = True
                login()
            else:
                print("Invalid entry, Try again!!!")
    except ValueError:
        print('Enter 1 or 2!!!')
        welcome()


def register():
    print('Please fill in your details correctly')

    first_name = input("Enter First Name:\n\t>")
    last_name = input("\nEnter Last Name:\n\t>")
    email = input("\nEnter Email Address\n\t")
    password = input("\nCreate Password (atleast 8 characters long)\n\t>")
    confirm_password = input("\nConfirm Password\n\t>")
    year_of_birth = int(input("Enter Your Birth Year\n\t>"))
    balance = "#" + str(500)

    is_valid = validate_input(first_name, last_name, email, password, confirm_password, year_of_birth)

    if is_valid:
        account_number = generate_account_number()

        database[account_number] = [first_name, last_name, email, password, year_of_birth, balance]

        print(f"\nYour Account Number Is: {account_number}\n")
        print(f"Your Account Details Are: {database[account_number]}\n")

    else:

        register()


def validate_input(fname, lname, mail, pword, cpword, ybirth):

    validity = False

    if not fname.isalpha() and not lname.isalpha():
        validity = False

    elif len(pword) < 8:
        print("Password must be 8 characters long.")
        validity = False

    elif re.search('[A-Z]', pword) is None:
        print("Password Must Contain Atleast 1 Uppercase Letter")
        validity = False

    elif re.search('[0-9]', pword) is None:
        print("Password Must Contain Atleast 1 Number")
        validity = False

    elif re.search('[!@#$%^&*<>]', pword) is None:
        print("Password Must Contain Atleast 1 Special Character ")
        validity = False

    elif pword != cpword:
        print("Passwords do not match!")
        validity = False

    elif not re.search(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)", mail):
        print("Email is valid!")
        validity = False


    elif int(datetime.datetime.strftime(now, "%Y")) - int(ybirth) < 18:
        print("To own an account, you must be at least 18years old")
        validity = False

    else:
        validity = True

    return validity


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


# def login():
#     print('hh')


# def exist():
#     print(' hgj')


welcome()
