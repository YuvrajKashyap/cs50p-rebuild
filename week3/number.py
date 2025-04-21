def main():
    x = get_int()
    print(x)
def get_int():
    while True:
        try: 
            x = int(input("Enter x: "))
            break
        except ValueError:
            print("x is not an integer")

    print(f"x is {x}")

    return x

get_int()