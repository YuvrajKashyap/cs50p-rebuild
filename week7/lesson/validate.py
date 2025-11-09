# im learning how to validate inputs without the whole tedious if statements
# with the re library

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")

else:
    print("Invalid")
