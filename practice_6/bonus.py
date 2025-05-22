
import matplotlib.pyplot as plt
import random
balance = 10000
stake = 100
i = 0
i_empty = []
empty = []
while balance>=100 and i <1000:
    x = random.randint(1,37)
    y =  random.randint(1,37)
    i +=1
    if x == y:
        balance += 3500
    else:
        balance -= stake
    empty.append(balance)
    i_empty.append(i)
plt.plot(i_empty, empty)
plt.show()


