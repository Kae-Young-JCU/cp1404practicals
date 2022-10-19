"""Expected time: 30 mins
   Actual time: 36 mins"""


def main():
    email = input("Enter your email address: ")
    accounts = {}
    while email != "":
        fullname = get_name(email)
        valid_option = False
        while not valid_option:
            option = input(f"Is {fullname} your actual name (Y/N): ")
            if option == "Y":
                accounts[email] = fullname
                valid_option = True
            elif option == "N":
                name = input("What is your name: ")
                accounts[email] = name
                valid_option = True
            else:
                print("Invalid option")
        email = input("Enter you're email address: ")
    print(accounts)


def get_name(email):
    username = email.split("@")[0]
    try:
        fullname = " ".join([username.split(".")[0].title(), username.split(".")[1].title()])
    except IndexError:
        fullname = username.title()
    return fullname


main()