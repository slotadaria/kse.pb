squares = {1:1, 2:5, 3:34, 4:16, 5:25, 6:3}
for key in squares.keys():
    if key**2 == squares[key]:
        squares[key] = True
    else:
        squares[key] = False
print(squares)