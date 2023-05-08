squares = []

# for x in range(5):
#     squares.append(lambda: x ** 2)


for x in range(5):
    squares.append(lambda n=x: n ** 2 )


for a in squares:
    print(a())
