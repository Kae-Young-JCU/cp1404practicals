from prac_06 import guitar
import csv

guitars = []

guitar_file = open("guitars.csv")
reader = csv.reader(guitar_file)
for row in reader:
    guitars.append(guitar.Guitar(row[0], int(row[1]), float(row[2])))
guitar_file.close()

name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(guitar.Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:,.2f} added.")
    name = input("Name: ")

guitars.sort()

for guitar in guitars:
    print(guitar)