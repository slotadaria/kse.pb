list_0 = [87, 8, 13, 1, 5, 43, 86774]
extract_list = []
for number in list_0:
    if number < 40:
        extract_list.append(number)
    else:
        continue
print(max(extract_list))

