import sys

if len(sys.argv) != 2:
    sys.exit("Must be exactly one filename")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Must be a python file")

try:
    with open(filename) as file:
        count = 0
        for line in file:
            stripped = line.strip()
            if stripped != "" and not stripped.startswith('#'):
                count += 1

    print(count)
except:
    sys.exit("Unable to open file")
    