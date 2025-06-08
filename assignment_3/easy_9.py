list_p = ["дід", "телевізор", " кіт", "око", "тут", "там"]
palindrom = []
for word in list_p:
    if word == word[::-1]:
        palindrom.append(word)
    else:
        continue
print(palindrom)
