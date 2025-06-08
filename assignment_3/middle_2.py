list_0 = [[1,2,3,4,5], ["a", "b","c","d","e","f"], [True, False]]
new_list = []
for lists in list_0:
    for items in lists:
        new_list.append(items)
print(new_list)
