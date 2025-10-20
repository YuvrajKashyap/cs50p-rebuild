def main():
    message = get_input()
    tweet = shorten(message)

    print(tweet)

def get_input():
    m = input("Input: ")
    return m

def shorten(word):
    t = ""

    for i in word:
        if i in "AEIOUaeiou":
            continue
        t += i
    return t


if __name__ == "__main__":
    main()

