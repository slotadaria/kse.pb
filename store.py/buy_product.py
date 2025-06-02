def buy_product(inventory, transactions, name, quantity, seller_id):
    if inventory[name]["quantity"]>=0:
        inventory[name]["quantity"] -= quantity
        transactions.append(inventory.get(name))
        return inventory.get(name)
    else:
        print("Немає в наявності")
def print_check(transactions, n=1):
    print(transactions[-1].values())



