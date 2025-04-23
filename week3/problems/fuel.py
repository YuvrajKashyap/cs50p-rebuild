"""
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. 
For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank 
is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction,
formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a 
percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1%
or less remains, output E instead to indicate that the tank is essentially empty. And 
if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt 
the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like
ValueError or ZeroDivisionError.

"""




def main():
    # get input from users (x and y)
    
    user_input = get_input()
    
    fuel = float(convert(user_input))
    
    
    # if fuel is less than or equal to 1% print E
    # elif fuel is greater than or equal to 99%, print F
    if fuel <= 0.01:
        print("E")
    elif fuel >= .99:
        print("F")
        
    # else print fuel to nearest integer
    else:
        print(f"{round(fuel * 100)}%")


    
def get_input():
    
    # check if x and y are integers - ValueError
    
    while True:
        check = input("Fraction: ")
        try: 
            x, y = check.split("/")
            x = int(x)
            y = int(y)
            if x > y or y==0:
                continue
            else:
                return check
        except ValueError:
            print("x and y have to be integers")


    
    
    
        
def convert(input):
    # convert function
        # separate the / and store first one into x and second to y
        # divide x / y and store into z
        
    x, y = input.split("/")
    x = int(x)
    y = int(y)
    return x/y



main()