MENU = "Select an option:\n" \
       "(L)oad\n" \
       "(S)ave\n" \
       "(D)isplay\n" \
       "(F)ilter\n" \
       "(A)dd\n" \
       "(U)pdate"


def main():
    # Load default projects file
    projects = []
    with open("projects.txt", 'r') as f:
        f.readline()
        for line in f.readlines():
            parts = line.strip().split('\t')
            projects.append([parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])])


    # Menu block
    print(MENU)
    selection = input(">>> ")
    while selection != "":
        match selection:
            case "L":
                break
            case "S":
                break
            case "D":
                break
            case "F":
                break
            case "A":
                break
            case "U":
                break
            case _:
                print("Invalid Selection")
        input(". . .")
        print(MENU)
        selection = input(">>> ")


main()