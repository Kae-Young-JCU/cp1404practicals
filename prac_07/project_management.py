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
    load_project("projects.txt", projects)

    # Menu block
    print(MENU)
    selection = input(">>> ")
    while selection != "":
        match selection:
            case "L":
                # Load project option
                load_file = input("File name: ")
                if "." not in load_file:
                    load_file = f"{load_file}.txt"
                if ".txt" not in load_file:
                    print("Please only load .txt files")
                else:
                    load_project(load_file, projects)
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


def load_project(load_file, projects):
    projects.clear()
    with open(load_file, 'r') as f:
        f.readline()
        for line in f.readlines():
            parts = line.strip().split('\t')
            projects.append([parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])])



main()
