list_n = [ 3, 325, 67, 57, 81, 4583, 210]
sum_n = 0
for i, number in enumerate(list_n):
    if i < 4:
        sum_n += number
    else:
        break
print(sum_n)

