import random
# ask user how man quick picks they wish to generate (x)
# generate x amount of lines consisting of 6 random numbers between 1 and 45 (stored as constants)
# Each line contains no repeated numbers
# Each line is displayed in ascending order
# Numbers align neatly
NUMBER_OF_QUICK_PICKS = int(input("How many quick picks? "))
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 5

for i in range(0, NUMBER_OF_QUICK_PICKS, 1):
    potential_numbers = list(range(MIN_NUMBER, MAX_NUMBER + 1))
    random.shuffle(potential_numbers)
    numbers = potential_numbers[:NUMBERS_PER_LINE]
    for j in range(0, NUMBERS_PER_LINE, 1):
        print(f"{str(numbers[j]):>2}", end=" ")
    print()



