nums = [4, 7, 2, 4, 8, 9, 2, 10, 3, 8]
nums_2 = set(nums)
nums_3 = list(nums_2)
lis = []
for i in nums_3:
  if i%2 != 0:
   nums_3.remove(i)
  else:
    continue
print(nums_3)
