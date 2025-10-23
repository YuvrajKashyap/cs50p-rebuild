
"""
names = []

for _ in range(3):
    name = input("What's your name? ")
    names.append(name)

for name in sorted(names):
    print(f"hello, {name}")


name = input("What's your name? ")


with open("names.txt", "a") as file:
    file.write(f"{name}\n")

    

    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())



    """


with open("names.csv") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())

