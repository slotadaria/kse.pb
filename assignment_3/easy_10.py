numb = [ 3, 325, 67, 9, 81, 4583, 210]
extract_list = []
for number in numb:
    if number % 3 ==0 :
        extract_list.append(True)
    else:
        extract_list.append(False)
print(extract_list)