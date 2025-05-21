def monthly_payment(present_value,rate, months):
  return(present_value*rate*((1+rate)**months)/(((1+rate)**months)-1))
print(monthly_payment(1000, 0.2, 12))