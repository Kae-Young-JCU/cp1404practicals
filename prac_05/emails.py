"""Expected time: 30 mins
   Actual time: """


def main():
    email = input("Enter you're email address: ")
    while email != "":
        get_name(email)
        email = input("Enter you're email address: ")


def get_name(email):
    username = email.split("@")[0]
    fullname = " ".join(username.split(".")[0].title(), username.split("."[1].title()))
    print(fullname)


main()
