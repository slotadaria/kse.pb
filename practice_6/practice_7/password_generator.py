#generate_password(length= 12, allow_symbols=False) -> str
import random
import string
"""def generate_password():
    x = []
    lower = list(string.ascii_uppercase)
    upper = list(string.ascii_uppercase¶)

    x.append(lower)
    
             
    lowercase = random.choice(string.ascii_lowercase)
"""
def generate_password(x, allow_symbols):
    if allow_symbols == False:
        symbols = string.ascii_letters+string.digits
        end = "".join(random.choices(symbols, k = x))
        return end
    else:
        symbols = string.ascii_letters+string.digits+string.punctuation
        end = "".join(random.choices(symbols, k = x))
        return end

print(generate_password(13, True))



 
