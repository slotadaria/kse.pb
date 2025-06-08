dictionary = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36}
dict_keys = list(dictionary.keys())
sorted_keys = []
dict_values = []
for key in dict_keys:
    if key % 2 ==0:
        sorted_keys.append(key)
for key in sorted_keys:
 dict_values.append(dictionary[key])
print(sum(dict_values))
