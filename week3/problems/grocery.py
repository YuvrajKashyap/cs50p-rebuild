""" 
Grocery List
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one’s input to a program). Then output
the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number
of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

"""




list = {}   


def main ():
    while True:
        try:
            user_input = get_input()
            add_list(user_input)
        except EOFError:
            for item in list:
                print(f"{list[item]} {item}")
            break

        
    
    
    
def get_input():
    item = input().strip().lower()
    return item
    
def add_list(key):
    global list
    if key not in list:
        list[key] = 1
    else:
        n = list[key]
        list.update({key: n+1})


main()
