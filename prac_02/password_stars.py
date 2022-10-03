def main():
    max_length, min_length, password, password_length = get_password()
    if min_length < password_length < max_length:
        print_stars(password)
    else:
        print(f"Password must be between {min_length} and {max_length} characters long.")


def print_stars(password):
    for i in range(0, len(password), 1):
        print("*", end="")
    print()


def get_password():
    password = input("Password: ")
    max_length = 15
    min_length = 5
    password_length = len(password)
    return max_length, min_length, password, password_length


main()
