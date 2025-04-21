
# takes your message and removes all vowels in case you ever wanted to do that i guess...


def main():
    #get input
    #convert input in loop to replace vowels
    #print output
    
    message = get_input()
    
    tweet = convert(message)
    
    print(tweet)
    
    
def get_input():
    m = input("Input: ")
    return m

def convert(v):
    t = ""
    
    for i in v:
        if i in "AEIOUaeiou":
            continue
        t += i
        
    return t


main()