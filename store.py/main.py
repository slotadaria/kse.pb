import  data
import add_product as ap
import buy_product as buy
import sellers as sel
while True:
    action = int(input())
    if action == 1: 
        name = input("Name")
        quantity = int(input("Quantity"))
        ap.add_product(data.inventory, name,  quantity)
    elif action == 2 :
        name = input("Name")
        quantity = int(input("Quantity"))
        seller_id = input("ID")
        buy.buy_product(data.inventory, sel.transactions, name, quantity, seller_id)
        buy.print_check(sel.transactions, n = 1)
    elif action == 3:
        print(data.inventory)
    else:
        break
  