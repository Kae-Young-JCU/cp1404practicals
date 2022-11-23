from prac_06 import guitar
import csv

guitars = []
new_guitars = []

guitar_file = open("guitars.csv", 'r+', newline='')
reader = csv.reader(guitar_file)
writer = csv.writer(guitar_file)

for row in reader:
    guitars.append(guitar.Guitar(row[0], int(row[1]), float(row[2])))

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    new_guitar = guitar.Guitar(name, year, cost)
    new_guitars.append([new_guitar.name, new_guitar.year, new_guitar.cost])
    guitars.append(new_guitar)
    print(f"{name} ({year}) : ${cost:,.2f} added.")
    name = input("Name: ")

if new_guitars != []:
    guitar_file.write("\n")
    last_row = new_guitars[-1]
    del new_guitars[-1]
    writer.writerows(new_guitars)
    guitar_file.write(",".join([last_row[0], str(last_row[1]), str(last_row[2])]))


guitars.sort()
for guitar in guitars:
    print(guitar)
guitar_file.close()