grades = [
    [90, 85, 88],
    [75, 80, 79],
    [95, 92, 96],
    [88, 85, 84]
]
empty = []
for lis in grades:
  x = [sum(lis)/len(lis)]
  empty.append(x)
for i, num in enumerate(empty):
   max(empty)
print(i, max(empty),grades[i-1])


