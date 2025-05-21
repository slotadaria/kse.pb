prices = [23,64,78,2859, 697]
def analyze_prices(prices):
  less = 0
  for i in prices:
    if i < (sum(prices)/len(prices)):
      less +=1
  dic = {"мінімальна ціна": min(prices), "максимальна ціна": max(prices), "середнє значення": sum(prices)/len(prices),"кількість товарів дешевших за середнє":less } 
  return(dic)
print(analyze_prices(prices))