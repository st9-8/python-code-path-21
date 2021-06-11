
def cuboide(x,y,z,n):
    "fonction cuboide"
    l = [[i, j, k]
        for i in range(x+1)
        for j in range(y+1)
        for k in range(z+1)
        if i+j+k != n]
    return l