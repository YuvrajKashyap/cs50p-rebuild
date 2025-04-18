#this asks use for name and prints hello (their name)
name = input("What's your name? ")
print(f"hello {name}")


name = input("enter your name with white spaces and random caps: ")
print(f"hello {name}") #regular
print(f"hello {name.strip()}") #strips white spaces
print(f"hello {name.title().strip()}")