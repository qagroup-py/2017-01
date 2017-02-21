# First fibonacci number that is greater than 10 millions
a, b = 1, 1

while b < 10 ** 7:
    a, b = b, a + b

print(b)

# First fibonacci number than is longer than 1000 symbols in decimal view
a, b = 1, 1

while len(str(b)) < 1000:  # same as b < 10**999, but latter is faster
    a, b = b, a + b

print(b)
