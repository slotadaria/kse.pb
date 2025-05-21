def adjust_for_inflation(income, inflation_rates):
  empty = []
  for i in inflation_rates:
     x = (1+i)*income
     income = (1+i)*income
     i+=1
     empty.append(income)
  print(empty)
(adjust_for_inflation(10000, [0.08, 0.1, 0.07]))