first_list = [87, 8, 13, 1, 5, 43, 86774]
second_list = [4,6,3,4,76,3,86,6,3,4,1,2,6,3,4,]
merged_list = []
for number_1 in first_list:
    if number_1 > 10:
        merged_list.append(number_1)
for number_2 in second_list:
    if number_2 > 10:
        merged_list.append(number_2)
print(merged_list)
