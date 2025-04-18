grade = int(input("Enter your grade: "))

if grade >= 90:
    print("You got an A!")
elif 80 <= grade < 90:
    print("You got a B!")
elif grade >= 70 and grade < 80:
    print("You got a C!")
elif grade >= 60 and grade < 70:
    print("You got a D!")
else:
    print("You got an F...")
    