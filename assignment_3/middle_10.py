list_0 = [87, 8, 13, 43, 86774]
extract_list = []
multiply_list = []
for number in list_0:
    if number > 40:
        extract_list.append(number)
for number in extract_list:
    number *= 5
    multiply_list.append(number)
print(multiply_list)
