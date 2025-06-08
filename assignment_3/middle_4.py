
numbers = [4,6,3,4,76,3,86,6,3,4,1,2,6,3,4,]
numbers_set = set(numbers)
print(numbers_set)
frequenty_list = []
count_frequenty = {}
sorted_list = []
for num_set in numbers_set:
   count_frequenty[num_set] = numbers.count(num_set)
   frequenty_list.append(numbers.count(num_set))
print(count_frequenty)
x =  list(sorted(count_frequenty.values()))
print(x)
for frequency in x:
  sorted_list = count_frequenty.pop(frequency)
print(sorted_list)

