from prac_06 import guitar
import csv

guitars = []

guitar_file = open("guitars.csv")
reader = csv.reader(guitar_file)
for row in reader:
    guitars.append(guitar.Guitar(row[0], int(row[1]), float(row[2])))
guitar_file.close()
guitars.sort()
for guitar in guitars:
    print(guitar)