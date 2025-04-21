def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # has to start with 2 letters at least
    # 2-6 characters total
    # numbers have to come after all the letters, and first number cant be 0
    # no periods, no punctuation, no spaces
    
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            if s[i:].isdigit():
                break
            else:
                return False
    
    if s[0:2].isalpha() and 2 <= len(s) <= 6 and s.isalnum():
        return True
    else:
        return False

        
    
    

main()