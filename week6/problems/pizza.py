import csv
import sys
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("Must be exactly one filename")

filename = sys.argv[1]

if not filename.endswith(".csv"):
    sys.exit("Must be CSV file.")



try:
    with open(filename) as file:
        reader = csv.reader(file)
        menu = list(reader)
        header = menu[0]
        table_data = menu[1:]
        output = tabulate(table_data, headers = header, tablefmt = "grid")
        print(output)

except FileNotFoundError:
    sys.exit("Unable to open file")

    #lock in after exam
    # tmrw you lock back in and get back on grind mode
    #good job on exam, now lock tf in, you're behind