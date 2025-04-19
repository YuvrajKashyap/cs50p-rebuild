
"""
for i in range(3):
    print("meow")
    
    
    
print("meow \n" * 3)
    
    
"""
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("How many times should I meow? "))
        if n > 0:
            break 
    return n


def meow(m):
    for _ in range(m):
        print("meow \n")
        

main()
    
