"""
sum_list = [45, 6.89, 0, 96854, 5]   
print(sum(sum_list))  # легший варіант
"""
sum_list = [45, 6.89, 0, 96854, 5]
sum_of_numbers = 0
for number in sum_list:
    sum_of_numbers += number
print(sum_of_numbers)