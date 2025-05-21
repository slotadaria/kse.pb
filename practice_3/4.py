a = float(input(" Enter first number"))
b = float(input(" Enter second number"))
c = float(input(" Enter third number"))

if a>b and a>c:
  print(a)
elif c>b and c>a:
  print(c)
else: 
  print(b)