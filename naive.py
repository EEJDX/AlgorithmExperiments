def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

def rec_naive(a, b):
    print("count me!")
    if a == 0:
        return 0
    return b + rec_naive(a-1, b)


def russian(a, b):
    x = a; y = b
    z = 0
    while x > 0:
        if x == 7 and z == 84: print(y)
        if x % 2 == 1: z = z + y
        y = y << 1
        x = x >> 1
    return z

def countClique(n):
    return 2 + n + (n * (n - 1)) / 2


def clique(n):
    print ("in a clique...")
    for j in range(n):
        for i in range(j):
            print (i, " is friends with ", j)
