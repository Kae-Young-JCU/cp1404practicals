MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def convert_c_to_f():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32


def convert_f_to_c():
    global fahrenheit, celsius
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)


def main():
    while choice != "Q":
        if choice == "C":
            convert_c_to_f()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            convert_f_to_c()
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


main()
