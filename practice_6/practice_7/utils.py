
def is_prime(n):
    for i in range(2, round(n/2)):
        if n%i != 0:
            continue
        else:
            return False
    return True
  
print(is_prime(5))
