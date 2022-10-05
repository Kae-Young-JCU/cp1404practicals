def main():
    menu = ("\n"
            "Please select an option:\n"
            "\n"
            "(G)et a valid score\n"
            "(P)rint result\n"
            "(S)how stars\n"
            "(Q)uit"
            "\n")
    selection = ""
    score_got = False
    while selection != "Q":
        print(menu)
        selection = input()
        match selection:
            case "G":
                score = get_score()
                score_got = True
                input("Press Enter to continue...")
            case "P":
                if not score_got:
                    print("No score. First select G to input a score.")
                else:
                    print(print_result(score))
                input("Press Enter to continue...")
            case "S":
                if not score_got:
                    print("No score. First select G to input a score.")
                else:
                    print_stars(score)
                input("Press Enter to continue...")
            case "Q":
                print("Goodbye")
            case _:
                print("Invalid selection")
                input("Press Enter to continue...")


def get_score():
    score = int(input("Enter score: "))
    while not 0 <= score <= 100:
        print("Invalid score. Must be between 0 and 100.")
        input("Enter score: ")
    return score


def print_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


def print_stars(score):
    for i in range(0, score, 1):
        print("*", end="")
    print()


main()
