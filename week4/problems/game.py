import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                continue
            else:
                answer = random.randint(1, level)
                break
        except ValueError:
            print("Must be an integer!")
            continue
        
        

    while True:
        try:
            guess = int(input("Guess: "))
            
            if guess < 1:
                continue
            elif guess > level:
                print("Wayyyyyyy too large")
            elif guess > answer:
                print("Too large!")
            elif guess < answer:
                print("Too small!")
            else:
                print("Just right!")
                break
        except ValueError:
            print("Must be an integer!")
    
main()