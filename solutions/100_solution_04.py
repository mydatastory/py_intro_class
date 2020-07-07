total = 0
for word in ["red", "green", "blue"]:
    total = total + len(word)
print(total)

lengths = []
for word in ["red", "green", "blue"]:
    lengths.append(len(word))
print(lengths)

words = ["red", "green", "blue"]
result = ""
for word in words:
    result = result + word
print(result)

acronym = ""
for word in ["red", "green", "blue"]:
    acronym = acronym + word[0].upper()
print(acronym)

