def comprendreLitse(n, a, b, c):
    x = list(range(a+1))
    y = list(range(b+1))
    z = list(range(c+1))
    s = [[i, j, k] for i in x for j in y for k in z if i + j + k != n]
    print(s)


comprendreLitse(3, 1, 2, 1)

