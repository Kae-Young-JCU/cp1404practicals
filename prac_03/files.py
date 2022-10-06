# TASK 1

name_file = open('name.txt', 'w')

name = input("Enter name: ")
print(name, file=name_file)

name_file.close()

input("End of task 1. Press enter to continue to task 2...")

# TASK 2

name_file = open('name.txt', 'r')

name = name_file.readline()
print(f"Your name is: {name}")

name_file.close()

input("End of task 2. Press enter to continue to task 3...")

# TASK 3

numbers_file = open('numbers.txt', 'r')

number_line_1 = int(numbers_file.readline())
number_line_2 = int(numbers_file.readline())
number_sum = number_line_1 + number_line_2
print(number_sum)

numbers_file.close()

input("End of task 3. Press enter to continue to task 4...")

# TASK 4

number_sum = 0
with open('numbers.txt') as f:
    for line in f:
        number_sum += int(line.strip())
print(number_sum)
