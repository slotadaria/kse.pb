prices = [1,2,6,9,7]
quantities = [4,7,8,12,76]
def weighted_average_price(prices, quantities):
  for i, num in enumerate(prices):
     sums = prices[i]*quantities[i]
  return(sums/sum(quantities))
print(weighted_average_price(prices, quantities))


