x = "ПророРопЩтаГаоК оаопПгаЛО"
uppercase = []
for word in x:
    if word == word.upper():
        uppercase.append(word)
    else:
        continue
print(uppercase)