numb = [ 3, 325, 67, 9, 81, 4583, 210]
extract_list = []
for number in numb:
    if number % 3 ==0 and number % 9 != 0 :
        extract_list.append(number)
    else:
        continue
print(extract_list)