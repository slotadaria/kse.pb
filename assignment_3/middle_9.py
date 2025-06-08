list_words = ["претихий", "хліб", "президент","премія","приморський", "телевізор"]
list_p = ["дід", "телевізор", " кіт", "око", "тут", "там"]
i = 0
merged_list = []
while i < len(list_words) and i < len(list_p):
    merged_list.append(list_words[i])
    merged_list.append (list_p[i])
    i += 1
print(merged_list)


