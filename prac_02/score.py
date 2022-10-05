"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

"""
BAD CODE

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
        print("Excellent")
if score < 50:
    print("Bad")
"""

import random

def grade_score(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


def main():
    score = float(input("Enter score: "))
    print(grade_score(score))
    random_score = random.randint(0, 100)
    print(f"For the score {random_score} the result is {grade_score(random_score)}")


main()
