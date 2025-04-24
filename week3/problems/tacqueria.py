"""
One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, 
which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:

{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
In a file called taqueria.py, implement a program that enables a user to place an order,
prompting them for items, one per line, until the user inputs control-d (which is a common way
of ending one’s input to a program). After each inputted item, display the total cost of all items
inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the
user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on
the menu will be titlecased.

"""







import sys


# define the dict
menu = {
    
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

price = 0

def main():
        
    # while loop
        # get_input()
        # title_case()
        # menu_bill()
        # total()
        
    while True:
        user_input = get_input()
        item = title_case(user_input)
        food = menu_bill(item)
        if food is not None:
            total(food)

    
    
    
def get_input():
    # try to get input from user and then return if all is well
    # except EOFerror: then print a new line and quit the program
    try:
        entry = input("Item: ")
        return entry
    except EOFError:
        print()
        sys.exit()


def title_case(i):
    # title_case the input
    # return the title cased input
    titled = i.title()
    return titled
    
    
def menu_bill(item):
    # try to access the menu from input
        # if k in d, then add the price and return amount
    # except KeyError: then just repeat the while loop again and prompt again (break or continue)
    
    if item in menu:
        return menu[item]
    else:
        return None
    

def total(f):
    global price
    price += f
    print(f"${price:.2f}")
    
    
main()