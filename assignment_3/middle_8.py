list_words = ["претихий", "хліб", "президент","премія","приморський", "презентація", "телевізор"]
number_of_strings = 0
for word in list_words:
    if len(word) > 7:
        number_of_strings += 1
print(number_of_strings)

