"""
names = ["Ada", "Alan", "Bill", "John"]
while len(names) > 0:
    print(", ".join(names))
    name_to_remove = input("Who do you want to remove? ")
    try:
        names.remove(name_to_remove)
    except ValueError:
        print(f"{name_to_remove} is not on the list")
print("The list is now empty")
"""


def get_numbers():
    text = input("Enter numbers seperated by commas: ")
    numbers = text.split(",")
    for number in numbers:
        try:
            float(number)
        except ValueError:
            print("Please enter only numbers")
            get_numbers()
    return numbers


print(get_numbers())