KEYS ='abcdefghijklmnopqrstuvwxyz'

missing = []

query = input("Test for a pangram > ")

for letter in KEYS:
    if letter not in query.lower():
        missing.append(letter)

form_list = str(missing).replace("'", "").replace("[", "").replace("]", "")

if len(missing) > 0:
    print("Missing characters: " + form_list)
else:
    print("Query is a pangram!")

input("> ")