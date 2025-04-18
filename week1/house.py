name = input("Enter your name: ")
"""
if name == "Harry":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
elif name == "Ron":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
else:
    print("who..?")
    
"""


match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who..?")