from prac_06.guitar import Guitar

print("My guitars!")
guitars = []

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:,.2f} added.")
    name = input("Name: ")

print("These are my guitars:")
longest_name_length = 0
longest_cost_length = 0
longest_guitar_number_length = len(str(len(guitars)))
for guitar in guitars:
    if len(guitar.name) > longest_name_length:
        longest_name_length = len(guitar.name)
    if len(",.2f".format(str(guitar.cost))) > longest_cost_length:
        longest_cost_length = len(",.2f".format(str(guitar.cost)))

counter = 1
for guitar in guitars:
    print(f"Guitar {counter:{longest_guitar_number_length}}: {guitar.name:>{longest_name_length}} "
          f"({guitar.year:>4}), worth $ {guitar.cost:>{longest_cost_length},.2f} ", end="")
    if guitar.is_vintage():
        print("(vintage)")
    else:
        print()
