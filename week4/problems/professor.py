import random


def main():
    score = 0
    digits = get_level()
    for _ in range(10):
        x = generate_integer(digits)
        y = generate_integer(digits)
        for _ in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {x+y}")
        
                
    print(f"Score: {score}")
                    


def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            
            if level in levels:
                return level
            else:
                continue
        except ValueError:
            continue
        


def generate_integer(n):
    if n == 1:
        return random.randint(0, 9)
    elif n == 2:
        return random.randint(0,99)
    elif n == 3:
        return random.randint(0,999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()