import emoji

def main():
    str = input("Input: ").strip()
    print(emoji.emojize(str))
    
main()