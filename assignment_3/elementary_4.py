odd_list = [2, 67, 0, 99, 66, 24]
for number in odd_list:
    if number % 2 == 0:
        odd_list.remove(number)
print(odd_list)

