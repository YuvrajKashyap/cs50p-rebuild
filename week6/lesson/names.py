
"""
names = []

for _ in range(3):
    name = input("What's your name? ")
    names.append(name)

for name in sorted(names):
    print(f"hello, {name}")
"""

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

