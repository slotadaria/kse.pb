list_words = ["претихий", "хліб", "президент","премія","приморський", "презентація", "телевізор"]
words = []
for word in list_words:
    if word[:3] == "пре" :
        words.append(word)
    else:
        continue
print(words)
