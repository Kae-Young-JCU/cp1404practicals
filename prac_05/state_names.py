"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":
    # EAFP Approach
    try:
        print(state_code, "is", CODE_TO_NAME[state_code.upper()])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")

    """ LBYL Approach
    if state_code.upper() in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code.upper()])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
    """
for state in CODE_TO_NAME:
    print(f"{state:<3} is {CODE_TO_NAME[state]}")
