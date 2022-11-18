import project
import datetime

MENU = "Select an option:\n" \
       "(L)oad\n" \
       "(S)ave\n" \
       "(D)isplay\n" \
       "(F)ilter\n" \
       "(A)dd\n" \
       "(U)pdate"


def main():
    """The main code block"""
    # Load default projects file
    projects = []
    load_projects("projects.txt", projects)

    # Menu block
    print(MENU)
    selection = input(">>> ")
    while selection != "":
        match selection.upper():
            case "L":
                # Load project option
                load_file = input("File name: ")
                if "." not in load_file:
                    load_file = f"{load_file}.txt"
                if ".txt" not in load_file:
                    print("Please only load .txt files")
                else:
                    load_projects(load_file, projects)
            case "S":
                save_file = input("File name: ")
                if "." not in save_file:
                    load_file = f"{save_file}.txt"
                if ".txt" not in save_file:
                    print("Please only load .txt files")
                else:
                    load_projects(load_file, projects)
            case "D":
                display_projects(projects)
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


def str_to_date(str_date):
    parts = str_date.split("/")
    return datetime.datetime(int(parts[2]), int(parts[1]), int(parts[0]))


def load_projects(load_file, projects):
    projects.clear()
    with open(load_file, 'r') as f:
        f.readline()
        for line in f.readlines():
            parts = line.strip().split('\t')
            projects.append(project.Project(parts[0], str_to_date(parts[1]), int(parts[2]), float(parts[3]), int(parts[4])))


def save_projects(save_file, projects):
    with open(save_file, 'w+') as f:
        f.write('\n')
        f.writelines(projects)


def display_projects(projects):
    incomplete_projects = []
    complete_projects = []
    for project_ in projects:
        if project_.completion_percentage == 100:
            complete_projects.append(project_)
        else:
            incomplete_projects.append(project_)
    incomplete_projects.sort(reverse=True)
    complete_projects.sort(reverse=True)
    plural = ''
    if len(incomplete_projects) > 1:
        plural = 's'
    print(f"You have {len(incomplete_projects)} incomplete project{plural}:")
    counter = 1
    for project_ in incomplete_projects:
        print(f"{counter}. {project_:d}")
        counter += 1
    plural = ''
    if len(complete_projects) > 1:
        plural = 's'
    print(f"You have {len(complete_projects)} complete project{plural}:")
    counter = 1
    for project_ in complete_projects:
        print(f"{counter}. {project_:d}")
        counter += 1


main()
