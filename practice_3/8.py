month = 0
left = 10000
while left >= 0:
    left = 1.02*(left-1200)
    month += 1
    if left<0:
     print("Потрібно", month)
     break
    else:
        print(month,left)