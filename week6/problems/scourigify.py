import csv
import sys


if len(sys.argv) != 3:
    sys.exit("Must be exactly two filenames")

before = sys.argv[1]
after = sys.argv[2]

if not before.endswith(".csv") or not after.endswith(".csv"):
    sys.exit("Must be csv files")

try:

    with open(before) as file:
        reader = csv.DictReader(file)
        students = []

        for row in reader:
            last, first = row["name"].split(",")
            last = last.strip()
            first = first.strip()
            house = row["house"]
            students.append({"first": first, "last": last, "house": house})

    with open(after, "w") as file:
        
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for student in students:
            writer.writerow(student)

except(FileNotFoundError):
    sys.exit("Unable to read file")

