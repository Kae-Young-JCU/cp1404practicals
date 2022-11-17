from prac_06 import guitar
import csv

guitars = []

guitar_file = open("guitars.csv")
reader = csv.reader(guitar_file)
for row in reader:
    parts = row.split(",")
    guitars.append(parts[0], int(parts[1]), float(parts[2]))
guitar_file.close()
