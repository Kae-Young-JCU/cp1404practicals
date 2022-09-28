userName = input("Please enter you're name: ")
MENU = """Please select an option
H - Personal greeting
G - Personal farewell
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != 'Q':
    if choice == 'H':
        print("Hello " + userName)
    elif choice == 'G':
        print("Goodbye " + userName)
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Program terminating")