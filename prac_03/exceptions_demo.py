"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Q1. When will a ValueError occur?
# A1. Line 10 when a non integer entry is made.
# Q2. When will a ZeroDivisionError occur?
# A2. Line 12 when the denominator is 0 and the division is executed
# Q3. Could you change the code to avoid the possibility of a ZeroDivisionError
# A3.
