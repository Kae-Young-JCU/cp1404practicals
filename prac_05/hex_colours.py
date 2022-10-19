COLOUR_TO_HEX = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#b0bf1a", "ALICE BLUE": "#f0f8ff",
                 "ALIZARIN CRIMSON": "#e32636", "AMARANTH": "#e52b50", "AMBER": "#ffbf00",
                 "AMETHYST": "#9966cc", "ANTIQUE WHITE": "#faebd7", "APRICOT": "#fbceb1",
                 "AQUA": "#00ffff"}
print(COLOUR_TO_HEX)

colour = input("Enter colour name: ")
while colour != "":
    try:
        print(f"The hex code of {colour} is {COLOUR_TO_HEX[colour.upper()]}")
    except KeyError:
        print("Invalid colour name")
    colour = input("Enter colour name: ")
