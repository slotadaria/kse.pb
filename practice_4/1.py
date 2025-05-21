nums = [3, 7, 2, 9, 6]
total = 0
print(list(enumerate(nums)))
for i, num in enumerate(nums):
  total+=num
print(total/(i+1))