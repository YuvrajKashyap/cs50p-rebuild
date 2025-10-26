with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
        print(f"{house} houses {name}\n")

        #remembering everything and revisiting
