while True:
 number = float(input("Введіть ваш місячний дохід або '0' для виходу:"))
 if number == 0:
  break
 elif number < 0:
   print("Дохід не може бути від’ємним")
 else: 
  a += number
  print("Ваш дохід збережено:",a)
  