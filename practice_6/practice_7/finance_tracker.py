transactions = []
def add_transaction(transactions, amount, transaction_type, category):
    
    diction = { "amount":amount,
              "transaction_type": transaction_type,
              "category":category }
    return transactions.append(diction)
add_transaction(transactions, 10000, "дохід", "зарплата")
add_transaction(transactions, 2500, "витрата", "їжа")
add_transaction(transactions, 1500, "витрата", "транспорт")
print(transactions)

def get_balance(transactions):
    total = 0
    for transact in transactions:
     if transact.get("transaction_type")  == "дохід":
        total += transact.get("amount")
     else:
        total -= transact.get("amount")
    print(total)
get_balance(transactions)
      
    
