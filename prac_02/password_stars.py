password = input("Password: ")
maxLength = 15
minLength = 5
passwordLength = len(password)
if minLength < passwordLength < maxLength:
    for i in range(0, len(password), 1):
        print("*", end="")
    print()
else:
    print(f"Password must be between {minLength} and {maxLength} characters long.")
