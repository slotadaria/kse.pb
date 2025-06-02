def  add_product(inventory, name, quantity):
    if name in inventory:
            inventory[name]["quantity"] += quantity
    else:
        price = int(input("Write price"))
        inventory[name] ={"price": price, "quantity":quantity}
    return inventory
