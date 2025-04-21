
""" takes coins until 50 cents is paid off - im getting lazy w these comments"""



def main():
    # print amount due: 50
    # ask user to insert coin
    # subtract input from 50
    # print remaining due
    # once its 0 or less, exit loop and then display distance from 0
    
    due = 50
    print("Amount Due: " + str(due))
    
    while due > 0:
        subtract = int(input("Insert Coin: "))
        if subtract != 25 and subtract != 10 and subtract != 5:
            print("You can only insert 25, 10, or 5 cents at a time. ")
            continue
        else:
            due -= subtract
            if due <= 0:
                break
            else:
                print("Amount Due: "+ str(due))
            
    print("Change Owed: " + str(abs(due)))
    
    
main()