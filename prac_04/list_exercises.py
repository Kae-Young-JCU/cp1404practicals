AMOUNT_OF_NUMBERS = 5


def main():
    exercise = input("Choose an exercise\n"
                      "\n"
                      "(N)umbers exercise\n"
                      "(S)ecurity checker exercise\n")
    if exercise == "N":
        numbers_exercise()
    elif exercise == "S":
        security_exercise()


def security_exercise():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter username: ")
    if username in usernames:
        print("Access Granted")
    else:
        print("Access denied")


def numbers_exercise():
    print_number_info(get_numbers())


def get_numbers():
    numbers = []
    for i in range(0, AMOUNT_OF_NUMBERS, 1):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


def print_number_info(numbers):
    print(f"The first number is {numbers[0]}\n"
          f"The last number is {numbers[AMOUNT_OF_NUMBERS - 1]}\n"
          f"The smallest number is {min(numbers)}\n"
          f"The largest number is {max(numbers)}\n"
          f"The average of the numbers is {sum(numbers)/AMOUNT_OF_NUMBERS}")


main()
