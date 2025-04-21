members = [
    {"name": "Yuvraj", "age": "19", "gender": "male"},
    {"name": "Tanisha", "age": "22", "gender": "female"},
    {"name": "Suresh", "age": "52", "gender": "male"},
    {"name": "Ruby", "age": "53", "gender": "female"},
    {"name": "Joy", "age": "8", "gender": "male"}
]

for member in members:
    print(member["name"], member["age"], member["gender"], sep=", ")